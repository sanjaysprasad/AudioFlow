#!/usr/bin/env python3
"""
SonicFlow Public Launcher
Starts the local FastAPI server and creates an instant, free Cloudflare HTTPS tunnel.
Works on mobile and PC anywhere in the world with zero accounts or configuration.
"""

import os
import re
import sys
import time
import shutil
import signal
import webbrowser
import subprocess
from pathlib import Path

DIR = Path(__file__).resolve().parent


def find_cloudflared():
    p = shutil.which("cloudflared")
    if p:
        return p
    for cand in ["/opt/homebrew/bin/cloudflared", "/usr/local/bin/cloudflared"]:
        if os.path.isfile(cand) and os.access(cand, os.X_OK):
            return cand
    return None


def main():
    print("=" * 60)
    print("🚀 Launching SonicFlow Public Website...")
    print("=" * 60)

    cloudflared_bin = find_cloudflared()
    if not cloudflared_bin:
        print("❌ Error: cloudflared was not found. Please run: brew install cloudflared")
        sys.exit(1)

    # 1. Start the FastAPI Uvicorn Server
    print("Starting backend web server on port 8000...")
    server_cmd = [
        sys.executable, "-m", "uvicorn", "server:app",
        "--host", "127.0.0.1", "--port", "8000"
    ]
    server_proc = subprocess.Popen(
        server_cmd,
        cwd=DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Give server a moment to bind
    time.sleep(1.5)

    # 2. Start Cloudflare Quick Tunnel
    print("Establishing secure Cloudflare HTTPS tunnel...")
    tunnel_cmd = [cloudflared_bin, "tunnel", "--url", "http://127.0.0.1:8000"]
    tunnel_proc = subprocess.Popen(
        tunnel_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True
    )

    public_url = None
    url_pattern = re.compile(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com')

    # Read output to capture the public URL
    start_time = time.time()
    while time.time() - start_time < 30:
        line = tunnel_proc.stdout.readline()
        if not line:
            continue
        match = url_pattern.search(line)
        if match:
            public_url = match.group(0)
            break

    if not public_url:
        print("❌ Failed to retrieve Cloudflare tunnel URL.")
        server_proc.terminate()
        tunnel_proc.terminate()
        sys.exit(1)

    print("\n" + "═" * 65)
    print("🎉 YOUR WEBSITE IS LIVE AND PUBLIC ON THE INTERNET!")
    print("═" * 65)
    print(f"\n👉 PUBLIC LINK (Mobile & PC):\n   {public_url}\n")
    print(f"👉 LOCAL MAC LINK:\n   http://localhost:8000\n")
    print("═" * 65)
    print("📱 Open the link above on your phone (iPhone/Android) or PC!")
    print("Press Ctrl+C anytime to stop the public server.\n")

    # Open in browser
    try:
        webbrowser.open(public_url)
    except Exception:
        pass

    # Handle clean shutdown
    def handle_exit(sig, frame):
        print("\nStopping public tunnel and server...")
        try:
            tunnel_proc.terminate()
            server_proc.terminate()
        except Exception:
            pass
        print("Done. Goodbye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    # Keep script alive
    try:
        tunnel_proc.wait()
    except KeyboardInterrupt:
        handle_exit(None, None)


if __name__ == "__main__":
    main()
