import os

# OpenAI API configuration
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Text-to-Speech configuration
TTS_MODEL = "tts-1"
TTS_VOICE = "onyx"

# Flask configuration
DEBUG = True
HOST = '0.0.0.0'
PORT = 8080

# File storage configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'md', 'html'}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB