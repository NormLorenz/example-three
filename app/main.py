from flask import Flask, request, render_template, Response
import openai
from dotenv import load_dotenv
import config
from typing import Optional, Any


load_dotenv()  # Load environment variables from .env file

app: Flask = Flask(__name__)
debug: bool = config.DEBUG
greeting: str = config.GREETING
openai.api_key = config.OPENAI_API_KEY


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    image_url: Optional[str] = None
    revised_prompt: Optional[str] = None
    if request.method == 'POST':
        prompt: str = request.form['prompt']
        response: Any = openai.images.generate(
            prompt=prompt,
            model='dall-e-3',
            n=1,
            size='1024x1024'
        )
        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt
        return render_template('index.html', image_url=image_url, revised_prompt=revised_prompt)
    return render_template('index.html', image_url=None, revised_prompt=None)


if __name__ == '__main__':
    app.run(debug=True)
