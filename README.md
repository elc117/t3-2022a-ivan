# Programação funcional em Python: 
## Aluno: Ivan Maidana da Silveira

## Motivação
No decorrer da disciplina foi abordado programação funcional, com a linguagem haskell que aceita apenas o paradigma funcional, mas neste trabalho eu irei usar programação funcional na linguagem python, eu escolhi este tema para o meu trabalho pois acredito, que as facilitações da programação funcional serão muito úteis, sendo usadas em uma linguagem que aceita multiparadigmas. 

## Funções Anônimas (lambda)
Em Python, uma função anônima significa que uma função não tem nome. Como já sabemos, a palavra-chave def é usada para definir uma função normal em Python.
Da mesma forma, a palavra-chave lambda é usada para definir uma função anônima em Python, elas são da mesma forma que as funções lambda em haskell.

Sintaxe: argumentos lambda: expressão<br>
Ex: Comparando uma função normal em python, com uma função anônima que faz a mesma coisa:<br>

        def cube(y):                    versus                        lambda_cube = lambda y: y*y*y 
          return y*y*y 
  
        


## Filter:
A função filter() como diz o nome, ela filtra uma lista dada, com a ajuda de uma função que testa cada elemento na sequência para ser verdadeiro ou não.
Com a lista resultante sendo apenas com os elementos verdadeiros.

Sintaxe: filter (função, sequência)<br>
Ex: Onde queremos que sejam mantidos apenas os elementos pares desta lista.<br>

        lista1 = [1, 4, 9, 16, 2]
        list(filter(lamdba x: x % 2 == 0, lista1))  
        
Resposta = [4, 16, 2]


## Map:
A função map() em Python recebe uma função e uma lista como argumentos. Cada elemento da lista é aplicada na função, e uma nova 
lista é retornada. Contendo toda a lista modificada pela função.

Sintaxe: map(função, sequência)<br>
Ex: Onde temos uma lista de graus em celsius e queremos transformar em fahrenheits.<br>

        temp = [0, 22.5, 40, 100]
        F_temp = list(map(lambda x:(9/5) * (x + 32), temp))

Resposta = [32.0, 72.5, 104.0, 212.0]

## Zip:
A função zip() recebe N listas e retorna uma lista de tupla, onde a tamanho da menor lista recebida, define o tamanho da nossa lista de tupla resultante.

Sintaxe: zip(listaA, listaB, ...)<br>
Ex: A função zip receberá 2 listas e retornará uma lista de tupla.<br>
        
        x = [1, 2, 3]
        y = [4, 5, 6, 7, 8]
        list(Zip(x, y))
        
Resposta:[(1, 4), (2, 5), (3, 6)]

## Reduce
A função reduce() recebe como parâmetros uma função que recebe dois argumentos e retorna apenas um e também uma lista, a função reduce irá aplicar os elementos da lista na função até que reste apenas um valor como resultado.

sintaxe: reduce(função, lista)<br>
Ex: Teremos um lista e descobriremos o seu somatório.<br>

        lista = [47, 11, 42, 13]
        reduce(lambda x, y: x+y, lista)
Resposta: 113

## List Comprehension
A função List Comprehension é uma construção que equivale a notação matemática do tipo:

S = {x^2 ∀ x em ℕ, x>=20}
Ou seja, S é o conjunto formado por x ao quadrado para todo x no conjunto dos naturais, se x for maior ou igual a 20 por exemplo.

Sintaxe: lista = [ <expressão> for <referência> in <sequência> if <condição> ]<br>
Ex: Todos os números ímpares serão elevados ao quadrado.<br>

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        print([ x**2 for x in nums if x % 2 ])
Resposta[1, 9, 25, 49, 81, 121]<br>
List Comprehension é mais eficiente do que usar as funções map() e filter() em relação a processamento e consumo de memória.


## Referências Consultadas


* [Programação Funcional em Python](https://acervolima.com/programacao-funcional-em-python/)
* [Programação Funcional em Python1](https://www.codigofluente.com.br/aula-18-programacao-funcional-em-python/)
* [Programação Funcional em Python2](https://docs.python.org/pt-br/3/howto/functional.html)
* [Função Lambda](https://acervolima.com/funcoes-python-lambda/)
* [Função Filter](https://acervolima.com/filter-em-python/)
* [Função Map](https://www.geeksforgeeks.org/python-map-function/)
