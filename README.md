
# Transcriber

Transcriber is a Python script designed to download audio from a YouTube video and transcribe it using the Whisper ASR model by OpenAI. This guide will help you set up and run the script on an Ubuntu server, specifically for a DigitalOcean droplet.

## Features

- Downloads audio from YouTube videos.
- Transcribes the audio using Whisper ASR.
- Supports various model sizes for transcription.

## Prerequisites

- Ubuntu server (e.g., DigitalOcean droplet).
- Python 3.
- Sufficient resources (CPU, memory, storage) for handling transcription.

## Setup Instructions

### Step 1: Update and Upgrade the Server

Update your package lists and upgrade existing packages:

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Required Packages

Install `ffmpeg` for handling audio and `pip` for Python package management:

```bash
sudo apt install ffmpeg python3-pip -y
```

### Step 3: Install Python Dependencies

Install the necessary Python libraries:

```bash
pip3 install pytube openai-whisper
```

### Step 4: Download the Transcriber Script

Download the `transcriber.py` script to your server:

```bash
wget https://your-link-to-transcriber.py -O transcriber.py
```

### Step 5: Run the Transcriber Script

Execute the script with the required YouTube URL and model size:

```bash
python3 transcriber.py <YouTube_URL> <model_size>
```

Replace `<YouTube_URL>` with the URL of the YouTube video you want to transcribe, and `<model_size>` with one of the supported Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`).

## Example Usage

```bash
python3 transcriber.py https://www.youtube.com/watch?v=example tiny
```

This command will download the audio from the provided YouTube video and transcribe it using the `tiny` model.

## Notes

- Ensure you have sufficient permissions to run the script and access the required resources.
- The transcription process may take some time depending on the length of the video and the chosen model size.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License.

