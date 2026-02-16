from flask import Flask, render_template, request, jsonify, send_file
from elevenlabs.client import ElevenLabs
from openai import OpenAI
import os
from dotenv import load_dotenv
import io
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize clients
elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Default voice ID (Mark - Natural Conversations)
DEFAULT_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"

def get_gpt_response(prompt, model="gpt-3.5-turbo"):
    """Get response from ChatGPT"""
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def text_to_speech(text, voice_id=DEFAULT_VOICE_ID):
    """Convert text to speech using ElevenLabs"""
    try:
        audio = elevenlabs.generate(
            text=text,
            voice=voice_id,
            model="eleven_monolingual_v1"
        )
        return audio
    except Exception as e:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

@app.route('/api/generate', methods=['POST'])
def generate():
    """Generate ChatGPT response and convert to speech"""
    data = request.json
    user_input = data.get('text', '').strip()
    voice_id = data.get('voice_id', DEFAULT_VOICE_ID)
    
    if not user_input:
        return jsonify({'error': 'No text provided'}), 400
    
    if len(user_input) > 2000:
        return jsonify({'error': 'Input too long (max 2000 characters)'}), 400
    
    try:
        # Get ChatGPT response
        gpt_text = get_gpt_response(user_input)
        
        # Convert to speech
        audio = text_to_speech(gpt_text, voice_id)
        
        if not audio:
            return jsonify({'error': 'Failed to generate audio'}), 500
        
        return jsonify({
            'gpt_response': gpt_text,
            'audio_generated': True,
            'success': True,
            'character_count': len(gpt_text)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/voices')
def get_voices():
    """Get list of available voices"""
    try:
        voices = elevenlabs.voices.get_all()
        voice_list = []
        for voice in voices.voices[:10]:  # Limit to first 10
            voice_list.append({
                'id': voice.voice_id,
                'name': voice.name,
                'category': voice.category
            })
        return jsonify({'voices': voice_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)
