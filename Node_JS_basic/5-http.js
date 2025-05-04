const http = require('http');
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
      }. List: ${names.join(', ')}\n`;
    }

    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const data = await countStudents(process.argv[2]);
      res.end(data);
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});
app.listen(1245);

module.exports = app;
