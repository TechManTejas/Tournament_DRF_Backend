// Import necessary libraries and modules
import express from 'express';
import { jsonCRUD } from '../utils/json.controller';
import User from '../models/user.model';

// Create a router instance
const userRouter = express.Router();

userRouter.use('/', jsonCRUD(User))

// Export the router
export default userRouter;
