# 🐍 Python Async Scraper - IMDB Movie Data Extraction

Um extrator de dados de alta performance desenvolvido em **Python**, focado na coleta automatizada de informações do IMDB. O projeto utiliza técnicas avançadas de programação assíncrona para processar centenas de páginas simultaneamente, otimizando o tempo de execução e a eficiência de rede.

---

# 📝 Resumo (Resume)
Neste projeto, implementei um Web Scraper robusto utilizando as bibliotecas **aiohttp** para requisições HTTP não bloqueantes e **BeautifulSoup** para o parsing do HTML. A arquitetura foi desenhada para lidar com concorrência através de um **Semáforo (Semaphore)**, limitando o número de acessos simultâneos para evitar bloqueios por parte do servidor. Os dados coletados (título, data, avaliação e sinopse) são processados e salvos em tempo real em um arquivo CSV, demonstrando um fluxo completo de ETL (Extract, Transform, Load).



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Aiohttp](https://img.shields.io/badge/Aiohttp-Async-blue?style=for-the-badge)](https://docs.aiohttp.org/)
[![BeautifulSoup](https://img.shields.io/badge/BS4-Scraping-green?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)
[![Asyncio](https://img.shields.io/badge/Asyncio-Concurrency-orange?style=for-the-badge)](https://docs.python.org/3/library/asyncio.html)

## 📋 Funcionalidades em Destaque
* **Execução Assíncrona:** Uso de `asyncio.gather` para disparar múltiplas tarefas de extração sem esperar que uma termine para começar a próxima.
* **Controle de Concorrência:** Implementação de `asyncio.Semaphore` para limitar o script a 10 requisições simultâneas, garantindo estabilidade e ética no scraping.
* **Simulação de Navegador Real:** Uso de Headers customizados (`User-Agent`) e delays aleatórios com `random.uniform` para mimetizar o comportamento humano.
* **Parsing de HTML Complexo:** Localização precisa de dados através de atributos `data-testid` e seletores CSS avançados no BeautifulSoup.
* **Persistência de Dados em CSV:** Escrita automatizada de resultados utilizando o módulo `csv` com suporte a encoding UTF-8.
* **Métricas de Performance:** Medição do tempo total de execução para demonstrar o ganho de velocidade da abordagem assíncrona sobre a síncrona.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Este projeto representa o coração do meu foco profissional: o **Back-End com Python**. Após dominar o ecossistema Front-End, agora aplico essa lógica para construir ferramentas de automação e coleta de dados. Entender a estrutura do DOM (que aprendi no Front) me permite criar scrapers muito mais precisos, enquanto o Python me dá o poder de processar grandes volumes de informação de forma performática e inteligente.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=3776AB)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=3776AB)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=3776AB)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para demonstrar proficiência em Python assíncrono e engenharia de dados aplicada.*
