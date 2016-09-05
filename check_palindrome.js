
function palindrome(str) {
  // Good luck!
  function toLower(match) {
    return match.toLowerCase();
  }
  var re1 = /[A-Z]/g;
  str = str.replace(re1, toLower);
  var re2 = /[^a-zA-Z0-9]/g;
  str = str.replace(re2, "");
  var arr = str.split("");
  arr.reverse();
  var str_rev = arr.join("");
  if (str === str_rev)
    return true;
  else
    return false;
  
  //return true;
}



palindrome("1 eye for of 1 eye.");
