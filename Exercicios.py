from functools import reduce
import math

#1.Usando list comprehension, defina uma função add10toall :: [Int] -> [Int], que receba uma lista e adicione o
#valor 10 a cada elemento dessa lista, produzindo outra lista. Exemplo:
def exercicio1(lista):
    print("Exercico 1:")
    print([x+10 for x in lista])

#2.Usando a função zip com list comprehension e outras funções auxiliares, escreva uma função dotProd :: [Int] -> [Int] -> Int
#que calcule o somatório dos produtos dos pares de elementos de duas listas, conforme o exemplo:
def exercicio2(lista, lista1):
    print("Exercico 2:")
    print(reduce(lambda x, y: x+y, [x * y for x, y in zip(lista, lista1)]))

#Suponha que uma cor seja representada por uma tupla (Int,Int,Int), contendo valores (R=red,G=Green,B=blue). Considerando isso,
#crie uma função strColor :: (Int,Int,Int) -> String que receba uma tupla representando uma cor (R=red,G=Green,B=blue) e retorne
#uma string no formato "rgb(R,G,B)".
def exercicio3(r, g, b):
    print("Exercico 3:")
    print("rgb"+"(" + str(r) + ", " + str(g) + ", " + str(b) +")")

#Crie uma função itemize :: [String] -> [String] que receba uma lista de strings e adicione tags HTML <li> e </li> antes e depois
#de cada string. Resolva esta questão usando lambda.
def exercicio4(lista):
    print("Exercico 4:")
    print(list(map(lambda x: "<li>"+x+"<li>", lista)))

#Escreva uma função onlyShorts :: [String] -> [String] que receba uma lista de strings e retorne outra lista contendo somente as
#strings cujo tamanho seja menor que 5.
def exercico5(lista):
    print("Exercico 5:")
    print(list(filter(lambda x: len(x) < 5, lista)))

#A vacinação contra COVID19 no Brasil aconteceu por grupos prioritários. As equipes responsáveis pelas ações de vacinação
#registram em um sistema cada dose de vacina aplicada, classificando cada indivíduo em um dos grupos previstos. No caso de idosos,
#este grupo prioritário foi organizado em 5 faixas etárias: de 60 a 64 anos, de 65 a 69 anos. de 70 a 74 anos, de 75 a 79 anos
#e de 80 anos ou mais. No sistema, essas faixas são identificadas, respectivamente, pelas siglas "IDO64", "IDO69", "IDO74", "IDO79"
#e "IDO80". Sabendo disso, crie uma função faixaIdoso :: Int -> String que receba uma idade e retorne o código da faixa
#correspondente. Caso a idade não se enquadre em nenhuma das faixas do grupo prioritário, o código será "ND" (não definido)
def exercicio6(x):
    if x < 60:
       return "ND"
    elif x <= 64:
       return "IDO64"
    elif x <= 69:
        return "IDO69"
    elif x <= 74:
        return "IDO74"
    elif x <= 79:
        return "IDO79"
    else:
        return "IDO80"

#Usando list comprehension, crie uma função classifIdosos :: [(String,Int)] -> [(String,Int,String)] que receba uma lista de tuplas
#contendo nome e idade, e retorne uma lista de tuplas com nome, idade e o código da faixa correspondente (faixaIdoso)
def exercicio7(lista):
   print("Exercicio 7:")
   print([(x[0], x[1], exercicio6(x[1])) for x in lista])

#Escreva uma função changeNames :: [String] -> [String] que receba uma lista de nomes e adicione o prefixo "Super " às strings que
#começarem com a letra A (maiúscula), deixando as demais inalteradas. A lista resultante, portanto, terá a mesma quantidade de
#strings da lista original.

def exercicio8(lista):
    print("Exercicio 8:")
    print(list(map(lambda y: "Super " + y, filter(lambda x : x[0] == 'A', lista))))

#Usando list comprehension, defina uma função selectExpr :: [Int] -> [Int], que receba uma lista e selecione somente os valores
#pares entre 20 e 50, inclusive, produzindo outra lista.
def exercicio9(lista):
    print("Exercicio 9:")
    print([x for x in lista if x%2 == 0 and x < 50 and x > 20])

#Escreva uma função calcAreas que, dada uma lista de valores de raios de círculos, retorne uma lista com a área correspondente
# a cada raio.
def exercicio10(lista):
    print("Exercicio 10:")
    print(list(map(lambda x : math.pi * (x**2), lista)))

if __name__ == '__main__':
    exercicio1([2, 4, 45, 67, 89])
    exercicio2([1, 6, 16, 60],[20, 62, 92,102])
    exercicio3(3, 5, 6)
    exercicio4(["vamos", "garafa", "volume", "iterador"])
    exercico5(["lista", "garafa", "oi", "uau", "ademais"])
    print("Exercico 6:")
    print(exercicio6(63))
    exercicio7([("luiza", 52), ("ivan", 72), ("joao", 99), ("calebi", 64)])
    exercicio8(["luiza", "AivAn", "Ajoao", "clebi"])
    exercicio9([1, 2, 3, 22, 23, 34, 35, 47, 80, 90, 100, 10000])
    exercicio10([20, 5, 6, 7, 200, 67])
