// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Goal from '../models/goal.model';

// Create a router instance
const goalRouter = express.Router();

goalRouter.use('/', jsonCRUD(Goal))

// Export the router
export default goalRouter;
