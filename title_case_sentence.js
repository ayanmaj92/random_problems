
function titleCase(str) {
  var arr = str.split(" ");
  var str1 = "";
  for (var i = 0; i < arr.length; i++) {
    var s = arr[i][0].toUpperCase() + arr[i].slice(1).toLowerCase();
    str1 += s + " ";
  }
  return str1.slice(0,str1.length-1);
}

titleCase("I'm a little tea pot");
