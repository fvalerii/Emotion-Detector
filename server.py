from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect():
    statement = request.args.get('textToAnalyze')
    output = emotion_detector(statement)
    dominant_emotion = output['dominant_emotion']
    emotions = ", ".join(
        f"'{key}': {value}"
        for key, value in output.items()
        if key != 'dominant_emotion')
    response = (
        f"For the given statement, the system response is {emotions}."
        f"The dominant emotion is {dominant_emotion}")
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    