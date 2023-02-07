import random, string

tamanho = int(input ('Digite o taamanho de senha que você deseja: '))

nome = input ('Digite o seu nome: ')

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;ç/?'

rnd = random.SystemRandom() 

print(nome,'Sua senha segura é:')
print(''.join(rnd.choice(chars) for i in range (tamanho)))

