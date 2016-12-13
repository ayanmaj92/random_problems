// Your code here.
function arrayToList(arr)
{
  var list = {};
  var last = null;
  for (var i=arr.length-1; i>=0; i--)
  {
    var temp = {value: arr[i],
                rest: null};
    temp["rest"] = last;
    last = temp;
    list = temp;
  }
  //console.log(list);
  return (list);
}

function listToArray(list)
{
  var arr = [];
  while(list!==null)
  {
    arr.push(list["value"]);
    list = list["rest"];
  }
  return arr;
}

function prepend(val, list)
{
  return ({value: val, rest: list});
}

function nth(list, pos) 
{
  var temp = list;
  while (pos>=1)
  {
    if (temp === null)
      return (undefined);
    temp = temp["rest"];
    pos -= 1;
  }
  return (temp["value"]);
}

console.log(arrayToList([10, 20, 30]));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(listToArray(arrayToList([10, 20, 30])));
// → [10, 20, 30]
console.log(prepend(10, prepend(20, null)));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(nth(arrayToList([10, 20, 30]), 10));
// → 20
