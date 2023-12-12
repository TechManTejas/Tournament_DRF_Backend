// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Substitute from '../models/substitute.model';

// Create a router instance
const substituteRouter = express.Router();

substituteRouter.use('/', jsonCRUD(Substitute))

// Export the router
export default substituteRouter;
