from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, Flask is running!"

# Function to analyze emotion & give suggestions
def analyze_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Happy, Sad & Angry Keywords
    happy_keywords = ["excited", "joyful", "amazing", "great", "awesome", "fantastic", "happy"]
    sad_keywords = ["depressed", "unhappy", "lonely", "heartbroken", "miserable", "crying", "hopeless", "sad"]
    angry_keywords = ["angry", "furious", "irritated", "annoyed", "frustrated", "mad", "enraged", "pissed"]

    if polarity > 0.3 or any(word in text.lower() for word in happy_keywords):
        return "Happy", "Listen to some energetic music or go for a walk!"
    elif polarity < -0.3 or any(word in text.lower() for word in sad_keywords):
        return "Sad", "Watch a feel-good movie, listen to calm music, or talk to a close friend."
    elif any(word in text.lower() for word in angry_keywords):
        return "Angry", "Take deep breaths, drink water, or try meditation to calm yourself."
    else:
        return "Neutral", "Try exploring a new hobby or reading something interesting."

# API Route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    mood, suggestion = analyze_emotion(text)
    
    return jsonify({"mood": mood, "suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)
