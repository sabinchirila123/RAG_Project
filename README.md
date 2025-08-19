# Smart Librarian

This is a simple chatbot that recommends books by theme.  
It uses **Flask** + **Chroma + OpenAI (text + images + moderation)** for the backend, and a **React frontend** to display the recommendation, generated cover, and audio playback.

## Requirements
- Python 3.10+  
- Node.js 18+ + npm  
- A valid **OPENAI_API_KEY** in `.env`  
- Internet connection (OpenAI + gTTS)

## How to run
```bash
# 1. Install & run backend
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-..." > .env
python app.py  

# 2. Install & run frontend
cd frontend
npm install
npm run dev    
