// Your code here.

function isObj(obj)
{
  if (typeof(obj) == "object" && obj != null)
    return (true);
  return (false);
}

function getCountProp(obj)
{
  var count = 0;
  for (i in obj)
  {
    count++;
  }
  return count;
}

function deepEqual(obj1, obj2)
{
  if (isObj(obj1) && isObj(obj2))
  {
    if (getCountProp(obj1) != getCountProp(obj2))
      return false;
    for (prop in obj1)
    {
      if (obj2.hasOwnProperty(prop))
      {
        return deepEqual(obj1[prop],obj2[prop]);
      }
      else
        return false;
    }
  }
  else
    return (obj1 === obj2);
}

var obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
// → true
console.log(deepEqual(obj, {here: 1, object: 2}));
// → false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
// → true
