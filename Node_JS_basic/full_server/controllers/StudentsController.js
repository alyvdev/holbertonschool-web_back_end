import readDatabase from '../utils';

/**
 * Students controller class
 */
class StudentsController {
  /**
   * Get all students handler
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static getAllStudents(request, response) {
    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((fields) => {
        let responseText = 'This is the list of our students\n';

        // Sort fields alphabetically (case insensitive)
        // eslint-disable-next-line max-len
        const sortedFields = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        for (const field of sortedFields) {
          const students = fields[field];
          responseText += `Number of students in ${field}: ${
            students.length
          }. List: ${students.join(', ')}\n`;
        }

        // Remove the last newline character
        responseText = responseText.slice(0, -1);

        response.status(200).send(responseText);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }

  /**
   * Get students by major handler
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static getAllStudentsByMajor(request, response) {
    const databasePath = process.argv[2];
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(databasePath)
      .then((fields) => {
        if (!fields[major]) {
          response.status(500).send(`No students found for major ${major}`);
          return;
        }

        const students = fields[major];
        response.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }
}

export default StudentsController;
