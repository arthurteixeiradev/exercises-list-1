// Ex1
function trueOrFalse(n) {
    if(n > 0) {
        return true;
    } else {
        return false;
    }
}
// Ex2
function positivoNegativo(n1) {
    if(n1 > 0) {
        return `O valor ${n1} informado é positivo`;
    } else {
        return `O valor ${n1} informado é Negativo`;
    }
}
// Ex3
function parImpar(n2) {
    if(n2 % 2 == 0) {
        return 'Número par';
    } else {
        return 'Número ímpar';
    }
}
// Ex4
function media(letra, nota1, nota2, nota3) {
    if(letra == 'A') {
        let mediaA = (nota1 + nota2 +nota3) / 3;
        let resultado = Math.round(mediaA, 2);
        return `A média aritmética das notas: ${nota1}, ${nota2}, ${nota3} é ${resultado}`;
    } else if(letra == 'P') {
        let mediaP = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10;
        let resultado = Math.round(mediaP, 2);
        return `A média ponderada das notas: ${nota1}, ${nota2}, ${nota3} é ${resultado}`;
    } else {
        console.log('Método inexistente!');
        return;
    }
}
// Ex5
function age(idadeAno, idadeMeses, idadeDias) {
    idadeAno = idadeAno * 360;
    idadeMeses = idadeMeses * 30;
    let resultadoIdade = idadeAno + idadeMeses + idadeDias;
    return resultadoIdade;
}
// Ex6
function retornaOrdemNumeros(num) {
    if(num.length < 2) {
        return num;
    } else {
        let pivo = num[0];
        let i = 1;
        let menorQuePivo = [];
        let maiorQuePivo = [];
        while(i < num.length) {
            if(num[i] <= pivo) {
                menorQuePivo.push(num[i]);
            } else {
                maiorQuePivo.push(num[i]);
            }
            i += 1;
        }
        return retornaOrdemNumeros(menorQuePivo).concat([pivo],retornaOrdemNumeros(maiorQuePivo));
    }
}
// Ex7
function segundosParaTempo(seg) {
    let segRestante = 0;
    let minutos = 0;
    let horas = 0;
    if(seg > 0) {
        segRestante = seg % 60;
        minutos = Math.round(seg / 60);
    }
    if(minutos >0) {
        horas = Math.round(minutos / 60);
        minutos = minutos % 60;
    }
    return `${horas}:${minutos}:${segRestante}`;
}
// Ex8
function validacao(n) {
    let perfectCount = 0;
    let count = n - 1;
    while(count > 0) {
        let restOfDivision = n % count;
        if(restOfDivision == 0) {
            perfectCount += count;
        }
        count -= 1
    }
    return perfectCount == n;
}
// Ex9
function pesoIdeal(alt, sexo) {
    if(sexo == 'masculino') {
        let peso = 72.7 * alt - 58;
        peso = Math.round(peso, 2);
        return peso;
    } else {
        let peso = 62.1 * alt - 44.7;
        peso = Meth.round(peso, 2);
        return peso;
    }
}
// Ex10
function tri(x, y, z) {
    if(x < y + z && y < x + z && y < x + y) {
        console.log('Os valores PODEM formar um triângulo');
        if(x == y && x == z) {
            console.log('É um Triângulo Equilátero!');
            return;
        } else if(x == y && x != z) {
            console.log('É um Triângulo Isósceles');
            return;
        } else {
            console.log('É um Triângulo Escaleno!');
            return;
        }
    } else {
        console.log('Os valores NÃO PODEM formar um triângulo');
        return;
    }
}