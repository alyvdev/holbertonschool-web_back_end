import express from 'express';
import routes from './routes';

const app = express();
const port = 1245;

// Use routes
app.use('/', routes);

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

export default app;
