// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Media from '../models/media.model';

// Create a router instance
const mediaRouter = express.Router();

mediaRouter.use('/', jsonCRUD(Media))

// Export the router
export default mediaRouter;
