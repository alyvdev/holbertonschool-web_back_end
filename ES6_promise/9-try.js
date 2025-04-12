/**
 * Executes a math function and returns an array containing the result or error,
 * followed by a processing message.
 * @param {Function} mathFunction - The function to execute.
 * @returns {Array} An array containing the result/error and a message.
 */
export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
