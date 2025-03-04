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
    calm_keywords = ["chill", "relax", "cool", "easy", "smooth", "peace", "breeze", "soft", "quiet", "gentle", "calm down", "take it easy", "no worries", "all good", "stay cool", "slow down", "deep breath", "unwind", "easygoing", "laid-back"]
    excited_keywords = ["awesome", "amazing", "cool", "wow", "yay", "let's go", "super", "fantastic", "great", "hyped", "pumped", "thrilled", "stoked", "can't wait", "insane", "fire", "lit", "epic", "unreal", "wild"]
    scared_keywords = ["afraid", "terrified", "nervous", "worried", "anxious", "jumpy", "shaky", "startled", "spooked", "panicked", "uneasy", "tensed", "alarmed", "restless", "creeped out", "dreading", "on edge", "frightened", "shivering", "paranoid"]
    happy_keywords = ["joyful", "cheerful", "smiling", "grateful", "awesome", "great", "wonderful", "excited", "glad", "fantastic", "amazing", "bright", "uplifted", "positive", "content", "delighted", "thrilled", "sunny", "vibrant", "ecstatic"]
    sad_keywords = ["down", "unhappy", "depressed", "gloomy", "blue", "heartbroken", "miserable", "tearful", "lonely", "melancholy", "sorrowful", "upset", "low", "crushed", "devastated", "hurt", "heavy", "moody", "lost", "drained"]
    love_keywords = ["love","affection", "adore", "heart", "caring", "sweet", "cute", "romantic", "cherish", "passionate", "devoted", "loyal", "fond", "warm", "kisses", "hugs", "soulmate", "beloved", "butterflies", "connected", "deep"]
    if any(word in text.lower() for word in angry_keywords):
        return {"suggestion": "Drink Water, Calm Yourself, try your hobby🙂‍↔️", "color": "#8B0000", "fontColor": "#FFFACD"}  
    elif any(word in text.lower() for word in calm_keywords):
        return{"suggestion": "Take a deep breath and let the stress melt away🌿","color":"#A8D5BA","fontcolor":"#FAFAFA"}
    elif any(word in text.lower() for word in excited_keywords):
        return{"suggestion": "Enjoy the moment and let your energy shine!✨🎉","color":"#FF4500","fontcolor":"#ffffff"}
    elif any(word in text.lower() for word in scared_keywords):
        return{"suggestion": "Take a deep breath; you’re stronger than your fears. 🖤💪","color":"#000000","fontcolor":"#FFFFFF"}
    elif any(word in text.lower() for word in love_keywords):
        return{"suggestion": "Express your feelings openly; love grows when shared! ❤️","color":"#E91E63","fontcolor":"#FFDDC1"}
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
