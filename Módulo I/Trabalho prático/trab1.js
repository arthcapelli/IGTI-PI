var num = 1000;
var primos = [];
var soma = 0;


for (var i = 0; i <= num; i++){
  count = 0;
  for (var aux = 1; aux <= i; aux++)
    if (i % aux == 0)
      count++;

  if (count == 2)
    primos.push(i);
    
}

for (var i = 0; i < primos.length; i++){
  soma += primos[i]; 
}

console.log(primos);
console.log(soma);