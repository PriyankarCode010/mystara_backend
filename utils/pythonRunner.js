const { spawn } = require('child_process');
const path = require('path');

/**
 * Execute a Python script and return the result as JSON
 * @param {string} scriptPath - Path to the Python script
 * @param {Array} args - Arguments to pass to the Python script
 * @returns {Promise<Object>} - Parsed JSON result from Python script
 */
function executePythonScript(scriptPath, args = []) {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python', [scriptPath, ...args], {
      cwd: process.cwd(),
      stdio: ['pipe', 'pipe', 'pipe']
    });

    let stdout = '';
    let stderr = '';

    pythonProcess.stdout.on('data', (data) => {
      stdout += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      stderr += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        console.error(`Python script error (exit code ${code}):`, stderr);
        reject(new Error(`Python script failed with exit code ${code}: ${stderr}`));
        return;
      }

      try {
        // Try to parse the output as JSON
        const result = JSON.parse(stdout.trim());
        resolve(result);
      } catch (parseError) {
        console.error('Failed to parse Python output as JSON:', stdout);
        reject(new Error(`Failed to parse Python output: ${parseError.message}`));
      }
    });

    pythonProcess.on('error', (error) => {
      console.error('Failed to start Python process:', error);
      reject(new Error(`Failed to start Python process: ${error.message}`));
    });

    // Set a timeout to prevent hanging
    setTimeout(() => {
      pythonProcess.kill();
      reject(new Error('Python script timeout'));
    }, 30000); // 30 second timeout
  });
}

/**
 * Execute LeetCode scraper
 * @param {string} username - LeetCode username
 * @param {string} url - Optional custom URL
 * @returns {Promise<Object>} - Scraped data
 */
async function scrapeLeetCode(username, url = null) {
  const scriptPath = path.join(__dirname, 'leetcode_scraper.py');
  const args = url ? [username, url] : [username];
  return executePythonScript(scriptPath, args);
}

/**
 * Execute GitHub scraper
 * @param {string} username - GitHub username
 * @param {string} url - Optional custom URL
 * @returns {Promise<Object>} - Scraped data
 */
async function scrapeGitHub(username, url = null) {
  const scriptPath = path.join(__dirname, 'github_scraper.py');
  const args = url ? [username, url] : [username];
  return executePythonScript(scriptPath, args);
}

/**
 * Execute GFG scraper
 * @param {string} username - GFG username
 * @param {string} url - Optional custom URL
 * @returns {Promise<Object>} - Scraped data
 */
async function scrapeGFG(username, url = null) {
  const scriptPath = path.join(__dirname, 'gfg_scraper.py');
  const args = url ? [username, url] : [username];
  return executePythonScript(scriptPath, args);
}

module.exports = {
  executePythonScript,
  scrapeLeetCode,
  scrapeGitHub,
  scrapeGFG
};
