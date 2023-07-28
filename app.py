from flask import Flask, render_template, request
from Clima import ClimaAPI

app = Flask(__name__)


# Dicionário com estados brasileiros e suas respectivas cidades
cidades_por_estado = {
    "Acre": ["Rio Branco"],
    "Alagoas": ["Maceió"],
    "Amapá": ["Macapá"],
    "Amazonas": ["Manaus"],
    "Bahia": ["Salvador"],
    "Ceará": ["Fortaleza"],
    "Distrito Federal": ["Brasília"],
    "Espírito Santo": ["Vitória"],
    "Goiás": ["Goiânia"],
    "Maranhão": ["São Luís"],
    "Mato Grosso": ["Cuiabá"],
    "Mato Grosso do Sul": ["Campo Grande"],
    "Minas Gerais": ["Belo Horizonte"],
    "Pará": ["Belém"],
    "Paraíba": ["João Pessoa"],
    "Paraná": ["Curitiba"],
    "Pernambuco": ["Recife"],
    "Piauí": ["Teresina"],
    "Rio de Janeiro": ["Rio de Janeiro"],
    "Rio Grande do Norte": ["Natal"],
    "Rio Grande do Sul": ["Porto Alegre"],
    "Rondônia": ["Porto Velho"],
    "Roraima": ["Boa Vista"],
    "Santa Catarina": ["Florianópolis"],
    "São Paulo": ["São Paulo"],
    "Sergipe": ["Aracaju"],
    "Tocantins": ["Palmas"],
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        estado = request.form.get("estado")
        cidade = request.form.get("cidade")

        if estado and cidade:
            cidade = cidade.capitalize()
            weather_api = ClimaAPI()
            clima_info = weather_api.informacoes_clima(cidade)

            return render_template(
                "clima.html",
                cidade=cidade,
                **clima_info,
                temperatura=clima_info["temperatura_celsius"]
            )
        else:
            return render_template(
                "index.html",
                cidades=cidades_por_estado,
                erro="Por favor, selecione um estado e uma cidade.",
            )

    return render_template("index.html", cidades=cidades_por_estado)


if __name__ == "__main__":
    app.run(debug=True)
