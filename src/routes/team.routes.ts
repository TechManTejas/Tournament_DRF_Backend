// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Team from '../models/team.model';

// Create a router instance
const teamRouter = express.Router();

teamRouter.use('/', jsonCRUD(Team))

// Export the router
export default teamRouter;
