// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IMedia } from './media.model';

// Define the Club schema
export interface IClub extends Document {
  name: string;
  logo: Types.ObjectId | IMedia; // Assuming logo is a reference to the Media model
  address: string;
}

const clubSchema = new Schema<IClub>({
  name: {
    type: String,
    required: true,
  },
  logo: {
    type: Types.ObjectId,
    ref: 'Media', // Referencing the Media model
    required: true,
  },
  address: {
    type: String,
    required: true,
  },
});

// Create and export the Club model
const Club = model<IClub>('Club', clubSchema);
export default Club;
