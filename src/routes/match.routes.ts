// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Match from '../models/match.model';

// Create a router instance
const matchRouter = express.Router();

matchRouter.use('/', jsonCRUD(Match))

// Export the router
export default matchRouter;
