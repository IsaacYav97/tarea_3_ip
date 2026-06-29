from flask import Flask, render_template_string, request

app = Flask(__name__)

# Lógica pura de Python (Esto es lo que probará pytest para tu nota)
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# Guardamos el HTML, CSS y la lógica responsiva en el string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Temperatura</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>

        body{
            margin:0;
            padding:0;
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            font-family:Arial, Helvetica, sans-serif;

            background:linear-gradient(135deg,#4b0082,#5f27cd,#54a0ff);
        }

        .contenedor{

            width:430px;
            background:white;
            border-radius:20px;
            padding:40px;
            box-shadow:0px 15px 35px rgba(0,0,0,.25);

        }

        h1{

            text-align:center;
            color:#4b0082;
            font-weight:bold;

        }

        p{

            text-align:center;
            color:#666;

        }

        .icono{

            font-size:70px;
            text-align:center;
            margin-bottom:15px;

        }

        .form-control{

            border-radius:12px;
            height:50px;

        }

        .btn-convertir{

            width:100%;
            border:none;
            border-radius:12px;
            background:#5f27cd;
            color:white;
            height:50px;
            font-size:18px;
            transition:.3s;

        }

        .btn-convertir:hover{

            background:#341f97;
            transform:scale(1.03);

        }

        .resultado{

            margin-top:25px;
            padding:20px;
            background:#eef4ff;
            border-left:6px solid #5f27cd;
            border-radius:10px;
            text-align:center;

        }

        .resultado h5{

            color:#341f97;
            font-weight:bold;

        }

        .resultado span{

            font-size:20px;
            color:#333;

        }

    </style>

</head>

<body>

<div class="contenedor">

    <div class="icono">
        🌡️
    </div>

    <h1>Conversor Celsius</h1>

    <p>
        Convierte grados Celsius a Fahrenheit de manera rápida.
    </p>

    <form method="POST" action="/">

        <div class="mb-4">

            <input
                type="number"
                name="celsius"
                step="any"
                class="form-control text-center"
                placeholder="Ingrese °C"
                required
                value="{{ celsius_enviado }}">

        </div>

        <button class="btn-convertir">
            Convertir
        </button>

    </form>

    {% if resultado is not none %}

    <div class="resultado">

        <h5>Resultado</h5>

        <span>

            {{ celsius_enviado }} °C =
            <strong>{{ resultado }} °F</strong>

        </span>

    </div>

    {% endif %}

</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    celsius_enviado = ""
    
    if request.method == 'POST':
        try:
            celsius_enviado = request.form.get('celsius', '')
            # Conversión usando nuestra función matemática
            resultado = celsius_a_fahrenheit(float(celsius_enviado))
            
            # Pequeña mejora visual (opcional): redondear a 2 decimales si el resultado es muy largo
            if isinstance(resultado, float):
                resultado = round(resultado, 2)
                
        except ValueError:
            resultado = "Valor inválido"
            
    return render_template_string(HTML_TEMPLATE, resultado=resultado, celsius_enviado=celsius_enviado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)