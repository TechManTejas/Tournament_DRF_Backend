// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IMatch } from './match.model';
import { IPlayer } from './player.model';

// Define the Substitute schema
interface ISubstitute extends Document {
  match: Types.ObjectId | IMatch; // Assuming match is a reference to the Match model
  player_in: Types.ObjectId | IPlayer; // Assuming match_player_in is a reference to the Player model
  player_out: Types.ObjectId | IPlayer; // Assuming match_player_out is a reference to the Player model
  minute: number;
  created_at: Date;
}

const substituteSchema = new Schema<ISubstitute>({
  match: {
    type: Types.ObjectId,
    ref: 'Match', // Referencing the Match model
    required: true,
  },
  player_in: {
    type: Types.ObjectId,
    ref: 'Player', // Referencing the Player model
    required: true,
  },
  player_out: {
    type: Types.ObjectId,
    ref: 'Player', // Referencing the Player model
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

// Create and export the Substitute model
const Substitute = model<ISubstitute>('Substitute', substituteSchema);
export default Substitute;
