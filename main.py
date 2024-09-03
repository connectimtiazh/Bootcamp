from flask import Flask, request, jsonify, url_for
import openai
import os
import uuid
from config import *

app = Flask(__name__)

print ("hello")
# Ensure the UPLOAD_FOLDER exists
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'audio')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/text_to_speech', methods=['GET'])
def text_to_speech():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        response = openai.audio.speech.create(
            model=TTS_MODEL,
            voice=TTS_VOICE,
            input=text
        )

        # Generate a unique filename
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        # Save the audio file
        with open(filepath, 'wb') as f:
            for chunk in response.iter_bytes(chunk_size=1024 * 1024):
                f.write(chunk)

        # Generate the URL for the file
        file_url = url_for('static', filename=f'audio/{filename}', _external=True)

        return jsonify({
            "audio_url": file_url,
            "content_type": "audio/mpeg"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)