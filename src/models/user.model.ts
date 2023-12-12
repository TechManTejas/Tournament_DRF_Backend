// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IClub } from './club.model';

// Define the User schema
interface IUser extends Document {
  club: Types.ObjectId | IClub; // Assuming club is a reference to the Club model
  firstname: string;
  lastname: string;
  email: string; // No further extension
  role: string;
}

const userSchema = new Schema<IUser>({
  club: {
    type: Types.ObjectId,
    ref: 'Club', // Referencing the Club model
    required: true,
  },
  firstname: {
    type: String,
    required: true,
  },
  lastname: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    required: true,
  },
});

// Create and export the User model
const User = model<IUser>('User', userSchema);
export default User;
