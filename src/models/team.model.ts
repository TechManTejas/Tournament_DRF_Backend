// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IClub } from './club.model';
import { IMedia } from './media.model';

// Define the Team schema
export interface ITeam extends Document {
  club: Types.ObjectId | IClub; // Assuming club is a reference to the Club model
  logo: Types.ObjectId | IMedia; // Assuming logo is a reference to the Media model
  name: string;
  short_name: string;
  category: string;
  deleted: boolean;
  verified: boolean;
}

const teamSchema = new Schema<ITeam>({
  club: {
    type: Types.ObjectId,
    ref: 'Club', // Referencing the Club model
    required: true,
  },
  logo: {
    type: Types.ObjectId,
    ref: 'Media', // Referencing the Media model
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  short_name: {
    type: String,
    required: true,
  },
  category: {
    type: String,
    required: true,
  },
  deleted: {
    type: Boolean,
    default: false, // Assuming deleted is initially set to false
  },
  verified: {
    type: Boolean,
    default: false, // Assuming verified is initially set to false
  },
});

// Create and export the Team model
const Team = model<ITeam>('Team', teamSchema);
export default Team;
