// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { ITournament } from './tournament.model';

// Define the Referee schema
export interface IReferee extends Document {
  tournament: Types.ObjectId | ITournament; // Assuming tournament is a reference to the Tournament model
  name: string;
}

const refereeSchema = new Schema<IReferee>({
  tournament: {
    type: Types.ObjectId,
    ref: 'Tournament', // Referencing the Tournament model
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
});

// Create and export the Referee model
const Referee = model<IReferee>('Referee', refereeSchema);
export default Referee;
