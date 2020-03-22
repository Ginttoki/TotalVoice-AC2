from flask import Flask, url_for, render_template, request
from totalvoice.cliente import Cliente

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sms/", methods=['GET','POST'])
def enviar_sms():
    celular = request.form.get('numero')
    texto = request.form.get('mensagem')
    print(celular)
    print(texto)
    cliente = Cliente("da6c070dff516c9b3ac31e0ad75b7d3c", 'https://api2.totalvoice.com.br/sms')
    response = cliente.sms.enviar(celular,texto)
    print(response)
    return render_template('index.html')
    
    



if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)


""" cliente = Cliente("da6c070dff516c9b3ac31e0ad75b7d3c", 'https://api2.totalvoice.com.br/sms')
    response = cliente.sms.enviar(celular,mensagem)
    print(response) """