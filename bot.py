from flask import Flask, request, jsonify
import unicodedata

def limpiar_texto(texto):
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    texto = texto.replace("¿", "").replace("?", "")
    return texto

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    mensaje = limpiar_texto(data.get("mensaje", ""))

    if any(palabra in mensaje for palabra in ["habitacion", "habitaciones", "cuarto", "cuartos"]):
        respuesta = "Hola, si tenemos habitaciones disponibles. ¿Quieres saber los precios?"
    elif any(palabra in mensaje for palabra in ["precio", "precios","coste", "costo"]):
        respuesta = "El precio de las habitaciones es de $800 MXN por noche."
    elif any(palabra in mensaje for palabra in ["reservar", "reservacion", "reserva"]):
        #cambiar las x por el numero de telefono del asesor
        respuesta = "¡Perfecto! Te conectamos con un asesor de reservaciones en WhatsApp. Haz clic aquí: https://wa.me/xxxxxxxxxxxxx?text=Hola,%20quiero%20hacer%20una%20reservación"
    else:
        respuesta = "Hola, soy velikan, ¿en qué puedo ayudarte?"

    return jsonify({"respuesta": respuesta})


if __name__ == '__main__':
    app.run(debug=True)
