import 'dotenv/config';
import cors from 'cors';
import express from 'express';
import http from "http";


const app = express();

app.use(cors({
  origin: '*',
}));

const PORT = 5000;


app.use(express.json());

// Create an HTTP server
const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT} with SSL`);
});