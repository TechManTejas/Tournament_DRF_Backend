// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IMatch } from './match.model';
import { IPlayer } from './player.model';

// Define the Goal schema
interface IGoal extends Document {
  match: Types.ObjectId | IMatch; // Assuming match is a reference to the Match model
  player: Types.ObjectId | IPlayer; // Assuming player is a reference to the Player model
  goal_minute: number;
  is_penalty_goal: boolean;
  is_own_goal: boolean;
  created_at: Date;
}

const goalSchema = new Schema<IGoal>({
  match: {
    type: Types.ObjectId,
    ref: 'Match', // Referencing the Match model
    required: true,
  },
  player: {
    type: Types.ObjectId,
    ref: 'Player', // Referencing the Player model
    required: true,
  },
  goal_minute: {
    type: Number,
    required: true,
  },
  is_penalty_goal: {
    type: Boolean,
    required: true,
  },
  is_own_goal: {
    type: Boolean,
    required: true,
  },
  created_at: {
    type: Date,
    required: true,
  },
});

// Create and export the Goal model
const Goal = model<IGoal>('Goal', goalSchema);
export default Goal;
