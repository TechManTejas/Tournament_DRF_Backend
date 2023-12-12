import 'dotenv/config';
import cors from 'cors';
import express from 'express';
import mongoose from './db';
import fs from 'fs';
import https from "https"
import http from "http";

// Routes 
// import userRoutes from './routes/userRoutes.routes';
// import contactUsResponsesRoutes from './routes/contactUsResponses.routes';
// import taxiFormRoutes from './routes/taxiForm.routes'; 
// import faqRoutes from './routes/faq.routes';
// import cityRoutes from './routes/city.routes';
// import couponRoutes from './routes/coupon.routes';
// import routeRoutes from './routes/route.routes';
// import taxiTypeRoutes from './routes/taxiType.routes';
// import taxiRoutes from './routes/taxi.routes';
// import driverRoutes from './routes/driver.routes';
// import bookingRoutes from './routes/bookings.routes'
// import settingsRoutes from './routes/settings.routes';

const app = express();

app.use(cors({
  origin: '*',
}));

const PORT = process.env.PORT || 5000;

mongoose.connection.on('error', console.error.bind(console, 'MongoDB connection error:'));

app.use(express.json());
// app.use('/users', userRoutes);
// app.use('/contact-us', contactUsResponsesRoutes);
// app.use('/taxi-forms', taxiFormRoutes);
// app.use('/faqs', faqRoutes);
// app.use('/citys', cityRoutes);
// app.use('/coupons', couponRoutes);
// app.use('/routes', routeRoutes);
// app.use('/taxitypes', taxiTypeRoutes);
// app.use('/taxis', taxiRoutes); 
// app.use('/drivers', driverRoutes); 
// app.use('/bookings', bookingRoutes);
// app.use('/settings', settingsRoutes);

// app.get('/.well-known/pki-validation/39DDA8E16A8150424FC88AD44C09AED0.txt', (req, res) => {
//   // Assuming your text file is named 'example.txt' in the root directory
//   const filePath = '39DDA8E16A8150424FC88AD44C09AED0.txt';

//   fs.readFile(filePath, 'utf8', (err, data) => {
//     if (err) {
//       console.error(err);
//       res.status(500).send('Internal Server Error');
//     } else {
//       res.send(data);
//     }
//   });
// });

// Specify the paths to your SSL certificate and private key
// const privateKey = fs.readFileSync('private.key', 'utf8');
// const certificate = fs.readFileSync('certificate.crt', 'utf8');
// const ca = fs.readFileSync('ca_bundle.crt', 'utf8');

// const credentials = { key: privateKey, cert: certificate, ca: ca };

// Create an HTTPS server
// const server = https.createServer(credentials, app);


// Create an HTTPS server
const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT} with SSL`);
});