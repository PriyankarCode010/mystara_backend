const express = require('express');
const { scrapeGFG } = require('../utils/pythonRunner');

const router = express.Router();

// GFG health check
router.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    service: 'gfg',
    timestamp: new Date().toISOString()
  });
});

// Get GFG data
router.get('/:username', async (req, res) => {
  try {
    const { username } = req.params;
    const { url } = req.query;
    
    console.log(`Fetching GFG data for user: ${username}`);
    
    const result = await scrapeGFG(username, url);
    
    res.json({
      success: true,
      data: result,
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('GFG scraper error:', error);
    
    res.status(500).json({
      success: false,
      error: 'Failed to fetch GFG data',
      message: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

module.exports = router;
