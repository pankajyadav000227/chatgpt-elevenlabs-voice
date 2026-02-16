# ChatGPT + ElevenLabs Voice Clone Integration

🎤 **Transform ChatGPT responses into realistic AI-generated speech with your own voice!**

## Features

- ✅ ChatGPT powered responses
- 🎙️ ElevenLabs text-to-speech generation
- 📊 Free tier: 10,000 characters/month
- 🌐 Web-based interface
- 🚀 Easy deployment to InfinityFree
- 📱 Mobile responsive design
- ⚡ Fast response generation

## Free Resources

- **ElevenLabs**: 10,000 free credits/month
- **OpenAI**: Free GPT-3.5-turbo trial
- **Hosting**: Completely free on InfinityFree

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/pankajyadav000227/chatgpt-elevenlabs-voice.git
cd chatgpt-elevenlabs-voice
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create `.env` file:

```env
ELEVENLABS_API_KEY=sk_37287d826f6874b434a9a083ea7fa41888b84578e5122e0d
OPENAI_API_KEY=your_openai_api_key
FLASK_ENV=development
PORT=5000
```

### 4. Get OpenAI API Key

1. Visit: https://platform.openai.com/api-keys
2. Sign up for free (get $18 free credits for 3 months)
3. Create new API key
4. Add to `.env` file

### 5. Run Locally

```bash
python app.py
```

Visit: http://localhost:5000

## Project Structure

```
.
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Configuration file
├── templates/
│   └── index.html           # Web interface
└── README.md
```

## API Endpoints

### `POST /api/generate`

Generate ChatGPT response and prepare audio

**Request:**
```json
{
  "text": "What is AI?",
  "voice_id": "21m00Tcm4TlvDq8ikWAM"
}
```

**Response:**
```json
{
  "gpt_response": "AI stands for Artificial Intelligence...",
  "audio_generated": true,
  "success": true,
  "character_count": 245
}
```

### `GET /api/health`

Check API health status

### `GET /api/voices`

Get available ElevenLabs voices

## Deployment to InfinityFree

### 1. Create InfinityFree Account

https://www.infinityfree.net

### 2. Setup FTP

- Download FileZilla
- Connect using FTP credentials from InfinityFree
- Upload all files to `public_html` folder

### 3. Install Dependencies via SSH

```bash
pip install -r requirements.txt
```

### 4. Update Configuration

- Change `debug=False` in app.py
- Set `FLASK_ENV=production` in .env

## Future Enhancements

### Voice Cloning (Paid Tier)

Once you upgrade ElevenLabs to Starter Plan:

1. Record 10+ seconds of clear audio (quiet room)
2. Upload to ElevenLabs
3. Get your voice ID
4. Replace `DEFAULT_VOICE_ID` in app.py

### Cost Estimation

- **ElevenLabs**: $5/month (Starter Plan) for voice cloning
- **OpenAI**: Pay-as-you-go (1000 requests ≈ $0.20)
- **Hosting**: Free tier available

## Troubleshooting

### API Key Issues

```bash
# Verify API key is set
echo $ELEVENLABS_API_KEY
```

### Port Already in Use

```bash
# Change port in .env
PORT=8000
```

### Module Not Found

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## Technologies Used

- **Backend**: Python Flask
- **APIs**: OpenAI (ChatGPT), ElevenLabs (TTS)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Hosting**: InfinityFree (Free)

## API Keys Reference

| Service | Key | Limit | Cost |
|---------|-----|-------|------|
| ElevenLabs | Free Tier | 10,000 characters/month | Free |
| OpenAI | GPT-3.5-turbo | $18 free credits | Then $0.002/1K tokens |
| InfinityFree | Free Hosting | ∞ | Free |

## License

MIT License - Feel free to use this project for personal and commercial purposes

## Support

For issues or questions:
1. Check GitHub Issues
2. Review documentation
3. Contact: [Your Contact]

---

**Made with ❤️ for voice lovers**
