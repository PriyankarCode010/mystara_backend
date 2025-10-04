const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const path = require('path');

// Import route handlers
const leetcodeRoutes = require('./routes/leetcode');
const githubRoutes = require('./routes/github');
const gfgRoutes = require('./routes/gfg');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/leetcode', leetcodeRoutes);
app.use('/github', githubRoutes);
app.use('/gfg', gfgRoutes);

// Root endpoint
app.get('/', (req, res) => {
  res.json({ 
    message: 'Mystara Backend is running 🚀',
    version: '1.0.0',
    endpoints: {
      leetcode: '/leetcode/{username}',
      github: '/github/{username}',
      gfg: '/gfg/{username}'
    }
  });
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).json({
    error: 'Internal Server Error',
    message: err.message,
    timestamp: new Date().toISOString()
  });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    error: 'Not Found',
    message: `Route ${req.originalUrl} not found`,
    timestamp: new Date().toISOString()
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Mystara Backend running on port ${PORT}`);
  console.log(`📊 Health check: http://localhost:${PORT}/health`);
  console.log(`📚 API docs: http://localhost:${PORT}/`);
});

module.exports = app;
