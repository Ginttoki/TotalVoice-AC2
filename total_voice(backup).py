from totalvoice.cliente import Cliente

cliente = Cliente("9b691b4f5ebfe5e32d28186be41965e8", 'https://api2.totalvoice.com.br/sms')

'''numero_destino = "11967716409"
mensagem = "teste envio sms"'''
numero_destino = input('Digite o numero:\n')
mensagem = input('Digite a mensagem solicitada:\n')
response = cliente.sms.enviar(numero_destino, mensagem)
print(response)
