function isPrime(number) {
  return !('1'.repeat(number).match(/^1?$|^(11+?)\1+$/))
}

console.log(isPrime(239))