// returns the decimal fraction from rational representation
function toDecimal(numerator, denominator, limit) {
  let unit = Math.floor(numerator / denominator);
  let decimal = `${unit}.`
  
  // long division
  states = {};
  divident = 10 * (numerator - unit * denominator);

  while (divident > 0 && limit == undefined || limit > 0) {

    previousIndex = states[divident];
    if (previousIndex != undefined) {
      // fraction -> unit.nonPeriodic(period)
      periodStarts = previousIndex;
      nonPeriodic = decimal.slice(0, periodStarts);
      period = decimal.slice(periodStarts, decimal.length);

      return `${nonPeriodic}(${period})`
    }
    states[divident] = decimal.length;

    unit = Math.floor(divident / denominator);
    decimal += unit.toString();
    divident = 10 * (divident - unit * denominator);

    if (limit != undefined) {limit -= 1;}
  }

  return decimal;
}

console.log(toDecimal(2013, 256, 3))