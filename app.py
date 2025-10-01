from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0.1:
        sentiment = 'Positive'
        emoji = '😊'
    elif polarity < -0.1:
        sentiment = 'Negative'
        emoji = '😞'
    else:
        sentiment = 'Neutral'
        emoji = '😐'
    
    return jsonify({
        'sentiment': sentiment,
        'polarity': round(polarity, 3),
        'subjectivity': round(subjectivity, 3),
        'emoji': emoji
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
