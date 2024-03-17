# GeminiRAG

## Project Setup with Poetry

### Installation and Activation of Poetry Shell

1. **Install Poetry (if not already installed):**

   Download the official installer for your operating system from [invalid URL removed].
   Follow the installation instructions based on your OS.

2. **Create a New Project:**

   Open a terminal or command prompt and navigate to your desired project directory.
   Run the following command to create a new Poetry project named my-llm-project:

   ```bash
   poetry init --name my-llm-project
   ```

   Your project directory will now have a `pyproject.toml` file (Poetry configuration) and a `poetry.lock` file (dependency lock).
   You'll likely have additional files related to your llm package (e.g., `qa_chain.py`, `vector_database.py`, `embeddings.py`).
   Consider creating a `doc` directory to store uploaded PDFs (if applicable).

3. **Install Packages:**

   Run the following command to install the required packages for your project:

   ```bash
   poetry install
   ```

4. **Activate Poetry Shell:**

   To activate the Poetry shell and work within the project's virtual environment, run:

   ```bash
   poetry shell
   ```

### Using the API Endpoints

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
