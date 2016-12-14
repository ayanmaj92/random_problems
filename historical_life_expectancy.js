function average(array) {
  function plus(a, b) { return a + b; }
  return array.reduce(plus) / array.length;
}

// Your code here.
cents = {};
for (var i=0;i<ancestry.length;i++)
{
  var century = Math.ceil(ancestry[i].died / 100);
  if (cents.hasOwnProperty(century))
  {
    // century has to be in brackets in order for it to be evaluated and then added.
    // Otherwise cents will get a property called century, not the individual ones.
    cents[century].push(ancestry[i].died - ancestry[i].born);
  }
  else
    cents[century] = [ancestry[i].died - ancestry[i].born];
}
//console.log(cents);
for (i in cents)
{
  console.log(i+": "+average(cents[i]).toFixed(1));
}

// → 16: 43.5
//   17: 51.2
//   18: 52.8
//   19: 54.8
//   20: 84.7
//   21: 94
