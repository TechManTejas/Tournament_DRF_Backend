// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Club from '../models/club.model';

// Create a router instance
const clubRouter = express.Router();

clubRouter.use('/', jsonCRUD(Club))

// Export the router
export default clubRouter;
