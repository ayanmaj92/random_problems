function average(array) {
  function plus(a, b) { return a + b; }
  return array.reduce(plus) / array.length;
}

var byName = {};
ancestry.forEach(function(person) {
  byName[person.name] = person;
});

// Your code here.
function hasKnownMother(person) {
  if (byName.hasOwnProperty(person["mother"]))
    return true;
  return false;
}
var filt_anc = ancestry.filter(hasKnownMother);
var arr = filt_anc.map(function(p) {
  return Math.abs(p["born"]-byName[p["mother"]]["born"]);
});
console.log(average(arr));
//console.log(filt_anc.length);
// → 31.2
