import requests
from bs4 import BeautifulSoup

def temperatura_porto_alegre():
    """
    CPTEC/INPE - Temperatura de Porto Alegre - scraping simples (1 informação)
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
    }

    url = "https://www.cptec.inpe.br/previsao-tempo/rs/porto-alegre"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        temperatura = soup.find('span', class_='temp')  

        if temperatura:
            print(f"🌡️ Temperatura atual em Porto Alegre: {temperatura.text.strip()}")
        else:
            print("🔍 Não foi possível encontrar a temperatura atual no site do CPTEC.")

    except Exception as e:
        print(f"❌ Erro ao obter dados: {e}")


temperatura_porto_alegre()
