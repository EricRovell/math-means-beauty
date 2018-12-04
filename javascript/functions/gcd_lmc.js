// returns the greatest common divisor for given numbers
function gcd() {
  numbers = Array.prototype.slice.call(arguments);

  function euclid_gcd(a, b) {
    while (b) {
      let temp = a;
      a = b;
      b = temp % b;
    }
    return a;
  }

  return numbers.reduce(euclid_gcd, numbers[0]);
}

// returns the least common multiple for given numbers
function lcm() {
  numbers = Array.prototype.slice.call(arguments);
  return numbers.reduce( (a, b) => a * b / gcd(a, b), numbers[0] )
}