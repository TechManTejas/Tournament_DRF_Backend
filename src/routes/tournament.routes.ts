// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Tournament from '../models/tournament.model';

// Create a router instance
const tournamentRouter = express.Router();

tournamentRouter.use('/', jsonCRUD(Tournament))

// Export the router
export default tournamentRouter;
