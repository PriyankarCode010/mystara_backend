const express = require('express');
const { scrapeLeetCode } = require('../utils/pythonRunner');

const router = express.Router();

// LeetCode health check
router.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    service: 'leetcode',
    timestamp: new Date().toISOString()
  });
});

// Get LeetCode data
router.get('/:username', async (req, res) => {
  try {
    const { username } = req.params;
    const { url } = req.query;
    
    console.log(`Fetching LeetCode data for user: ${username}`);
    
    const result = await scrapeLeetCode(username, url);
    
    res.json({
      success: true,
      data: result,
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('LeetCode scraper error:', error);
    
    res.status(500).json({
      success: false,
      error: 'Failed to fetch LeetCode data',
      message: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

module.exports = router;
