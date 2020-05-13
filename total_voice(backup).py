from totalvoice.cliente import Cliente

cliente = Cliente("coloque sua key", 'https://api2.totalvoice.com.br/sms')

'''numero_destino = "11111111111"
mensagem = "teste envio sms"'''
numero_destino = input('Digite o numero:\n')
mensagem = input('Digite a mensagem solicitada:\n')
response = cliente.sms.enviar(numero_destino, mensagem)
print(response)
