const express = require('express');
const { scrapeGitHub } = require('../utils/pythonRunner');

const router = express.Router();

// GitHub health check
router.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    service: 'github',
    timestamp: new Date().toISOString()
  });
});

// Get GitHub data
router.get('/:username', async (req, res) => {
  try {
    const { username } = req.params;
    const { url } = req.query;
    
    console.log(`Fetching GitHub data for user: ${username}`);
    
    const result = await scrapeGitHub(username, url);
    
    res.json({
      success: true,
      data: result,
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('GitHub scraper error:', error);
    
    res.status(500).json({
      success: false,
      error: 'Failed to fetch GitHub data',
      message: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

module.exports = router;
