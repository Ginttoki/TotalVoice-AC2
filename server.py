from flask import Flask, url_for, render_template, request
from totalvoice.cliente import Cliente

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def enviar_sms():
    celular = request.form.get('numero')
    texto = request.form.get('mensagem')
    cliente = Cliente("883737a6404a138640e5e25ea916516c", 'https://api2.totalvoice.com.br/sms')
    response = cliente.sms.enviar(celular,texto)
    print(response)
    return render_template('index.html')
    
    



if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)


