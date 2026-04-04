# 🧠 MCQ Generator using LangChain & OpenAI

An AI-powered Multiple Choice Question (MCQ) generator built with LangChain 
and OpenAI GPT. Upload a text or PDF file and automatically generate MCQs 
with configurable difficulty and count — all via a clean Streamlit interface.

---

## 📌 Project Overview

This application allows users to:
- Upload a `.txt` or `.pdf` file as input content
- Specify the number of MCQs to generate (3–50)
- Choose a subject and complexity level
- Get well-structured MCQs displayed as a table instantly

**Tech Stack:** Python · LangChain · OpenAI · Streamlit · dotenv · pandas

---

## 🗂️ Project Structure
```
GenAI-LangChain_MCQGenerator/
├── src/
│   └── mcqgenerator/
│       ├── __init__.py
│       ├── MCQGenerator.py    # LangChain chain logic
│       ├── utils.py           # read_file, get_table_data helpers
│       └── logger.py          # logging setup
├── experiment/
│   └── trials.ipynb           # Jupyter notebook for experimentation
├── StreamlitApp.py            # Main Streamlit application
├── setup.py                   # Package setup
├── requirements.txt           # Python dependencies
├── response.json              # MCQ response format template
├── test.py                    # Test scripts
└── .env                       # API keys (not committed)
```

---

## ✅ Prerequisites

- Python 3.8+
- OpenAI API Key — get one at [platform.openai.com](https://platform.openai.com)
- Git installed
- pip package manager

---

## 🚀 How to Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/ramakrishna160222/GenAI-LangChain_MCQGenerator.git
cd GenAI-LangChain_MCQGenerator
```

**Step 2 — Create and activate virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Set up environment variables**

Create a `.env` file in the root folder:
```
OPENAI_API_KEY=your_openai_api_key_here
```

**Step 5 — Run the application**
```bash
streamlit run StreamlitApp.py
```

Open your browser at `http://localhost:8501`

---

## 🎯 How to Use

1. Upload a `.txt` or `.pdf` file containing the topic content
2. Enter the number of MCQs you want (between 3 and 50)
3. Enter the subject name (e.g. `Machine Learning`)
4. Enter the complexity level (e.g. `simple`, `medium`, `hard`)
5. Click **Create MCQs**
6. View generated MCQs as a table and review the evaluation

---

## ☁️ Deploy on AWS EC2

**Step 1 — Launch EC2 instance**
- Login to [AWS Console](https://aws.amazon.com/console/)
- Navigate to EC2 → Launch Instance → choose **Ubuntu**
- Add inbound rule for port **8501** in security group

**Step 2 — Setup the server**
```bash
sudo apt update && sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget python3-pip -y
```

**Step 3 — Clone and install**
```bash
git clone https://github.com/ramakrishna160222/GenAI-LangChain_MCQGenerator.git
cd GenAI-LangChain_MCQGenerator
pip3 install -r requirements.txt
```

**Step 4 — Add your API key**
```bash
touch .env
vi .env
# Press i → paste OPENAI_API_KEY=your_key → Esc → :wq → Enter
```

**Step 5 — Run**
```bash
python3 -m streamlit run StreamlitApp.py
```

Access at `http://<your-ec2-public-ip>:8501`

---

## 📦 Key Dependencies

| Package | Purpose |
|---|---|
| `langchain` | LLM chaining and prompt management |
| `langchain-community` | OpenAI callbacks |
| `openai` | GPT model API |
| `streamlit` | Web UI |
| `python-dotenv` | Environment variable management |
| `pandas` | MCQ table display |
| `PyPDF2` | PDF file reading |

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key |

---

## 👤 Author

**Rama Krishna** — [github.com/ramakrishna160222](https://github.com/ramakrishna160222)
