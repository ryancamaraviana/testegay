from flask import Flask, request, redirect, url_for
import random

app = Flask(__name__)

# 🔹 PÁGINA INICIAL
@app.route("/", methods=["GET"])
def home():
    return """
    <html>
    <head>
        <title>Sistema Supremo</title>

        <style>
            body {
                margin: 0;
                text-align: center;
                font-family: Arial;
                color: white;
                background: linear-gradient(
                    red, orange, yellow, green, blue, purple
                );
            }

            input {
                padding: 10px;
                margin: 10px;
                border: none;
            }

            button {
                padding: 10px 20px;
                background: black;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>

    <body>

    <h1>🏳️‍🌈 SISTEMA SUPREMO 🏳️‍🌈</h1>

    <form action="/resultado" method="POST">
        <input type="text" name="nome" placeholder="Digite seu nome..." required>
        <br>
        <button type="submit">INICIAR</button>
    </form>

    </body>
    </html>
    """


# 🔹 PÁGINA DE RESULTADO
@app.route("/resultado", methods=["POST"])
def resultado():
    nome = request.form.get("nome")

    porcentagem = random.randint(80, 100)

    frases = [
        "fala 'coé' automaticamente",
        "vive na praia",
        "escuta funk no talo",
        "usa chinelo até em casamento",
        "já chamou alguém de 'cria'"
    ]

    motivo = random.choice(frases)

    resultado = f"{nome}, nível de carioca: {porcentagem}% 😂 - {motivo}"

    return f"""
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                text-align: center;
                font-family: Arial;
                color: white;
                overflow: hidden;
                background: black;
            }}

            .rainbow {{
                animation: arcoiris 0.3s linear infinite;
            }}

            @keyframes arcoiris {{
                0% {{ background: red; }}
                20% {{ background: orange; }}
                40% {{ background: yellow; }}
                60% {{ background: green; }}
                80% {{ background: blue; }}
                100% {{ background: purple; }}
            }}

            .flag {{
                position: absolute;
                font-size: 30px;
                animation: subir 3s linear forwards;
            }}

            @keyframes subir {{
                0% {{ bottom: -50px; }}
                100% {{ bottom: 100%; }}
            }}

            button {{
                padding: 10px 20px;
                background: white;
                color: black;
                border: none;
                cursor: pointer;
                margin-top: 20px;
            }}
        </style>
    </head>

    <body onload="ativarModo()">

    <h1>⚠️ PROCESSANDO ⚠️</h1>
    <h2>{resultado}</h2>

    <button onclick="voltar()">TESTAR DE NOVO</button>

    <audio id="musica" autoplay>
        <source src="/static/musica.mp3" type="audio/mpeg">
    </audio>

    <script>
    function ativarModo() {{
        let audio = document.getElementById("musica");
        audio.play();

        document.body.classList.add("rainbow");

        for (let i = 0; i < 30; i++) {{
            let flag = document.createElement("div");
            flag.innerHTML = "🏳️‍🌈";
            flag.classList.add("flag");

            flag.style.left = Math.random() * 100 + "%";
            flag.style.animationDuration = (2 + Math.random() * 3) + "s";

            document.body.appendChild(flag);
        }}
    }}

    function voltar() {{
        window.location.href = "/";
    }}
    </script>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)