Some exercises in Python language to practice and learn.

"Lista de Exercícios"

1. Faça uma função que recebe por parâmetro um valor inteiro e retorne o valor lógico
Verdadeiro (True) caso o valor seja positivo e Falso (False) caso contrário.

2. Crie uma função que que receba como parâmetro um valor lido do teclado e imprima
para o usuário, a mensagem “O valor {N} informado é positivo” ou a mensagem “O
valor {N} informado é negativo”.

3. Faça uma função que recebe um valor inteiro e retorna uma mensagem que informa
se o valor é par ou ímpar.

4. Faça uma função que recebe as 3 notas de um aluno por parâmetro e uma letra, que
indicará o tipo da média a ser calculada. Caso a letra seja A, a função deve calcular a
média aritmética das notas do aluno, se for P, deve ser calculada a média ponderada
(pesos: 5, 3 e 2 respectivamente). O cálculo da média deve ser retornado pela função.
Na chamada da função, as 3 notas devem ser informadas pelo usuário e as notas
podem ser fracionadas (por exemplo, 7.5 ou 8.5).

5. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias (um
parâmetro para anos, outro para meses e outro para dias) e retorne essa idade em
dias. Considere que um ano tem 360 dias e os meses são de 30 dias.

6. Faça uma função que recebe 3 valores inteiros por parâmetro e retorna-os ordenados
em ordem crescente. Os valores retornados devem estar separados por vírgula (,) e
para serem retornados como uma string, cada valor deve ser convertido para uma
string com o uso da função str(), que recebe por parâmetro um número e retorna
uma string.

7. Faça uma função que recebe por parâmetro o tempo representado em segundos e
retorne esse tempo em horas, minutos e segundos. A hora completa deve ser
retornada em uma variável no seguinte formato “Horas:Minutos:Segundos”, por
exemplo, se for passado por parâmetro 3800 segundos para o método, este deverá
retornar “1:3:20”, que indica, 1 hora, 3 minutos e 20 segundos. ATENÇÃO: Para
formatar a variável de retorno, você precisará converter os valores para string. Para
isso, utilize a função str(), que recebe um número inteiro por parâmetro e o
converte para string.

8. Faça uma função que verifique se um valor é perfeito ou não. Um valor é perfeito
quando ele é igual a soma dos seus divisores, exceto ele próprio. (por exemplo, 6 é
perfeito, pois 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor
booleano: True se é perfeito e False se não for perfeito. Pesquise na internet por
outros números considerados perfeitos e teste sua função.

9. Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e
retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso
ideal = 72.7 x alt - 58 e ,para mulheres, peso ideal = 62.1 x alt - 44.7.

10. Faça uma função que recebe 3 valores reais X, Y e Z e que verifica se esses valores
podem ser os comprimentos dos lados de um triângulo. Caso seja um triângulo, deve
retornar o tipo que triângulo que os lados formam, caso contrário retorna uma
mensagem informando que não é um triângulo.
Obs: Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade
seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma
do comprimento dos outros dois lados.
A função deve identificar o tipo de triângulo formado observando as seguintes
definições:
Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
Triângulo Isósceles: os comprimentos de 2 lados são iguais.
Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.
