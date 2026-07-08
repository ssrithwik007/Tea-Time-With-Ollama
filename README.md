# Tea Time with Ollama

Tea Time with Ollama is a lightweight chat application built with Streamlit that allows users to interact with locally hosted Ollama language models. The application provides a clean interface for chatting with any installed model, maintaining conversation history, switching between models, and exporting conversations.

## Features

- Chat with locally installed Ollama models
- Automatic detection of available models
- Conversation history
- Model switching
- Clear chat functionality
- Download conversation as a text file
- Loading indicator while generating responses
- Connection status indicator
- Clean, responsive chat interface with custom message bubbles

## Tech Stack

- Python
- Streamlit
- Ollama Python Client

## Prerequisites

Before running the application, ensure you have:

- Python 3.10 or later
- Ollama installed
- At least one Ollama model downloaded

Install Ollama from:

https://ollama.com

Download a model, for example:

```bash
ollama pull llama3.2
```

Start the Ollama server:

```bash
ollama serve
```

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/tea-time-with-ollama.git
cd tea-time-with-ollama
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Project Structure

```
Tea-Time-With-Ollama/
│
├── app.py
├── ollama_service.py
├── helpers.py
├── requirements.txt
└── README.md
```

## Usage

1. Ensure the Ollama server is running.
2. Launch the Streamlit application.
3. Select an available model from the sidebar.
4. Start chatting.
5. Download the conversation if needed.
6. Clear the chat to begin a new conversation.
