// Import necessary libraries and modules
import { Schema, model, Document } from 'mongoose';

// Define the Media schema
export interface IMedia extends Document {
  name: string;
  logo: string; // Assuming logo is a URL or file path
  type: string;
  category: string;
  verified: boolean;
}

const mediaSchema = new Schema<IMedia>({
  name: {
    type: String,
    required: true,
  },
  logo: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
  category: {
    type: String,
    required: true,
  },
  verified: {
    type: Boolean,
    default: false, // Assuming verified is initially set to false
  },
});

// Create and export the Media model
const Media = model<IMedia>('Media', mediaSchema);
export default Media;
