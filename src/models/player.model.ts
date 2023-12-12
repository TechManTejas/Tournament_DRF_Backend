// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { ITeam } from './team.model';

// Define the MatchPlayer schema
interface IPlayer extends Document {
  team: Types.ObjectId | ITeam; // Assuming team is a reference to the Team model
  name: string;
  squad_number: number;
  is_deleted: boolean;
  display_order: number;
  status: 'First Eleven' | 'Substitute';
}

const MatchSchema = new Schema<IPlayer>({
  team: {
    type: Types.ObjectId,
    ref: 'Team', // Referencing the Team model
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  squad_number: {
    type: Number,
    required: true,
  },
  is_deleted: {
    type: Boolean,
    default: false, // Assuming is_deleted is initially set to false
  },
  display_order: {
    type: Number,
    required: true,
  },
  status: {
    type: String,
    enum: ['First Eleven', 'Substitute'],
    required: true,
  },
});

// Create and export the MatchPlayer model
const MatchPlayer = model<IPlayer>('MatchPlayer', MatchSchema);
export default MatchPlayer;
