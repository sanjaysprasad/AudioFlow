# 🌐 Free Ways to Make AudioFlow Public (Mobile & PC)

Here are the best **100% free** methods to share your website with anyone on mobile or desktop:

---

## Method 1: Instant Free Public URL from your Mac (Zero Sign-up)

If you have the server running locally on your Mac (`python3 -m uvicorn server:app --host 0.0.0.0 --port 8000`), you can turn it into an instant public HTTPS link using **Pinggy**:

1. Start your web server in one terminal:
   ```bash
   cd "/Users/ssp/Documents/SSP CODES/Yt to MP3/web"
   ./run_web.command
   ```
2. Open a second terminal window and run:
   ```bash
   ssh -p 443 -R0:localhost:8000 a.pinggy.io
   ```
3. Pinggy will output a live HTTPS URL (e.g. `https://xxxx.a.pinggy.link`).
4. **Open that link on your phone** or send it to anyone in the world!

---

## Method 2: Permanent 24/7 Free Hosting on Hugging Face Spaces (Recommended)

Hugging Face provides **free 24/7 Docker hosting** (2 vCPU, 16 GB RAM) with pre-configured HTTPS and zero monthly fees.

### Steps:
1. Go to [huggingface.co](https://huggingface.co) and sign up for a free account.
2. Click **New Space** (or go to `huggingface.co/new-space`).
3. Set:
   - **Space Name**: `audioflow`
   - **License**: `MIT`
   - **Space SDK**: Select **Docker** (Blank)
   - **Space Hardware**: Free (CPU basic - 2 vCPU · 16 GB)
4. Upload the following 3 files from this `web/` folder to the repository:
   - `Dockerfile`
   - `requirements.txt`
   - `server.py`
5. Click **Commit Changes**.
6. Hugging Face will automatically build the container and provide your permanent public URL (e.g., `https://yourusername-audioflow.hf.space`).

---

## Method 3: Free Deployment on Render

1. Push this folder to a GitHub repository.
2. Go to [render.com](https://render.com) and create a free account.
3. Click **New** -> **Web Service** -> Connect your GitHub repo.
4. Select **Docker** as the environment.
5. Choose the **Free** instance type.
6. Click **Deploy**. Your app will be live on `https://audioflow.onrender.com`.

---

## Method 4: Test on Mobile over Local Wi-Fi (No Internet Sharing)

If your phone and your Mac are connected to the same Wi-Fi network:
1. Run `./run_web.command`.
2. Check your Mac's local IP address (e.g. `192.0.0.2` or run `ipconfig getifaddr en0`).
3. On your phone's browser (Safari or Chrome), open:
   ```
   http://<YOUR_MAC_IP>:8000
   ```
