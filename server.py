"""
Detects emotion
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    route
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the label is None, indicating an error or invalid input
    if response is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the sentiment label and score
    return f"""For the given statement, the system response is
    'anger': {response['anger']}, 
    'disgust': {response['disgust']}, 
    'fear': {response['fear']}, 
    'joy': {response['joy']} and 
    'sadness': {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    """
    render page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
