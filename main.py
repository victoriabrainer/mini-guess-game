from random import randint

your_name = input('Olá, qual o seu nome? ')
print(f'Ok! {your_name}, eu estou escolhendo um número de 1 a 10. Você consegue adivinhar? ')

guessed_number = randint(1, 10)
attempts_number = 3

for attempt in range(1, attempts_number + 1):
  chosen_number = int(input('Escolha um número: '))
  if chosen_number == guessed_number:
    print(f'Parabéns, você acertou em {attempt} tentativas!')
    break
  elif chosen_number > guessed_number:
    print('Escolha um número menor')
  else:
    print('Escolha um número maior')
print(f'O número era {guessed_number}. Obrigada por jogar!')