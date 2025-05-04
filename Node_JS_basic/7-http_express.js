const express = require('express');
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1); // Remove header
    let output = '';
    output += `Number of students: ${students.length}\n`;
    const fields = {};
    for (const student of students) {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }
    for (const [field, names] of Object.entries(fields)) {
      output += `Number of students in ${field}: ${
        names.length
      }. List: ${names.join(', ')}`;
      if (Object.keys(fields).indexOf(field) < Object.keys(fields).length - 1) {
        output += '\n';
      }
    }
    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
const app = express();
const port = 1245;
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  let output = 'This is the list of our students\n';
  try {
    const data = await countStudents(process.argv[2]);
    output += data;
    res.send(output);
  } catch (error) {
    output += error.message;
    res.send(output);
  }
});
app.listen(port);

module.exports = app;
