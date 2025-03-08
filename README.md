# DALL-E Image Generator

This is a simple web application that uses the OpenAI API to generate images based on user-provided prompts. The application is built using Flask and allows users to enter a prompt, which is then sent to the OpenAI API to generate an image.

## Features

- Enter a prompt to generate an image using the DALL-E model.
- Display the generated image on the web page.
- Dark-themed and centered content for a better user experience.

## Prerequisites

- Python 3.6 or higher
- Flask
- OpenAI Python client library
- python-dotenv (optional, for loading environment variables from a `.env` file)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/dalle-image-generator.git
    cd dalle-image-generator
    ```

2. Create a virtual environment:

    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install Flask openai python-dotenv
    ```

5. Set your OpenAI API key:

    - Create a `.env` file in the project directory and add the following line:
        ```sh
        OPENAI_API_KEY=your_openai_api_key
        ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter a prompt in the input field and click the "Generate Image" button.

4. The generated image will be displayed on the page.

## Project Structure

- [app.py](http://_vscodecontentref_/0): The main Flask application file.
- [index.html](http://_vscodecontentref_/1): The HTML template for the web page.
- [styles.css](http://_vscodecontentref_/2): The CSS file for styling the web page.
- `.env`: The file containing environment variables (e.g., OpenAI API key).
- `README.md`: This file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.