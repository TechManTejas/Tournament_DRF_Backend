// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import Comment from '../models/comment.model';

// Create a router instance
const commentRouter = express.Router();

commentRouter.use('/', jsonCRUD(Comment))

// Export the router
export default commentRouter;
