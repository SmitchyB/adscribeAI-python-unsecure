# InputValid-nodejs-unsecure - Node.js/Express Vulnerable Build (Improper Input Validation)

This repository houses a specific application build that is part of a larger comparative study, "Evaluating the Effectiveness of Secure Coding Practices Across Python, Node.js, and .NET 8." The experiment systematically assesses how secure coding techniques mitigate critical web application vulnerabilities—specifically improper input validation, insecure secrets management, and insecure error handling—across these three diverse development stacks. Through the development of paired vulnerable and secure application versions, this study aims to provide empirical evidence on the practical effectiveness of various security controls and the impact of architectural differences on developer effort and overall security posture.

## Purpose
This particular build contains the **Vulnerable Build** of the Node.js/Express application, specifically designed to demonstrate **Improper Input Validation**.

## Vulnerability Focus
This application build explicitly demonstrates:
* **Improper Input Validation:** The application fails to adequately check, filter, or sanitize user-supplied input, making it vulnerable to various attacks that leverage malformed or malicious data.

## Description of Vulnerability in this Build
In this version, the `/signup` endpoint directly processes user input from the request body without performing **any server-side input validation or sanitization**. This means that:
* Required fields can be left empty.
* Strings of excessive length can be submitted.
* Invalid data formats (e.g., malformed emails, phone numbers) are accepted.
* Inputs potentially containing malicious characters (e.g., script tags for XSS, SQL injection payloads) are processed directly and acknowledged as "received".
This complete lack of validation creates direct avenues for attackers to exploit the application, potentially leading to data corruption, unauthorized access, or other system compromises.

## Setup and Running the Application

### Prerequisites
* Node.js (LTS recommended) and npm (Node Package Manager).

### Steps
1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Navigate to the specific build folder, e.g.:
    cd InputValid-dotnet-secure/nodejs/vulnerable-input-validation # Assuming this is Node.js's backend
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    # or
    yarn install
    ```
    This will install `express` and `cors`.
3.  **Run the application:**
    ```bash
    node server.js
    ```
    The application will typically start on `http://localhost:5000`.

## API Endpoints

### `POST /signup`
* **Purpose:** Handles user registration requests. In this vulnerable build, it processes input without any server-side validation.
* **Method:** `POST`
* **Content-Type:** `application/json`
* **Request Body Example (JSON):**
    ```json
    {
      "username": "",  // Will be accepted
      "email": "malicious<script>alert(1)</script>", // Will be accepted
      "phoneNumber": "abc", // Will be accepted
      "password": "1", // Will be accepted
      "confirmPassword": "1" // Will be accepted
    }
    ```
* **Expected Behavior:**
    * **Any Input (valid or invalid):** Returns `200 OK` with a message like "Sign-up data received (unvalidated)!".
        * Backend console will show logs indicating `--- RECEIVED UNSECURE SIGN-UP DATA ---` and the raw, unvalidated input.

## Static Analysis Tooling
This specific build is designed to be analyzed by Static Analysis Security Testing (SAST) tools such as Semgrep and ESLint-Security (if configured) to measure their detection capabilities for the specific **input validation vulnerabilities** present in this build.
