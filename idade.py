from datetime import date

#Data atual
anoAtual = date.today().year
mesAtual = date.today().month
diaAtual = date.today().day

#Data de nascimento
nascimento = date(1981, 5, 25)
anoNascimento = nascimento.year
mesNascimento = nascimento.month
diaNascimento = nascimento.day

#Recebendo a idade em anos
idade = anoAtual - anoNascimento

#Mês de nascimento sendo MAIOR que o atual
if mesNascimento > mesAtual:
    idade -= 1
    mes = 12 - (mesNascimento - mesAtual)
    if diaNascimento > diaAtual:
        mes -= 1
        dia = 30 - (diaNascimento - diaAtual) #Base no mês de 30 dias
    elif diaNascimento == diaAtual:
        dia = 0
    elif diaNascimento < diaAtual:
        dia = diaAtual - diaNascimento

#Mês de nascimento sendo IGUAL ao atual
if mesNascimento == mesAtual:
    mes = 0
    if diaNascimento > diaAtual:
        idade -= 1
        dia = 30 - (diaNascimento - diaAtual) #Base em mês de 30 dias
    elif diaNascimento == diaAtual:
        print('Parabéns! Feliz Aniversário')
        dia = 0
    elif diaNascimento < diaAtual:
        dia = diaAtual - diaNascimento

#Mês de nascimento sendo MENOR que o atual
if mesNascimento < mesAtual:
    mes = mesAtual - mesNascimento
    if diaNascimento > diaAtual:
        mes -= 1
        dia = 30 - (diaNascimento - diaAtual) #Base em mês de 30 dias
    elif diaNascimento == diaAtual:
        dia = 0
    elif diaNascimento < diaAtual:
        dia = diaAtual - diaNascimento
        
print(idade)
print(mes)
print(dia)