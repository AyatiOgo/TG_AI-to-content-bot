# 🎥 AI Video-to-Content Telegram Bot

> Transform videos into engaging content with AI-powered transcription and generation

A Telegram bot that converts video content into professional blog posts and social media content. Upload a video or send a link, and get AI-generated content optimized for your platform of choice.

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🌟 Features

- **📹 Video Processing**
  - Upload videos directly to Telegram (up to 20MB)
  - Support for video links from YouTube, TikTok, Instagram, Twitter
  - Automatic audio extraction and conversion

- **🎙️ AI Transcription**
  - Powered by OpenAI Whisper for accurate speech-to-text
  - CloudConvert integration for reliable audio processing
  - Supports multiple languages

- **✍️ Content Generation**
  - Generate engaging blog posts from video content
  - Create short-form social media content
  - Powered by AkashChat API (decentralized AI)
  - Professional Word document output (.docx)

- **⚡ Easy to Use**
  - Simple Telegram commands
  - Real-time processing updates
  - Download documents directly in chat

---

## 📋 Table of Contents

- [Demo](#-demo)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🎬 Demo

### Bot Commands

```
/start - Welcome message and instructions
/help - Show all available commands
```

### Example Workflow

1. **Upload a video** or send a video link
2. **Bot transcribes** the audio using Whisper AI
3. **Choose content type:** Short-form or Blog post
4. **Receive .docx file** with your generated content

---

## 🔧 How It Works

```
┌─────────────┐
│ User Sends  │
│ Video/Link  │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Telegram Bot (bot.py)│
│ - Downloads video    │
│ - Validates file     │
└──────┬──────────────┘
       │
       ▼
┌────────────────────────────┐
│ CloudConvert               │
│ - Converts video to audio  │
│ - Optimizes for Whisper    │
└──────┬─────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Transcriber (transcriber.py)│
│ - Whisper AI transcription  │
│ - Text extraction           │
└──────┬──────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│ Content Generator                │
│ (content_generator.py)           │
│ - AkashChat API                  │
│ - Prompt engineering             │
│ - Content optimization           │
└──────┬───────────────────────────┘
       │
       ▼
┌─────────────────────┐
│ Word Document       │
│ Generation (docx)   │
│ - Professional      │
│   formatting        │
│ - Ready to publish  │
└──────┬──────────────┘
       │
       ▼
┌─────────────┐
│ Send to User│
└─────────────┘
```

---

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- AkashChat API Key (from [chatapi.akash.network](https://chatapi.akash.network))
- CloudConvert API Key (from [cloudconvert.com](https://cloudconvert.com))
- Docker (optional, for deployment)

### Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/telegram-video-bot.git
cd telegram-video-bot
```

2. **Create virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create `.env` file**

```bash
# Create .env file in project root
touch .env
```

Add your API keys:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
AKASH_API_KEY=your_akash_api_key_here
CLOUDCONVERT_API_KEY=your_cloudconvert_api_key_here
```

5. **Run the bot**

```bash
python bot.py
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `TELEGRAM_BOT_TOKEN` | Token from @BotFather | Yes | `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz` |
| `AKASH_API_KEY` | AkashChat API key | Yes | `akml-xxxxxxxxxxxxx` |
| `CLOUDCONVERT_API_KEY` | CloudConvert API key | Yes | `xxxxxxxxxxxxx` |

### Bot Settings

Edit these in `bot.py`:

```python
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB limit for Telegram
WHISPER_MODEL = "base"  # Options: tiny, base, small, medium, large
```

### Supported Video Platforms

- YouTube
- TikTok
- Instagram
- Twitter/X
- Direct video uploads (MP4, MOV, AVI, etc.)

---

## 💡 Usage

### Starting the Bot

1. Open Telegram and search for your bot
2. Send `/start` to begin
3. Follow the interactive prompts

### Creating Content from Video

**Option 1: Upload a video file**
```
1. Click the attachment icon
2. Select video (max 20MB)
3. Send to bot
4. Choose content type
```

**Option 2: Send a video link**
```
1. Copy video URL from YouTube/TikTok/etc
2. Send URL to bot
3. Choose content type
```

### Content Types

**📱 Short-form Content**
- Social media optimized
- Hook + key points + CTA
- 150-300 words
- Perfect for Twitter, LinkedIn, Instagram

**📝 Blog Post**
- SEO-friendly structure
- Introduction, body, conclusion
- 500-1000 words
- Ready for Medium, WordPress, etc.

### Commands

| Command | Description |
|---------|-------------|
| `/start` | Initialize bot and see welcome message |
| `/help` | Display help information |

---

## 🐳 Deployment

Deploy on **Akash Network** - decentralized cloud infrastructure for ~$5/month.

### Deployment Overview

This project uses a fully automated CI/CD pipeline:

```
GitHub Push → GitHub Actions → Docker Hub → Akash Console → Live Bot
```

### Prerequisites

1. **GitHub Account** - For repository and Actions
2. **Docker Hub Account** - For image storage ([hub.docker.com](https://hub.docker.com))
3. **Keplr Wallet** - For Akash Network ([keplr.app](https://www.keplr.app))
4. **AKT Tokens** - ~5-10 AKT for deployment

### Step 1: Set Up GitHub Repository

1. **Fork or clone this repository**

2. **Add GitHub Secrets** (Settings → Secrets and variables → Actions):
   ```
   DOCKER_USERNAME=your_dockerhub_username
   DOCKER_PASSWORD=your_dockerhub_password
   TELEGRAM_BOT_TOKEN=your_telegram_token
   AKASH_API_KEY=your_akash_key
   CLOUDCONVERT_API_KEY=your_cloudconvert_key
   ```

3. **GitHub Actions will automatically:**
   - Build Docker image on every push
   - Run tests
   - Push to Docker Hub with `latest` tag
   - You can then deploy to Akash Console

### Step 2: Automated Docker Build

The `.github/workflows/docker-build.yml` workflow automatically:

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKER_USERNAME }}/telegram-video-bot:latest
```

### Step 3: Deploy to Akash Console

1. **Go to [console.akash.network](https://console.akash.network)**

2. **Connect your Keplr wallet**

3. **Click "Deploy" and paste this SDL:**

```yaml
---
version: "2.0"
services:
  bot:
    image: YOUT_DOCKER_IMAGE
    env:
      - BOT_TOKEN=YOUR_BOT_TOKEN
      - AKASH_API_KEY=YOUR_AKASH_API_KEY
      - >-
        CLOUD_CONVERT_KEY=YOUR_CLOUD_COVERT_KEY
    expose:
      - port: 80
        as: 80
        to:
          - global: true
profiles:
  compute:
    bot:
      resources:
        cpu:
          units: 4
        memory:
          size: 8Gi
        storage:
          - size: 10Gi
  placement:
    dcloud:
      attributes:
        host: akash
      pricing:
        bot:
          denom: ibc/170C677610AC31DF0904FFE09CD3B5C657492170E7E52372E48756B71E56F2F1
          amount: 80000
      signedBy:
        anyOf:
          - akash1365yvmc4s7awdyj3n2sav7xfx76adc6dnmlx63
        allOf: []
deployment:
  bot:
    dcloud:
      profile: bot
      count: 1

```

4. **Replace the placeholders:**
   - `yourusername` → your Docker Hub username
   - `YOUR_TELEGRAM_BOT_TOKEN` → your actual token
   - `YOUR_AKASH_API_KEY` → your actual key
   - `YOUR_CLOUDCONVERT_KEY` → your actual key

5. **Click "Create Deployment"**
   - Review cost estimate
   - Deposit 5 AKT initially
   - Approve in Keplr

6. **Choose a provider**
   - Sort by price
   - Accept the cheapest bid
   - Approve in Keplr

7. **Monitor your deployment**
   - View logs in real-time
   - Check bot status
   - Test with `/start` in Telegram

### Step 4: Update Deployment

When you push code changes to GitHub:

1. **GitHub Actions automatically builds and pushes new image**
2. **In Akash Console:**
   - Go to your deployment
   - Click "Update Deployment"
   - Change image tag to `:latest` or specific version
   - Approve transaction
3. **Your bot automatically restarts with new code**

### Deployment Costs

Monthly costs on Akash Network:

| Resource | Amount | Cost/Month |
|----------|--------|-----------|
| CPU | 1 core | $2-4 |
| Memory | 2GB | $1-2 |
| Storage | 5GB | $0.50-1 |
| **Total** | - | **$3.50-7** |

Compare to AWS/Azure: $20-50/month for similar setup!

### Managing Your Deployment

**View Logs:**
```
Akash Console → Your Deployment → Logs Tab → Follow
```

**Add More Funds:**
```
Akash Console → Your Deployment → Deposit → Enter AKT → Approve
```

**Update Bot:**
```
Push to GitHub → Wait for build → Update deployment in Console
```

**Close Deployment:**
```
Akash Console → Your Deployment → Close → Approve
```

### Complete Deployment Guide

For detailed step-by-step instructions, see [Akash_Console_Guide.md](./docs/Akash_Console_Guide.md)

---

## 📁 Project Structure

```
telegram-video-bot/
├── bot.py                      # Main bot logic and handlers
├── transcriber.py              # Video processing and transcription
├── content_generator.py        # AI content generation
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── deploy.yaml                 # Akash deployment config
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
└── github/
    └── workflows 
        └── docker-build.yml.md  # docker-build
```

### Key Files Explained

**`bot.py`**
- Telegram bot initialization
- Message handlers for videos and links
- User interaction flow
- Document generation and delivery

**`transcriber_V2.py`**
- CloudConvert integration
- Audio extraction from video
- Whisper AI transcription
- Text cleanup and formatting

**`content_generator.py`**
- AkashChat API client
- Prompt templates for different content types
- Content formatting and structure

---

## 🛠️ Technologies Used

### Core Technologies

- **[Python 3.11+](https://www.python.org/)** - Programming language
- **[python-telegram-bot](https://python-telegram-bot.org/)** - Telegram Bot API wrapper
- **[OpenAI Whisper](https://github.com/openai/whisper)** - Speech-to-text transcription
- **[CloudConvert](https://cloudconvert.com/)** - Video/audio conversion
- **[AkashChat](https://chatapi.akash.network/)** - Decentralized AI inference
- **[python-docx](https://python-docx.readthedocs.io/)** - Word document generation
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Video download from platforms

### AI Models

- **Faster Whisper Base** - Fast and accurate transcription
- **Meta Llama 3.3 70B** - High-quality content generation
- Alternative models available on AkashChat

### Infrastructure

- **[Akash Network](https://akash.network/)** - Decentralized cloud deployment
- **[Docker](https://www.docker.com/)** - Containerization
- **[Docker Hub](https://hub.docker.com/)** - Image registry

---

## 📊 Performance

### Transcription Speed
- **Tiny model:** ~1x video length (fastest)
- **Base model:** ~2x video length (recommended)
- **Small model:** ~4x video length (more accurate)

### Content Generation Speed
- **Short-form:** 5-10 seconds
- **Blog post:** 15-30 seconds

### Resource Usage
- **CPU:** 1 core minimum (2 cores recommended)
- **RAM:** 2GB minimum (4GB recommended)
- **Storage:** 5GB minimum

---

## 🔒 Security

### Best Practices Implemented

- ✅ API keys stored in environment variables
- ✅ No sensitive data in Git repository
- ✅ File size validation (prevents abuse)
- ✅ Temporary file cleanup after processing
- ✅ User input sanitization

### Security Checklist

- [ ] Rotate API keys regularly
- [ ] Use `.env` file (never commit it)
- [ ] Monitor bot usage for abuse
- [ ] Implement rate limiting (optional)
- [ ] Set up logging and monitoring

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

1. **Report Bugs** - Open an issue with details
2. **Suggest Features** - Share your ideas
3. **Submit PRs** - Fix bugs or add features
4. **Improve Docs** - Help others understand the project
5. **Share the Project** - Star ⭐ and spread the word

### Development Setup

```bash
# Fork the repository
git clone https://github.com/yourusername/telegram-video-bot.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Write descriptive commit messages
- Test before submitting PR

---

## 🐛 Troubleshooting

### Common Issues

**Bot not responding**
```bash
# Check if bot is running
ps aux | grep bot.py

# Check logs
tail -f bot.log
```

**Transcription fails**
```bash
# Verify CloudConvert API key
# Check video format is supported
# Ensure file size is under limit
```

**Content generation errors**
```bash
# Verify AkashChat API key
# Check API endpoint: https://chatapi.akash.network/api/v1/chat/completions
# Ensure sufficient API credits
```

**Memory issues**
```bash
# Use smaller Whisper model
# Reduce concurrent processing
# Increase available RAM
```

---

## 📝 Roadmap

### Current Version (v1.0)
- [x] Video upload support
- [x] Video link support
- [x] Whisper transcription
- [x] Short-form content generation
- [x] Blog post generation
- [x] Word document output

### Planned Features (v1.1)
- [ ] Multiple language support
- [ ] Custom content templates
- [ ] Batch processing
- [ ] Progress indicators
- [ ] Content editing interface

### Future Ideas (v2.0+)
- [ ] Audio-only uploads
- [ ] Podcast transcription
- [ ] Twitter thread generation
- [ ] SEO optimization tools
- [ ] Analytics dashboard
- [ ] Multi-user support

---

---

## 🙏 Acknowledgments

### Technologies & Services

- **[OpenAI](https://openai.com/)** - For the incredible Whisper model
- **[Akash Network](https://akash.network/)** - For decentralized cloud infrastructure and Free Test Credits
- **[CloudConvert](https://cloudconvert.com/)** - For reliable media conversion
- **[Telegram](https://telegram.org/)** - For the amazing Bot API

### Inspiration

This project was built to solve the common problem of repurposing video content for different platforms. Special thanks to content creators who inspired this tool.

### Community

Thanks to everyone who contributed, tested, and provided feedback!

---

## 📞 Support

### Get Help

- **Email:** ayatiogochukwu@gmail.com

### Stay Connected

- **GitHub:** [@ayatiogo](https://github.com/AyatiOgo/)
- **Twitter:** [@yourusername](https://x.com/ayatiogo)
- **LinkedIn:** [Ayati Ogochukwu](https://www.linkedin.com/in/ayati-ogochukwu-23b032364)

---

## 💖 Show Your Support

If this project helped you, please consider:

- ⭐ **Starring the repo** on GitHub
- 🐦 **Sharing on Twitter**
- 💬 **Telling your friends**
- ☕ **Buying me a coffee** (if you set up sponsorship)


---

<div align="center">

**Made with ❤️ and ☕ by [Your Name](https://github.com/yourusername)**

[⬆ Back to Top](#-ai-video-to-content-telegram-bot)

</div>