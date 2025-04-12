/**
 * Divides two numbers.
 * @param {number} numerator - The number to be divided.
 * @param {number} denominator - The number to divide by.
 * @returns {number} The result of the division.
 * @throws {Error} If the denominator is 0.
 */
export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
