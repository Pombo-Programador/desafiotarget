##Questão 1:


def fibbonaci(num):
    fiblist = [0,1]
    print(fiblist[0])
    print(fiblist[1])
    if num in fiblist:
        return True
    fibnum = 0
    while(fibnum < num):
        fibnum = fiblist[0] + fiblist[1]
        print(fibnum)
        if fibnum == num:
            return 1
        fiblist.pop(0)
        fiblist.append(fibnum)
    return 0


def questao1():
    print("Digite um número positivo inteiro\n")
    num = int(input())
    res = fibbonaci(num)
    if res == 1:
        print("Faz parte da Sequência Fibbonaci")
    if res == 0:
        print("Não faz parte da Sequência Fibbonaci")


def stringAcheck(frase):
    vezesdeA = frase.lower().count('a')
    return vezesdeA

def questao2():
    print("Digite uma frase qualquer\n")
    frase = input()
    res = stringAcheck(frase)
    print("A letra 'a' aparece " + str(res)+ " vezes.")


questao1()
questao2()
  