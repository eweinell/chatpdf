# ChatPDF
The purpose of the `chatpdf` project is to demonstrate a conversational interface that allows users to query content within uploaded PDF documents using artificial intelligence techniques.

### Project Structure and Relevant Files

1. **`main.py`**: This file serves as the entry point for the application. It imports the `App` class from `src/app.py` and creates an instance of it, then calls the `run()` method to start the application.

2. **`.vscode/launch.json`**: This configuration file is used in Visual Studio Code (VSCode) to define debugging and running configurations for the project. It includes two main configurations:
   - **"Python: Current File"**: Launches a Python script in an integrated terminal.
   - **"Streamlit: Launch Streamlit App"**: Launches the Streamlit application using debugpy, sets the `STREAMLIT_DEBUG` environment variable to "1", and points to the main file of the Streamlit app.

3. **`app.py`**: This module contains the core functionality of the project. The `App` class initializes a user interface (`PDFChatbot`) and defines methods for tokenizing PDF content and initializing a conversational chat engine.

4. **`ui.py`**: This module contains the definition of the user interface class (`PDFChatbot`). It includes an `__init__` method that sets up the UI with methods for handling file uploads, tokenization, and conversation initialization.

### Project Installation and Dependency Management

To install and run the project locally using `uv` as the package manager, follow these steps:

1. **Clone or download the repository** containing the code.
   
2. **Navigate to the project directory**: Open a terminal and change the directory to where the project files are located.

3. **Install `uv` package manager**: If you don't already have `uv`, you can install it using pip:
   ```bash
   pip install uv
   ```

4. **Fetch dependencies**: Use `uv` to fetch the required dependencies listed in the `pyproject.toml` file. Run the following command:
   ```bash
   uv install .
   ```
   This command will read the `pyproject.toml` file and install all specified dependencies.

5. **Run the application**:
   - To run the application using VSCode, open the project in VSCode and use the "Streamlit: Launch Streamlit App" configuration from the launch.json file.
   - Alternatively, you can manually start the Streamlit server by running:
     ```bash
     streamlit run main.py
     ```

By following these steps, you will be able to install the dependencies using `uv` and start the `chatpdf` application locally.