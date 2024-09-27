function multiply(multiplier,... args){
  return args.map((x) => multiplier * x);
}

const arr1= multiply(2,1,2,3);
console.log(arr1);

const arr2= multiply(3,4,2,3);
console.log(arr2);