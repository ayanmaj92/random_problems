
function rot13(str) { // LBH QVQ VG!
  var str1 = "";
  for (var i = 0; i < str.length; i++) {
    var j = str.charCodeAt(i);
    if (j < 65 || j > 90) {
      str1 += str[i];
    }
    else {
      j -= 13;
      if (j < 65){
        //if below 65, we need to wrap around so add 26...
        j += 26;
      }
      str1 += String.fromCharCode(j);
    }
  }
  return str1;
}

// Change the inputs below to test
rot13("SERR CVMMN!");
