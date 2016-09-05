
function destroyer(arr) {
  // Remove all the values
  var des = [];
  for (var i = 1; i < arguments.length; i++) {
    des.push(arguments[i]);
  }
  arr = arr.filter(function(val) {
    var flag = 0;
    for (var i = 0; i < des.length; i++){
      if (val === des[i]) {
        flag = 1;
      }
    }
    if (flag === 0)
      return val;
  });
  return arr;
}

destroyer([1, 2, 3, 1, 2, 3], 2, 3);
