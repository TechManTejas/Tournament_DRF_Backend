import 'dotenv/config';
import cors from 'cors';
import express from 'express';
import mongoose from './db';
import http from "http";

// Routes 
import userRoutes from './routes/user.routes';
import cardRouter from './routes/card.routes';
import clubRouter from './routes/club.routes';
import commentRouter from './routes/comment.routes';
import goalRouter from './routes/goal.routes';
import matchRouter from './routes/match.routes';
import mediaRouter from './routes/media.routes';
import playerRouter from './routes/player.routes';
import refereeRouter from './routes/referee.routes';
import stadiumRouter from './routes/stadium.routes';
import substituteRouter from './routes/substitute.routes';
import teamRouter from './routes/team.routes';
import tournamentRouter from './routes/tournament.routes';

const app = express();

app.use(cors({
  origin: '*',
}));

const PORT = process.env.PORT || 5000;

mongoose.connection.on('error', console.error.bind(console, 'MongoDB connection error:'));

app.use(express.json());
app.use('/card', cardRouter);
app.use('/club', clubRouter);
app.use('/comment', commentRouter);
app.use('/goal', goalRouter);
app.use('/match', matchRouter);
app.use('/media', mediaRouter);
app.use('/player', playerRouter);
app.use('/referee', refereeRouter);
app.use('/stadium', stadiumRouter);
app.use('/substitute', substituteRouter);
app.use('/team', teamRouter);
app.use('/tournament', tournamentRouter);
app.use('/user', userRoutes);

// Create an HTTPS server
const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT} with SSL`);
});