// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IClub } from './club.model';
import { IMedia } from './media.model';

// Define the Stadium schema
export interface IStadium extends Document {
  club: Types.ObjectId | IClub; // Assuming club is a reference to the Club model
  image: Types.ObjectId | IMedia; // Assuming image is a reference to the Media model
  name: string;
  address: string;
}

const stadiumSchema = new Schema<IStadium>({
  club: {
    type: Types.ObjectId,
    ref: 'Club', // Referencing the Club model
    required: true,
  },
  image: {
    type: Types.ObjectId,
    ref: 'Media', // Referencing the Media model
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  address: {
    type: String,
    required: true,
  },
});

// Create and export the Stadium model
const Stadium = model<IStadium>('Stadium', stadiumSchema);
export default Stadium;
