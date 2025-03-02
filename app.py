from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to analyze emotion
def analyze_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    angry_keywords = ["angry", "furious", "irritated", "annoyed", "frustrated", "mad", "enraged", "pissed"]
    happy_keywords = ["excited", "joyful", "amazing", "great", "awesome", "fantastic", "happy"]
    sad_keywords = ["depressed", "unhappy", "lonely", "heartbroken", "miserable", "crying", "hopeless", "sad"]

    if any(word in text.lower() for word in angry_keywords):
        return {"suggestion": "Drink Water, Calm Yourself, try your hobby🙂‍↔️", "color": "#8B0000", "fontColor": "#FFFACD"}  
    elif polarity < -0.3 or any(word in text.lower() for word in sad_keywords):
        return {"suggestion": "Watch a feel-good movie, listen to calm music🎵, or talk to a close friend.😊", "color": "#4682B4", "fontColor": "#FFFFFF"}  
    elif polarity > 0.3 or any(word in text.lower() for word in happy_keywords):
        return {"suggestion": "Listen to some energetic music🕺 or go for a walk!😁", "color": "#FFD700", "fontColor": "#1B2631"}  
    else:
        return {"suggestion": "Try exploring a new hobby or reading something interesting.🤙", "color": "#F5F5DC", "fontColor": "#3E2723"}  

# API Route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    response = analyze_emotion(text)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
