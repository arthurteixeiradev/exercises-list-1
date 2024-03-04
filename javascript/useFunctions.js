console.log(
    '1 - Verifica número inteiro e retorna True ou False',
    '\n2 - Verifica se um número é positivo ou negativo',
    '\n3 - Verifica se um número é ímpar ou par',
    '\n4 - Calcula média',
    '\n5 - converte idade em dias',
    '\n6 - Ordena valores em ordem crescente',
    '\n7 - Converte segundos em "horas:minutos:segundos"',
    '\n8 - Verifica se um valor é perfeito',
    '\n9 - Verifica peso ideal',
    '\n10 - Verifica se os valores informados formam um triângulo',
    '\n0 - Sair'
);

menu = prompt('Digite a opção:');
while(menu != 0) {
    if(menu == 1) {
        let n = prompt('Digite um número:');
        console.log('Seu número é:', trueOrFalse(n));
    } else if(menu == 2) {
        let n1 = prompt('Digite algo:');
        console.log(positivoNegativo(n1));
    } else if(menu == 3) {
        let n2 = prompt('Digite um número (Para saber se é par ou ímpar): ');
        console.log(parImpar(n2));
    } else if(menu == 4) {
        let nota1 = parseInt(prompt('Digite sua primeira nota:'));
        let nota2 = parseInt(prompt('Digite sua segunda nota:'));
        let nota3 = parseInt(prompt('Digite sua terceira nota:'));
        let letra = prompt('Média aritmetica (A)\nMédia ponderada (P)\nDigite o método:');
        console.log(media(letra, nota1, nota2, nota3));
    } else if(menu == 5) {
        let idadeAno = prompt('Digite a sua idade:');
        let idadeMeses = prompt('Quantos meses');
        let idadeDias = prompt('Quantos dias');
        console.log('Sua idade em dias é:', age(idadeAno, idadeMeses, idadeDias), 'dias.');
    } else if(menu == 6) {
        let num = [];
        num.push(parseInt(prompt('Digite o primeiro número inteiro:')));
        num.push(parseInt(prompt('Digite o segundo número inteiro:')));
        num.push(parseInt(prompt('Digite o terceiro número inteiro:')));
        let resultado = retornaOrdemNumeros(num);
        console.log(resultado);
    } else if(menu == 7) {
        let segundos = prompt('Segundos:')
        console.log(segundosParaTempo(segundos));
    } else if(menu == 8) {
        let n = prompt('Digite um número perfeito:');
        console.log(validacao(n));
    } else if(menu == 9) {
        let alt = prompt('Digite sua altura:');
        let sexo = prompt('Qual é o seu sexo');
        console.log('Seu peso ideal é:', pesoIdeal(alt, sexo), 'Kg');
    } else if(menu == 10) {
        let x = parseFloat(prompt('Digite o valor do primeiro lado:'));
        let y = parseFloat(prompt('Valor do segundo lado:'));
        let z = parseFloat(prompt('Valor do terceiro lado:'));
        tri(x, y, z);
    }

    menu = prompt('Digite a opção: ')
}
