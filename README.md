# Programação funcional em Python:

## Funções Anônimas (lambda)
Em Python, uma função anônima significa que uma função não tem nome. Como já sabemos, a palavra-chave def é usada para definir uma função normal em Python.
Da mesma forma, a palavra-chave lambda é usada para definir uma função anônima em Python, elas são da mesma forma que as funções lambda em haskell.

Sintaxe: argumentos lambda: expressão

Comparando uma função normal em python com uma função anonima que faz a mesma coisa:
def cube(y): 
    return y*y*y 
  
lambda_cube = lambda y: y*y*y 


## Filter:
A função filter() como diz o nome ela filtra uma lista dada, com a ajuda de uma função que testa cada elemento na sequência para ser verdadeiro ou não.
Com a lista resultante sendo apenas com os elementos verdadeiros.

sintaxe: filter (função, sequência)
Ex: Onde queremos que sejam mantidos apenas os elementos pares desta lista.
lista1 = [1, 4, 9, 16, 2]

list(filter(lamdba x: x % 2 == 0, lista1))  



## Map:
A função map() em Python recebe uma função e uma lista como argumento. Cada elemento da lista é aplicada na função, e uma nova 
lista é retornada que contém todos os elementos modificados pela função.

Sintaxe: map(função, sequência)
Ex: Onde temos uma lista de graus em celsius e queremos transformar em fahrenheits.
temp = [0, 22.5, 40, 100]

F_temp = list(map(lambda x:(5/9) * (x - 32), Ftemp))



## Referências Consultadas

* [Programação Funcional em Python](https://acervolima.com/programacao-funcional-em-python/)
* [Função Lambda](https://acervolima.com/funcoes-python-lambda/)
* [Função Filter](https://acervolima.com/filter-em-python/)
* [Função Map](https://www.geeksforgeeks.org/python-map-function/)
