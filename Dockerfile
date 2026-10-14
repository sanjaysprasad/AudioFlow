FROM python:3.11-slim

# Install system dependencies including ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up non-root user (best practice and required for Hugging Face Spaces)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Install python dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy server code
COPY --chown=user server.py .

# Standard port (7860 for Hugging Face, or Render dynamic $PORT)
EXPOSE 7860

CMD ["sh", "-c", "python3 -m uvicorn server:app --host 0.0.0.0 --port ${PORT:-7860}"]
