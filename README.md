# GeminiRAG

## Project Setup with Poetry

### Installation and Activation of Poetry Shell

1. **Install Poetry (if not already installed):**

   Download the official installer for your operating system from [Python Poetry Documentation](https://python-poetry.org/docs/).
   Follow the installation instructions based on your OS.

2. **Install Packages:**

   Run the following command to install the required packages for your project:

   ```bash
   poetry install
   ```

3. **Activate Poetry Shell:**

   To activate the Poetry shell and work within the project's virtual environment, run:

   ```bash
   poetry shell
   ```

### Using the API Endpoints

You can use `curl` as given as an example here or use any other api accessing tool like `postman` or `insomnia`

1. **Chat Endpoint (`/chat`)**

   - **Method:** POST
   - **Request Body (JSON):**

     ```json
     {
       "question": "Your question here"
     }
     ```

   - **Response (JSON):**

     ```json
     {
       "result": "Answer retrieved from the LLM",
       "source_documents": [
         "Page content from document 1",
         "Page content from document 2"
       ]
     }
     ```

   - **Example Usage (using cURL):**

     ```bash
     curl -X POST http://localhost:5000/chat -H 'Content-Type: application/json' -d '{"question": "What is the capital of France?"}'
     ```

2. **Upload Endpoint (`/upload`)**

   - **Method:** POST
   - **Request Body (Multipart Form):**

     A file named `document` containing the PDF document to be processed.

   - **Response (JSON):**

     ```json
     {
       "message": "Document uploaded successfully."
     }
     ```

   - **Example Usage (using cURL):**

     ```bash
     curl -X POST http://localhost:5000/upload -F 'document=@path/to/your/document.pdf'
     ```
