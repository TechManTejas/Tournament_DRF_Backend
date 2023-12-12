import express, { Router, Request, Response } from 'express';
import multer, { Multer } from 'multer';
import { Document, Model, Query } from 'mongoose';

interface CrudRouterOptions<T extends Document> {
    model: Model<T>;
    uploadFields?: { name: string; maxCount: number }[];
    destination?: string;
    population?: string | string[];
}

const formdataCRUD = <T extends Document>({ model, uploadFields = [], destination = 'uploads', population = [] }: CrudRouterOptions<T>): Router => {
    const router = express.Router();

    // Multer configuration for file uploads
    const storage = multer.diskStorage({
        destination: function (req, file, cb) {
            cb(null, destination); // Specify the destination directory
        },
        filename: function (req, file, cb) {
            const timestamp = Date.now(); // Get the current timestamp in milliseconds
            const extension = file.originalname.split('.').pop(); // Get the file extension
            const newFilename = `${timestamp}_${file.originalname}`; // Combine timestamp and original filename
            cb(null, newFilename); // Use the new filename
        },
    });

    const upload: Multer = multer({ storage: storage });

    // Create
    router.post('/', upload.fields(uploadFields), async (req: Request, res: Response) => {
        try {
            const files = req.files as { [fieldname: string]: Express.Multer.File[] };
            const uploadedFiles: Record<string, string[]> = {};

            uploadFields.forEach((field) => {
                const fieldFiles = files[field.name] || [];
                uploadedFiles[field.name] = fieldFiles.map((file) => `/uploads/${file.originalname}`);
            });

            const newItem = new model({
                // Extract other fields from req.body
                ...uploadedFiles,
                ...req.body,
            });

            const savedItem = await newItem.save();

            res.status(201).json(savedItem);
        } catch (error) {
            console.error(error);
            res.status(500).send('Internal Server Error');
        }
    });

    // Read all
    router.get('/', async (req: Request, res: Response) => {
        try {
            // Pagination
            const page = req.query.page ? parseInt(req.query.page as string, 10) : 1;
            const pageSize = req.query.pageSize ? parseInt(req.query.pageSize as string, 10) : 10;
            const skip = (page - 1) * pageSize;

            // Filter (you can customize this based on your model's properties)
            const filterQuery: any = req.query.filter;
            const filter = filterQuery ? JSON.parse(filterQuery) : {};

            // Search
            const searchQuery = req.query.search as string;
            const searchFilter: Record<string, any> = {};

            if (searchQuery) {
                const modelProperties = Object.keys(model.schema.paths);

                const orArray = modelProperties
                    .filter((property) => {
                        const propertyType = model.schema.paths[property]?.instance;
                        return propertyType === 'String';
                    })
                    .map((property) => {
                        const regexFilter = { [property]: { $regex: new RegExp(searchQuery, 'i') } };
                        return regexFilter;
                    });

                // Add the $or array to the search filter
                searchFilter.$or = orArray;
            }

            // Combine search and filter queries
            const query = { ...filter, ...searchFilter };

            let itemsQuery: Query<T[], T, {}>;

            // Populate specified attributes
            if (population) {
                itemsQuery = model.find(query).populate(population) as Query<T[], T, {}>;
            } else {
                itemsQuery = model.find(query) as Query<T[], T, {}>;
            }

            // Fetch total count without pagination
            const totalCount = await model.countDocuments(query);

            const items = await itemsQuery
                .skip(skip)
                .limit(pageSize);

            res.status(200).json({ [`${model.modelName.toLowerCase()}s`]: items, total: totalCount });
        } catch (error) {
            console.error(error);
            res.status(500).json({ message: 'Internal Server Error' });
        }
    });

    // Read by ID
    router.get('/:id', async (req: Request, res: Response) => {
        try {
            const { id } = req.params;
            const item = await model.findById(id);

            if (!item) {
                res.status(404).json({ message: `${model.modelName} not found` });
                return;
            }

            res.status(200).json({ [model.modelName.toLowerCase()]: item });
        } catch (error) {
            console.error(error);
            res.status(500).json({ message: 'Internal Server Error' });
        }
    });

    // Update by ID
    router.put('/:id', upload.fields(uploadFields), async (req: Request, res: Response) => {
        try {
            const itemId = req.params.id;
            const files = req.files as { [fieldname: string]: Express.Multer.File[] };

            const existingItem = await model.findById(itemId);

            if (!existingItem) {
                return res.status(404).json({ error: `${model.modelName} not found` });
            }

            const updatedItem: Partial<T> = {};

            // Handle file uploads
            uploadFields.forEach(async (field) => {
                const file = files[field.name]?.[0];

                if (file) {
                    // Delete the previous file if it exists and is different from the new file
                    const previousFilePath = existingItem[field.name];
                    if (previousFilePath && previousFilePath !== `/uploads/${file.originalname}`) {
                        const fs = require('fs').promises;
                        try {
                            await fs.unlink(`uploads/${previousFilePath}`);
                            console.log(`Previous file deleted: ${previousFilePath}`);
                        } catch (error) {
                            console.error(`Error deleting previous file: ${error}`);
                        }
                    }

                    // Set the updated file path
                    updatedItem[field.name] = `/uploads/${file.originalname}`;
                } else {
                    // No file change, retain the existing file path
                    updatedItem[field.name] = existingItem[field.name];
                }
            });

            // Merge with other fields from req.body
            Object.assign(updatedItem, req.body);

            const result = await model.findByIdAndUpdate(itemId, updatedItem, { new: true });

            if (!result) {
                return res.status(404).json({ error: `${model.modelName} not found` });
            }

            res.status(200).json(result);
        } catch (error) {
            console.error(error);
            res.status(500).send('Internal Server Error');
        }
    });

    // Delete by ID
    router.delete('/:id', async (req: Request, res: Response) => {
        try {
            const { id } = req.params;
            const deletedItem = await model.findByIdAndDelete(id);

            if (!deletedItem) {
                res.status(404).json({ message: `${model.modelName} not found` });
                return;
            }

            // Delete associated files
            uploadFields.forEach(async (field) => {
                const filePath = deletedItem[field.name];

                if (filePath) {
                    // Delete the file from the server
                    const fs = require('fs').promises;
                    try {
                        await fs.unlink(`uploads/${filePath}`);
                        console.log(`File deleted: ${filePath}`);
                    } catch (error) {
                        console.error(`Error deleting file: ${error}`);
                    }
                }
            });

            res.status(200).json({ message: `${model.modelName} deleted successfully` });
        } catch (error) {
            console.error(error);
            res.status(500).json({ message: 'Internal Server Error' });
        }
    });

    return router;
};

export default formdataCRUD;
