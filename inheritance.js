// Your code here.

function Iterator(sequence)
{
  this.sequence = sequence;
  this.end = this.sequence.length;
  this.current = 0;
  this.next = function() {
    if (this.current == this.length)
      return;
    else
    {
      value = this.sequence[this.current];
      this.current++;
      return value;
    }
  };
}

function logFive(seq)
{
  for (var i=0; i<5;i++)
  {
    if (seq.current != seq.end)
      console.log(seq.next());
    else
      return;
  }
}

function ArraySeq(arr)
{
  Iterator.call(this,arr);
}

function RangeSeq(lo,hi)
{
  var arr = [];
  for (var i=lo;i<=hi;i++)
    arr.push(i);
  Iterator.call(this,arr);
}

ArraySeq.prototype = Object.create(Iterator.prototype);
RangeSeq.prototype = Object.create(Iterator.prototype);

logFive(new ArraySeq([1, 2]));
// → 1
// → 2
logFive(new RangeSeq(100, 1000));
// → 100
// → 101
// → 102
// → 103
// → 104
