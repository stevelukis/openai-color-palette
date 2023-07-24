# openai-color-palette

openai-color-palette is a web app written with Python and Flask, with a touch of JavaScript for the frontend.
It works by providing a sentence or keywords, and it will generate color palettes according to the input text.

### Preview
![preview.gif](readme_images%2Fpreview.gif)

### Requirements

You need an OpenAI API key to use this web app. [Create an account here](https://platform.openai.com/signup?launch).

### Getting Started

1. Clone the Repository

```shell
git clone https://github.com/your_username/openai-color-palette.git
cd openai-color-palette
```

2. Create a Virtual Environment

```shell
pip install virtualenv

# Create a virtual environment (you can choose any name you prefer).
virtualenv venv

# Activate the virtual environment.
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Save OpenAI API key as an environment variable. Create a file called `.env` and put this:

```
OPENAI_SECRET_KEY=your_openai_api_key_here
```

4. Run the web development server

```shell
flask run
```

5. Access the app

```
# Once the Flask app is running, open your web browser and navigate to:
http://localhost:5000
```

### License

This project is licensed under the MIT License.