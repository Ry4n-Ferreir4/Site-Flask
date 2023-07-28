import requests


class ClimaAPI:
    def __init__(self):
        self.api_key = "API_KEY"

    def informacoes_clima(self, city):
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&lang=pt_br"
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic["weather"][0]["description"]
        temperatura = requisicao_dic["main"]["temp"]
        temperatura_celsius = int(temperatura - 273.15)
        pressao = requisicao_dic["main"]["pressure"]
        umidade = requisicao_dic["main"]["humidity"]
        vento_velocidade = requisicao_dic["wind"]["speed"]
        vento_direcao = requisicao_dic["wind"]["deg"]
        nuvens = requisicao_dic["clouds"]["all"]

        # Criar um dicionário com todas as informações
        clima_info = {
            "descricao": str(descricao).capitalize(),
            "temperatura_celsius": temperatura_celsius,
            "pressao": pressao,
            "umidade": umidade,
            "vento_velocidade": vento_velocidade,
            "vento_direcao": vento_direcao,
            "nuvens": nuvens,
        }

        return clima_info
