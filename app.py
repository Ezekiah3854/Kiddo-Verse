import os
import json
from flask import Flask, render_template

# Load story data once
STORIES_PATH = os.path.join(os.path.dirname(__file__), 'stories.json')
with open(STORIES_PATH) as f:
    stories = json.load(f)

app = Flask(__name__)
@app.route('/')
def home():
    """render the home page"""
    return render_template('home.html')

@app.route('/api/learning-tools', methods=['GET'])
def learning_tools():
    """render the learning tools page"""
    return render_template('learning_tools.html')

@app.route('/api/stories-category', methods=['GET'])
def storiescategories():
    """render the read stories page"""
    return render_template('storiescategories.html')

@app.route('/api/stories-category/fairytales', methods=['GET'])
def fairytales():
    """render fairy tales page"""
    return render_template('fairytales.html')

@app.route('/api/stories-category/animal-stories', methods=['GET'])
def animalstories():
    """render animal stories page"""
    return render_template('animalstories.html')

@app.route('/api/stories-category/adventure-stories', methods=['GET'])
def adventurestories():
    """render adventure stories page"""
    return render_template('adventurestories.html')

@app.route('/api/stories-category/bedtime-stories', methods=['GET'])
def bedtimestories():
    """render bedtime stories page"""
    return render_template('bedtimestories.html')

@app.route('/story/<story_id>')
def story(story_id):
    """pass"""
    #find story by ID
    story_data = next((s for s in stories if s['id'] == story_id), None)
    if story_data is None:
        print("Mambo ni kama imekataaa kiasi!")

    return render_template('story.html', story = story_data)

if __name__ == '__main__':
    app.run(debug=True)