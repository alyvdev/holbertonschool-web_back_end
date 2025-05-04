import fs from 'fs';

/**
 * Reads the database file asynchronously
 * @param {string} path - Path to the database file
 * @returns {Promise<Object>} - Promise resolving
 */
const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1); // Remove header
    const fields = {};

    for (const student of students) {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }

    resolve(fields);
  });
});

export default readDatabase;
