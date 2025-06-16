# AdScribe.AI - Python/Flask (Vulnerable Version)

This repository contains the Python/Flask stack version of the AdScribe.AI application. This version is intentionally vulnerable and serves as a test case for a university research project evaluating the effectiveness of secure coding practices and SAST (Static Analysis Security Testing) tools.

## Application Purpose

AdScribe.AI is a simple marketing tool that uses the OpenAI API to generate compelling product descriptions based on a product name and user-provided keywords.

## Research Context: The Vulnerability

The primary purpose of this repository is to demonstrate an unsecure but common coding practice: **hardcoded secrets**.

In this application, the `OPENAI_API_KEY` is written directly into the backend source code (`backend/server.py`). This is a significant security risk because it exposes the secret to anyone with access to the codebase and makes it visible in the version control history. This build is used to test whether security scanning tools can successfully detect this type of vulnerability.

## How to Run This Application

This is a standard Python application with a React frontend and a Python/Flask backend.

### Prerequisites
* Python 3 installed.
* An active OpenAI API key.

### Instructions

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    ```

2.  **Set the API Key:**
    * Navigate to the `backend/` directory.
    * Open the `server.py` file.
    * Find the line `OPENAI_API_KEY = 'FakeAPIKeyGoesHere'` and replace the placeholder with your actual OpenAI API key.

3.  **Set up the Backend (Python):**
    * Navigate to the `backend/` directory.
    * Create and activate a virtual environment:
        ```bash
        # Create the virtual environment
        python -m venv venv
        # Activate on Windows (PowerShell)
        .\venv\Scripts\Activate.ps1
        # Activate on Mac/Linux
        source venv/bin/activate
        ```
    * Create a `requirements.txt` file for your dependencies:
        ```bash
        pip freeze > requirements.txt
        ```
    * Install the Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Set up the Frontend (React):**
    * In a second terminal, navigate to the `frontend/` folder.
    * Install the Node.js dependencies:
        ```bash
        npm install
        ```

5.  **Run the Application:**
    * In your backend terminal (with the venv active), navigate to the project root folder and run:
        ```bash
        flask --app backend/server run
        ```
        The backend will run on `http://localhost:5001`.
    * In your frontend terminal, run:
        ```bash
        npm start
        ```
        The application will open in your browser at `http://localhost:3000`.
