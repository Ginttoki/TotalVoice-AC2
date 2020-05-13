from flask import Flask, url_for, render_template, request
from totalvoice.cliente import Cliente

app = Flask(__name__)

#Para utilizar a aplicação deve ser criada uma conta no totalvoice e pegar a key gerada.

@app.route("/", methods=['POST'])
def enviar_sms():
    celular = request.form.get('numero')
    texto = request.form.get('mensagem')
    cliente = Cliente("insira sua key para utilizar a aplicação", 'https://api2.totalvoice.com.br/sms')
    response = cliente.sms.enviar(celular,texto)
    print(response)
    return render_template('index.html')

@app.route("/", methods=['GET'])
def mostrar_tela():
    return render_template ('index.html')


    
    



if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)


