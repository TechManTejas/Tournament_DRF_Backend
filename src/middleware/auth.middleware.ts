// Import necessary libraries and modules
import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';

// Middleware for token authentication
export const authenticateToken = (req: Request, res: Response, next: NextFunction): void => {
  // Extract the token from the request headers
  const token = req.header('Authorization');

  // Check if the token is present
  if (!token) {
    res.status(401).json({ message: 'Unauthorized - Token not provided' });
    return;
  }

  // Verify the token
  jwt.verify(token, process.env.JWT_SECRET_KEY || 'your-secret-key', (err, decoded) => {
    if (err) {
      res.status(401).json({ message: 'Unauthorized - Invalid token' });
      return;
    }

    // Attach the user ID to the request for further processing
    // (you can attach more user information if needed)
    (req as any).userId = (decoded as any).userId;

    // Continue to the next middleware or route handler
    next();
  });
};
