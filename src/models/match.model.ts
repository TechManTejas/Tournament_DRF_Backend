// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { ITeam } from './team.model';
import { ITournament } from './tournament.model';
import { IReferee } from './referee.model';
import { IStadium } from './stadium.model';

// Define the Match schema
export interface IMatch extends Document {
  teamA: Types.ObjectId | ITeam; // Assuming teamA is a reference to the Team model
  teamB: Types.ObjectId | ITeam; // Assuming teamB is a reference to the Team model
  tournament: Types.ObjectId | ITournament; // Assuming tournament is a reference to the Tournament model
  referee_head: Types.ObjectId | IReferee; // Assuming referee_head is a reference to the Referee model
  referee_assistant: Types.ObjectId | IReferee; // Assuming referee_assistant is a reference to the Referee model
  referee_assistant_2: Types.ObjectId | IReferee; // Assuming referee_assistant_2 is a reference to the Referee model
  referee_fourth: Types.ObjectId | IReferee; // Assuming referee_fourth is a reference to the Referee model
  stadium: Types.ObjectId | IStadium; // Assuming stadium is a reference to the Stadium model
  datetime: Date;
  status: string;
  start_time: string;
  timer: boolean;
  end_time: Date;
}

const matchSchema = new Schema<IMatch>({
  teamA: {
    type: Types.ObjectId,
    ref: 'Team', // Referencing the Team model
    required: true,
  },
  teamB: {
    type: Types.ObjectId,
    ref: 'Team', // Referencing the Team model
    required: true,
  },
  tournament: {
    type: Types.ObjectId,
    ref: 'Tournament', // Referencing the Tournament model
    required: true,
  },
  referee_head: {
    type: Types.ObjectId,
    ref: 'Referee', // Referencing the Referee model
    required: true,
  },
  referee_assistant: {
    type: Types.ObjectId,
    ref: 'Referee', // Referencing the Referee model
    required: true,
  },
  referee_assistant_2: {
    type: Types.ObjectId,
    ref: 'Referee', // Referencing the Referee model
    required: true,
  },
  referee_fourth: {
    type: Types.ObjectId,
    ref: 'Referee', // Referencing the Referee model
    required: true,
  },
  stadium: {
    type: Types.ObjectId,
    ref: 'Stadium', // Referencing the Stadium model
    required: true,
  },
  datetime: {
    type: Date,
    required: true,
  },
  status: {
    type: String,
    required: true,
  },
  start_time: {
    type: String,
    required: true,
  },
  timer: {
    type: Boolean,
    required: true,
  },
  end_time: {
    type: Date,
    required: true,
  },
});

// Create and export the Match model
const Match = model<IMatch>('Match', matchSchema);
export default Match;
