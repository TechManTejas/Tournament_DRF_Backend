// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Card from '../models/card.model';

// Create a router instance
const cardRouter = express.Router();

cardRouter.use('/', jsonCRUD(Card))

// Export the router
export default cardRouter;
