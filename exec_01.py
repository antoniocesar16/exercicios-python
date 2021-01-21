# Repetiços

rodando = True
while rodando:
    nota = int(input("Nota entre 0 e 10: "))
    if(nota > 10):
        print("Nota invalida!")
    else:
        rodando = False
        print("Obrigado pela sua nota!")