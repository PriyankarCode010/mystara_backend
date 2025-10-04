# Mystara Backend - Node.js Server

A Node.js Express server that calls Python scraping scripts for LeetCode, GitHub, and GeeksforGeeks data.

## Architecture

- **Node.js Express Server**: Handles HTTP requests and responses
- **Python Scripts**: Perform the actual web scraping
- **Child Process Communication**: Node.js spawns Python processes and communicates via JSON

## Project Structure

```
mystara_backend/
├── server.js                 # Main Express server
├── package.json              # Node.js dependencies
├── utils/
│   ├── pythonRunner.js       # Python execution utilities
│   ├── leetcode_scraper.py   # LeetCode scraper (Python)
│   ├── github_scraper.py     # GitHub scraper (Python)
│   └── gfg_scraper.py        # GFG scraper (Python)
├── routes/
│   ├── leetcode.js           # LeetCode routes
│   ├── github.js             # GitHub routes
│   └── gfg.js                # GFG routes
└── config/
    └── settings.py           # Python configuration
```

## Installation

1. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

### Development Mode
```bash
npm run dev
```

### Production Mode
```bash
npm start
```

The server will start on `http://localhost:3000`

## API Endpoints

### Health Check
- `GET /health` - Server health status
- `GET /leetcode/health` - LeetCode service health
- `GET /github/health` - GitHub service health
- `GET /gfg/health` - GFG service health

### Data Endpoints
- `GET /leetcode/{username}` - Get LeetCode user data
- `GET /github/{username}` - Get GitHub user data
- `GET /gfg/{username}` - Get GFG user data

### Query Parameters
- `url` - Optional custom URL to scrape

## Example Usage

```bash
# Get LeetCode data
curl http://localhost:3000/leetcode/Priyankar_

# Get GitHub data
curl http://localhost:3000/github/octocat

# Get GFG data
curl http://localhost:3000/gfg/someuser
```

## Response Format

```json
{
  "success": true,
  "data": {
    // Scraped data here
  },
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

## Error Handling

The server includes comprehensive error handling:
- Python script execution errors
- Timeout protection (30 seconds)
- JSON parsing errors
- Network request failures

## Deployment

This Node.js server can be deployed to:
- **Vercel**: Use `vercel.json` configuration
- **Heroku**: Use `Procfile`
- **Railway**: Direct deployment
- **DigitalOcean App Platform**: Direct deployment

## Benefits of This Architecture

1. **Deployment Flexibility**: Node.js servers are easier to deploy than Python servers
2. **Performance**: Node.js handles concurrent requests efficiently
3. **Maintainability**: Clear separation between API layer and scraping logic
4. **Scalability**: Can easily add more Python scrapers
5. **Error Handling**: Better error handling and logging in Node.js

## Troubleshooting

1. **Python not found**: Ensure Python is installed and in PATH
2. **Module not found**: Run `pip install -r requirements.txt`
3. **Permission errors**: Check file permissions for Python scripts
4. **Timeout errors**: Increase timeout in `pythonRunner.js` if needed
