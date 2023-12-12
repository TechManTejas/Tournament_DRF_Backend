// Import necessary libraries and modules
import { Schema, model, Document, Types } from 'mongoose';
import { IMatch } from './match.model';

// Define the Comment schema
interface IComment extends Document {
  match: Types.ObjectId | IMatch; // Assuming match is a reference to the Match model
  comment_minute: number;
  comment: string;
  type: string;
  created_at: Date;
}

const commentSchema = new Schema<IComment>({
  match: {
    type: Types.ObjectId,
    ref: 'Match', // Referencing the Match model
    required: true,
  },
  comment_minute: {
    type: Number,
    required: true,
  },
  comment: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
  created_at: {
    type: Date,
    required: true,
  },
});

// Create and export the Comment model
const Comment = model<IComment>('Comment', commentSchema);
export default Comment;
