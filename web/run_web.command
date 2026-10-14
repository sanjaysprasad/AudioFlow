#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "========================================="
echo "🎵 AudioFlow Web Server"
echo "========================================="
echo "Local access:    http://localhost:8000"

# Print local LAN IP for mobile access
LOCAL_IP=$(ipconfig getifaddr en0 || ipconfig getifaddr en1 || echo "localhost")
echo "Mobile access:   http://$LOCAL_IP:8000"
echo "========================================="
echo "Press Ctrl+C to stop the server."
echo

python3 -m uvicorn server:app --host 0.0.0.0 --port 8000 --reload
