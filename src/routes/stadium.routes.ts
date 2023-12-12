// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Stadium from '../models/stadium.model';

// Create a router instance
const stadiumRouter = express.Router();

stadiumRouter.use('/', jsonCRUD(Stadium))

// Export the router
export default stadiumRouter;
