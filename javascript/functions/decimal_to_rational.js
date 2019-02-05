// '0.02(35)' -> rational representation
function toRational(number) {
  
  if (typeof(decimal) !== 'string') {
    var decimal = number.toString();
  } else {
    var decimal = arguments[0];
  }

  let unit = (decimal[0] === '.') ? 0 : decimal.slice(0, decimal.indexOf('.'));
  
  if (!decimal.includes('(') & !decimal.includes(')')) {
    let mantissa = decimal.slice(decimal.indexOf('.') + 1, decimal.length);
    let numerator = parseInt(mantissa, 10);
    let denominator = 10 ** mantissa.length;

    if (unit != 0) {numerator += unit * denominator}
    return [numerator, denominator];
  }
    
  let nonPeriodic = decimal.slice(decimal.indexOf('.') + 1, decimal.indexOf('('));
  let periodic = decimal.slice(decimal.indexOf('(') + 1, decimal.indexOf(')'));

  if (nonPeriodic === '') {
    var numerator = parseInt(periodic, 10);
  } else {
    var numerator = parseInt(nonPeriodic + periodic, 10) - parseInt(nonPeriodic, 10);
  }
  
  let denominator = parseInt('9'.repeat(periodic.length) + '0'.repeat(nonPeriodic.length), 10);

  if (unit != 0) {numerator += parseInt(unit, 10) * denominator;}
  return [numerator, denominator];
}

console.log(toRational(20.01))