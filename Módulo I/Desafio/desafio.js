/*
1- Nome do funcionario com MAIOR SALARIO da empresa
2- Nome do funcionario com MENOR SALARIO da empresa
3- MEDIA da empresa
4- Recebe um SETOR como parâmetro e retorna o funcionário de MAIOR salário do setor informado
5- Recebe um setor como parâmetro e retorna o funcionário de MENOR salário do setor informado
6- Recebe um setor como parâmetro e retorna a MEDIA salarial do setor informado.
*/
var fs = require('fs');
// const { Console } = require("console");
var readLine = require('readline');

var func = require('./funcionarios.json');

function maiorSalario() {
  let maiorSalario = 0;
  let funcionario = '';
  for (let i = 0; i < func.funcionarios.length; i++) {
    if (func.funcionarios[i].salario > maiorSalario) {
      maiorSalario = func.funcionarios[i].salario;
      funcionario = func.funcionarios[i].nome;
    }
  }

  console.log(
    'O funcionario com MAIOR salario na empresa é ' +
      funcionario +
      ', com um salario de R$' +
      maiorSalario
  );
}

function menorSalario() {
  let menorSalario = 100000000;
  let funcionario = '';
  for (let i = 0; i < func.funcionarios.length; i++) {
    if (func.funcionarios[i].salario < menorSalario) {
      menorSalario = func.funcionarios[i].salario;
      funcionario = func.funcionarios[i].nome;
    }
  }

  console.log(
    'O funcionario com MENOR salario na empresa é ' +
      funcionario +
      ', com um salario de R$' +
      menorSalario
  );
}

function MEDIA() {
  let media = 0;
  let soma = 0;
  for (let i = 0; i < func.funcionarios.length; i++) {
    soma += func.funcionarios[i].salario;
  }
  media = soma / func.funcionarios.length;

  console.log('A média salarial da empresa é R$' + media);
}

function maiorSETOR() {
  let maiorSalario = 0;
  let funcionario = '';
  let setor = 'Comercial';
  for (let i = 0; i < func.funcionarios.length; i++) {
    if (func.funcionarios[i].setor == setor) {
      if (func.funcionarios[i].salario > maiorSalario) {
        maiorSalario = func.funcionarios[i].salario;
        funcionario = func.funcionarios[i].nome;
      }
    }
  }

  console.log(
    'O funcionario com MAIOR salario no setor ' +
      setor +
      ' é ' +
      funcionario +
      ', com um salario de R$' +
      maiorSalario
  );
}

function menorSETOR() {
  let menorSalario = func.funcionarios[0].salario;
  let funcionario = '';
  let setor = 'Comercial';
  for (let i = 0; i < func.funcionarios.length; i++) {
    if (func.funcionarios[i].setor == setor) {
      if (func.funcionarios[i].salario < menorSalario) {
        menorSalario = func.funcionarios[i].salario;
        funcionario = func.funcionarios[i].nome;
      }
    }
  }

  console.log(
    'O funcionario com MENOR salario no setor ' +
      setor +
      ' é ' +
      funcionario +
      ', com um salario de R$' +
      menorSalario
  );
}

function mediaSETOR() {
  let media = 0;
  let soma = 0;
  let count = 0;
  let setor = 'Comercial';
  for (let i = 0; i < func.funcionarios.length; i++) {
    if (func.funcionarios[i].setor == setor) {
      count += 1;
      soma += func.funcionarios[i].salario;
    }
  }
  media = soma / count;
  console.log('A média salarial no setor ' + setor + ' é R$' + media);
}

maiorSalario();
menorSalario();
MEDIA();
maiorSETOR();
menorSETOR();
mediaSETOR();
