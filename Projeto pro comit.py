print('='*30)
print('     Controle de gastos ')
print('='*30)

dinheiro_do_usuario = float(input('Digite quanto dinheiro ha na sua conta : '))
gastos = float(input('Digite o valor da compra '))
restante = dinheiro_do_usuario - gastos

print(f'Resta na sua conta : {restante} ')
