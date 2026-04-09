from flask import Flask, request
import random
import os

app = Flask(__name__)

# 🔹 HOME
@app.route("/", methods=["GET"])
def home():
    return """
    <html>
    <head>
        <title>Teste gay</title>

        <style>
            body {
                margin: 0;
                text-align: center;
                font-family: Arial;
                color: white;
                background: linear-gradient(red, orange, yellow, green, blue, purple);
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

    <h1>🏳️‍🌈 Veja se você é gay 🏳️‍🌈</h1>
    
    <form action="/resultado" method="POST">
        <input type="text" name="nome" placeholder="Digite seu nome..." required>
        <br>
        <button type="submit">INICIAR</button>
    </form>

    </body>
    </html>
    """


# 🔹 RESULTADO
@app.route("/resultado", methods=["POST"])
def resultado():
    nome = request.form.get("nome")

    # 🔥 MODO RYAN (VÍDEO FUNCIONANDO)
    if nome and nome.strip().lower().startswith("ryan"):
        return """
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    background: black;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                video {
                    width: 100vw;
                    height: 100vh;
                    object-fit: contain;
                }

                button {
                    position: absolute;
                    bottom: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    padding: 10px 20px;
                    background: white;
                    color: black;
                    border: none;
                    cursor: pointer;
                }
            </style>
        </head>

        <body>

        <video id="video" autoplay loop muted playsinline>
            <source src="/static/layout.mp4" type="video/mp4">
        </video>

        <button onclick="window.location.href='/'">
            FAZER O TESTE NOVAMENTE
        </button>

        <script>
            const video = document.getElementById("video");

            video.play().then(() => {
                video.muted = false;
            }).catch(() => {
                document.body.addEventListener("click", () => {
                    video.play();
                }, { once: true });
            });
        </script>

        </body>
        </html>
        """

    # 🔽 MODO NORMAL
    porcentagem = random.randint(90, 100)

    frases = [
        "odeia molieres",
        "gosta do negão dentro",
        "já fez ménage com homens kkj",
        "gosta do grosso",
        "senta na jiromba todo dia"
    ]

    motivo = random.choice(frases)

    resultado = f"{nome}, nível de viadagem: {porcentagem}% - {motivo}"

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

    <button onclick="window.location.href='/'">
        TESTAR DE NOVO
    </button>

    <audio id="musica" autoplay muted>
        <source src="/static/musica.mp3" type="audio/mpeg">
    </audio>

    <script>
    function ativarModo() {{
        let audio = document.getElementById("musica");

        audio.play().then(() => {{
            audio.muted = false;
        }}).catch(() => {{
            document.body.addEventListener("click", () => {{
                audio.play();
            }}, {{ once: true }});
        }});

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
    </script>

    </body>
    </html>
    """


# 🔥 RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))