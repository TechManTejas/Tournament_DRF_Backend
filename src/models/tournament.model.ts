// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IClub } from './club.model';
import { IMedia } from './media.model';

// Define the Tournament schema
export interface ITournament extends Document {
  club: Types.ObjectId | IClub; // Assuming club is a reference to the Club model
  logo: Types.ObjectId | IMedia; // Assuming logo is a reference to the Media model
  name: string;
  alias: string;
  points_draw: number;
  start_time: string;
  start_date: Date;
  no_of_teams: number;
  no_of_groups: number;
  playing_fields: string[];
  playing_time_mins: number;
  pause_between_games_mins: number;
  points_winner: number;
  points_defeat: number;
  timer: boolean;
}

const tournamentSchema = new Schema<ITournament>({
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
  alias: {
    type: String,
    required: true,
  },
  points_draw: {
    type: Number,
    required: true,
  },
  start_time: {
    type: String,
    required: true,
  },
  start_date: {
    type: Date,
    required: true,
  },
  no_of_teams: {
    type: Number,
    required: true,
  },
  no_of_groups: {
    type: Number,
    required: true,
  },
  playing_fields: {
    type: [String],
    required: true,
  },
  playing_time_mins: {
    type: Number,
    required: true,
  },
  pause_between_games_mins: {
    type: Number,
    required: true,
  },
  points_winner: {
    type: Number,
    required: true,
  },
  points_defeat: {
    type: Number,
    required: true,
  },
  timer: {
    type: Boolean,
    required: true,
  },
});

// Create and export the Tournament model
const Tournament = model<ITournament>('Tournament', tournamentSchema);
export default Tournament;
