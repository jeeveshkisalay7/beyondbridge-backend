require('dotenv').config();
const express    = require('express');
const cors       = require('cors');
const path       = require('path');

const authRoutes    = require('./routes/auth');
const bookingRoutes = require('./routes/booking');
const webhookRoutes = require('./routes/webhook');

const app  = express();
const PORT = process.env.PORT || 3001;

// ─── MIDDLEWARE ───────────────────────────────────────────
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// Serve frontend build if needed
// app.use(express.static(path.join(__dirname, '../frontend')));

// ─── ROUTES ───────────────────────────────────────────────
app.use('/api/auth',    authRoutes);
app.use('/api/booking', bookingRoutes);
app.use('/api/webhook', webhookRoutes);

// Health check
app.get('/api/health', (req, res) => res.json({ status: 'ok', env: process.env.NODE_ENV }));

// ─── START ────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`🚀 BeyondBridge backend running on http://localhost:${PORT}`);
});
