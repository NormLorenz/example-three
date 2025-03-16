from flask import Flask, request, render_template
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config.from_object('config.Config')

# Use square brackets to access the config value
openai.api_key = app.config['OPENAI_API_KEY']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.images.generate(
            prompt=prompt,
            model='dall-e-3',
            n=1,
            size='1024x1024'
        )
        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt
        return render_template('index.html', image_url=image_url, revised_prompt=revised_prompt)
    return render_template('index.html', image_url=None)


if __name__ == '__main__':
    app.run(debug=True)
