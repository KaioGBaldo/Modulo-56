import asyncio
import aiohttp
import csv
import random
from bs4 import BeautifulSoup
from asyncio import Semaphore
import time

# =========================================================
# CONFIGURAÇÕES GERAIS
# =========================================================

# URL base do IMDB
BASE_URL = "https://www.imdb.com"

# Página com os filmes mais populares
POPULAR_MOVIES_URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

# Cabeçalho para simular um navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Número máximo de requisições simultâneas
MAX_CONCURRENT_REQUESTS = 10

# Semáforo para controle de concorrência
semaphore = Semaphore(MAX_CONCURRENT_REQUESTS)


# =========================================================
# FUNÇÃO ASSÍNCRONA PARA BUSCAR UMA PÁGINA
# =========================================================
async def fetch(session, url):
    """
    Realiza uma requisição HTTP assíncrona.
    O semáforo limita a quantidade de requisições simultâneas.
    """
    async with semaphore:
        # Pequeno delay aleatório para evitar bloqueio do site
        await asyncio.sleep(random.uniform(0, 0.2))
        async with session.get(url, headers=HEADERS) as response:
            return await response.text()


# =========================================================
# FUNÇÃO PARA EXTRAIR DADOS DE UM FILME
# =========================================================
async def extract_movie_details(session, movie_url, writer):
    """
    Extrai informações individuais de um filme:
    - Título
    - Data de lançamento
    - Avaliação
    - Sinopse
    """
    html = await fetch(session, movie_url)
    soup = BeautifulSoup(html, "html.parser")

    title = None
    release_date = None
    rating = None
    plot = None

    # Título do filme
    title_tag = soup.find("h1")
    if title_tag:
        title = title_tag.get_text(strip=True)

    # Data de lançamento
    date_tag = soup.find("a", href=lambda h: h and "releaseinfo" in h)
    if date_tag:
        release_date = date_tag.get_text(strip=True)

    # Avaliação do filme
    rating_tag = soup.find(
        "div",
        attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"}
    )
    if rating_tag:
        rating = rating_tag.get_text(strip=True)

    # Sinopse
    plot_tag = soup.find("span", attrs={"data-testid": "plot-xs_to_m"})
    if plot_tag:
        plot = plot_tag.get_text(strip=True)

    # Grava no CSV apenas se todos os dados existirem
    if all([title, release_date, rating, plot]):
        print(title, release_date, rating)
        writer.writerow([title, release_date, rating, plot])


# =========================================================
# FUNÇÃO PRINCIPAL DE EXTRAÇÃO DOS FILMES
# =========================================================
async def extract_movies():
    """
    Acessa a página principal do IMDB,
    coleta os links dos filmes e executa
    as requisições assíncronas para cada filme.
    """
    async with aiohttp.ClientSession() as session:
        main_page = await fetch(session, POPULAR_MOVIES_URL)
        soup = BeautifulSoup(main_page, "html.parser")

        # Localiza a lista de filmes
        movies_section = soup.find(
            "div",
            attrs={"data-testid": "chart-layout-main-column"}
        )
        movie_items = movies_section.find_all("li")

        # Monta os links completos dos filmes
        movie_links = [
            BASE_URL + movie.find("a")["href"]
            for movie in movie_items
            if movie.find("a")
        ]

        # Cria o arquivo CSV para salvar os dados
        with open("movies.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["title", "release_date", "rating", "plot"])

            # Cria tarefas assíncronas para cada filme
            tasks = [
                extract_movie_details(session, link, writer)
                for link in movie_links
            ]

            # Executa todas as tarefas de forma concorrente
            await asyncio.gather(*tasks)


# =========================================================
# FUNÇÃO MAIN
# =========================================================
def main():
    """
    Função principal que mede o tempo
    total de execução do web scraping.
    """
    start = time.time()
    asyncio.run(extract_movies())
    end = time.time()
    print("Tempo total de execução:", end - start)


# =========================================================
# EXECUÇÃO DO SCRIPT
# =========================================================
if __name__ == "__main__":
    main()
