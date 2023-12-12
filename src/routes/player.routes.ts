// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Player from '../models/player.model';

// Create a router instance
const playerRouter = express.Router();

playerRouter.use('/', jsonCRUD(Player))

// Export the router
export default playerRouter;
