// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Referee from '../models/referee.model';

// Create a router instance
const refereeRouter = express.Router();

refereeRouter.use('/', jsonCRUD(Referee))

// Export the router
export default refereeRouter;
