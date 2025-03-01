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
    angry_keywords = ["angry", "furious", "irritated", "annoyed", "frustrated", "mad", "enraged", "pissed"]
    happy_keywords = ["excited", "joyful", "amazing", "great", "awesome", "fantastic", "happy"]
    sad_keywords = ["depressed", "unhappy", "lonely", "heartbroken", "miserable", "crying", "hopeless", "sad"]
   

    if  any(word in text.lower() for word in angry_keywords):
        return "Drink Water, Calm Yourself, try your hobby"
    elif polarity < -0.3 or any(word in text.lower() for word in sad_keywords):
        return "Watch a feel-good movie, listen to calm music, or talk to a close friend."
    elif polarity > 0.3 or any(word in text.lower() for word in happy_keywords):
        return "Listen to some energetic music or go for a walk!"
    else:
        return "Try exploring a new hobby or reading something interesting."

# API Route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    suggestion = analyze_emotion(text)
    
    return jsonify({"suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)
