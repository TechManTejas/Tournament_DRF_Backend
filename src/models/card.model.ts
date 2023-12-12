// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IMatch } from './match.model';
import { IPlayer } from './player.model';

// Define the Card schema
interface ICard extends Document {
  match: Types.ObjectId | IMatch; // Assuming match is a reference to the Match model
  player: Types.ObjectId | IPlayer; // Assuming player is a reference to the Player model
  card: 'Yellow' | 'Red' | string; // Possible card types in football
  penalty_time: number;
  minute: number;
  created_at: Date;
}

const cardSchema = new Schema<ICard>({
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
  card: {
    type: String,
    enum: ['Yellow', 'Red', 'Other'], // Add other possible card types as needed
    required: true,
  },
  penalty_time: {
    type: Number,
    required: true,
  },
  minute: {
    type: Number,
    required: true,
  },
  created_at: {
    type: Date,
    required: true,
  },
});

// Create and export the Card model
const Card = model<ICard>('Card', cardSchema);
export default Card;
