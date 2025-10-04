#!/bin/bash

echo "🚀 Deploying Mystara Backend to Vercel..."

# Install dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Test the server locally
echo "🧪 Testing server locally..."
node server.js &
SERVER_PID=$!

# Wait for server to start
sleep 3

# Test endpoints
echo "🔍 Testing endpoints..."
curl -s http://localhost:3000/health > /dev/null && echo "✅ Health endpoint working"
curl -s http://localhost:3000/github/octocat > /dev/null && echo "✅ GitHub endpoint working"
curl -s http://localhost:3000/leetcode/Priyankar_ > /dev/null && echo "✅ LeetCode endpoint working"

# Stop local server
kill $SERVER_PID

echo "🎉 Local testing completed!"
echo "📤 Ready for deployment to Vercel"
echo "Run: vercel --prod"
