from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)
@app.route('/')
def home():
    """render the home page"""
    return render_template('home.html')

@app.route('/api/learning-tools', methods=['GET'])
def learning_tools():
    """render the learning tools page"""
    return render_template('learning_tools.html')

@app.route('/api/read-stories', methods=['GET'])
def read_stories():
    """render the read stories page"""
    return render_template('read_stories.html')

@app.route('/api/read-stories/fairytales', methods=['GET'])
def fairytales():
    """render fairy tales stories page"""
    return render_template('fairytales.html')

if __name__ == '__main__':
    app.run(debug=True)