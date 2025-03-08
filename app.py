from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size='1024x1024',
            model='dall-e-3'
        )
        image_url = response['data'][0]['url']
        return render_template('index.html', image_url=image_url)
    return render_template('index.html', image_url=None)

if __name__ == '__main__':
    app.run(debug=True)
