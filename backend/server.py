# backend/server.py

# Import the necessary libraries
import requests # For making HTTP requests to the OpenAI API
from flask import Flask, request, jsonify # Flask for creating the web server and handling requests
from flask_cors import CORS # CORS to allow cross-origin requests from the frontend

# Create an instance of a Flask application
app = Flask(__name__)

# Use CORS to allow cross-origin requests from the frontend
CORS(app)


# --- THIS IS THE VULNERABLE ENDPOINT ---
@app.route('/api/generate', methods=['POST'])
def generate_description():
    """
    Handles the API request to generate a product description.
    """
    # Get the JSON data from the incoming request, similar to req.body
    data = request.get_json()
    product_name = data.get('productName')
    keywords = data.get('keywords')

    # --- THIS IS THE INTENTIONAL VULNERABILITY ---
    # The secret OpenAI API key is hardcoded directly in the source code.
    # In a real application, this is a major security risk.
    OPENAI_API_KEY = 'FAKEAPIKEY'  # <--- REPLACE WITH YOUR OPENAI API KEY TO SEE THE APPLICATION FUNCTION

    # Construct the prompt to send to the AI
    prompt = f'Write a short, catchy, and professional product description for a "{product_name}" that highlights these keywords: "{keywords}".' #

    # Try to call the OpenAI API
    try:
        # Make a POST request to the OpenAI API using the 'requests' library
        response = requests.post(
            'https://api.openai.com/v1/chat/completions', #
            headers={
                'Content-Type': 'application/json', #
                # The hardcoded key is used in the authorization header
                'Authorization': f'Bearer {OPENAI_API_KEY}' #
            },
            json={
                "model": "gpt-3.5-turbo",  # Specify the model to use
                "messages": [{"role": "user", "content": prompt}],  # The prompt is sent as a message
                "max_tokens": 100,  # Limit the length of the response
            }
        )
        
        # Check if the response from OpenAI is OK. If not, it will raise an error.
        response.raise_for_status()

        # Parse the JSON response from OpenAI
        completion = response.json()
        
        # Extract the generated text from the OpenAI response
        description = completion['choices'][0]['message']['content'].strip() #
        
        # Send the description back to the frontend
        return jsonify({'description': description})

    except requests.exceptions.RequestException as error:
        # If the API call fails, send back an error
        print(f'Error in /api/generate: {error}')
        return jsonify({'error': 'Failed to generate description.'}), 500 #


# Start the server and listen on the specified port
if __name__ == '__main__':
    # Listen on port 5001 to match your original Node.js server
    app.run(port=5001) #