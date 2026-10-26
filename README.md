# 🤖 Local GenAI Q&A Chatbot with Ollama & LangChain

An interactive, completely local Generative AI Q&A Chatbot built with **Ollama (using `llama3.2:3b`)**, orchestrating responses using **LangChain's Prompt Template Technique**, and served via a user-friendly **Streamlit UI**.

This application allows you to converse with open-source LLMs locally, adjustments for parameters like Max Tokens and Temperature, and operates entirely on your machine without requiring external API calls or compromising data privacy.

---

## ✨ Features

* **100% Local & Secure**: No external API calls are required (unless tracking is explicitly enabled), keeping your queries completely private.
* **Ollama Integration**: Powered by lightweight, high-performance open-source models like `llama3.2:3b`.
* **LangChain Orchestration**: Leverages the `ChatPromptTemplate` technique to structure and refine bot interactions.
* **Adjustable Parameters**: Live UI sliders to control `Temperature` (creativity) and `Max Tokens` (length).
* **Beautiful Streamlit UI**: Simple, responsive, and clean chat interface for seamless Q&A.
* **Developer Observability (Optional)**: Built-in hooks for LangSmith monitoring and tracing.

---

## 🛠️ Tech Stack

* **Framework**: [LangChain](https://github.com/langchain-ai/langchain)
* **Model Runner**: [Ollama](https://ollama.com/) (using the `llama3.2` model)
* **Frontend**: [Streamlit](https://streamlit.io/)
* **Runtime**: Python 3.10+
* **Environment Management**: `python-dotenv`

---

## 🚀 Getting Started

Follow these steps to set up and run the chatbot locally.

### 1. Prerequisites

* Ensure you have **Python 3.10+** installed.
* Download and install **Ollama** from [ollama.com](https://ollama.com/).

### 2. Prepare the Open-Source Model

Once Ollama is installed, run the following command in your terminal to download and start the `llama3.2:3b` model:

```bash
ollama run llama3.2

```

### 3. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

```

### 4. Set Up the Virtual Environment

Create and activate a virtual environment to keep your dependencies isolated:

```bash
# Create the virtual environment
python -m venv .venv

# Activate it:
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

```

### 5. Install Dependencies

Install the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt

```

> **Note**: This will install Streamlit, LangChain, LangChain Ollama integration, and dotenv support.

### 6. Environment Setup

Create a `.env` file in the root directory to store configuration variables (e.g., if you want to enable LangSmith tracking):

```env
# Optional: LangSmith Tracking (for debugging/monitoring)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_api_key_here

```

---

## 💻 Running the Application

To start the Streamlit server and launch the chatbot in your browser, execute:

```bash
streamlit run app.py

```

Once running, it will automatically open in your default browser at `http://localhost:8501`.

---

## 💡 How It Works

1. **User Query**: Users type a question into the input field in the Web UI.
2. **Dynamic Settings**: The sidebar allows users to configure hyperparameters like `Temperature` and `Max Tokens` on the fly.
3. **LangChain Prompt Templating**: Inside `app.py`, we define a custom system and user prompt using `ChatPromptTemplate` to structure how the model responds.
4. **Ollama Execution**: The query, along with the prompt template and parameters, are sent to the local Ollama instance running `llama3.2:3b`.
5. **Local Response**: The model runs locally on your machine, generates the text, and streams/updates it on the UI.

---

## 📂 Project Structure

```text
├── .venv/               # Virtual environment (ignored)
├── .env                 # Environment variables for tracking
├── app.py               # Main Streamlit & LangChain logic
├── requirements.txt     # Python dependency list
├── test.ipynb           # Notebook for testing model prompt/output
└── README.md            # Project documentation

```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2FYOUR_USERNAME%2FYOUR_REPO_NAME%2Fissues).

---


---

*Made with 💻, 🦙, and ⛓️ by Your Name.*
