from flask import Flask, request, jsonify
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Chroma
from openai import OpenAI
from summary_tool import get_summary_by_title
from flask_cors import CORS
import os
import re
from gtts import gTTS
from uuid import uuid4
from dotenv import load_dotenv
app = Flask(__name__)
CORS(app)

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Lipsește OPENAI_API_KEY. Adaugă-l în .env sau ca variabilă de mediu.")
client = OpenAI()


with open("books.md", "r", encoding="utf-8") as f:
    text = f.read()

docs_raw = text.split("## Title: ")[1:]
documents = []
for doc in docs_raw:
    title, summary = doc.strip().split("\n", 1)
    documents.append(Document(page_content=summary.strip(), metadata={"title": title.strip()}))

embedding = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma.from_documents(documents, embedding, persist_directory="./book_db")
retriever = db.as_retriever()

BAD_WORDS = {
    "prost", "proasta", "praf", "varza", "aiurea",
    "lenes", "leneș", "slab", "jalnic", "penibil",
    "vai de capul tau", "vai steaua ta", "esti varza", "esti praf"
}

def contains_profanity(text):
    words = set(re.findall(r"\b\w+\b", text.lower()))
    return bool(words & BAD_WORDS)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Missing 'query'"}), 400

    if contains_profanity(query):
        return jsonify({
            "blocked": True,
            "message": "Te rog să folosești un limbaj adecvat. Sunt aici să te ajut cu recomandări de cărți."
        }), 200

    results = retriever.get_relevant_documents(query)
    if not results:
        return jsonify({
            "found": False,
            "message": "Nu am găsit nicio carte relevantă pentru această temă."
        }), 200

    top_doc = results[0]
    title = top_doc.metadata["title"]
    full_summary = get_summary_by_title(title)

    prompt = f"""    
    Utilizatorul caută o carte. Pe baza interesului: „{query}”,
    ai selectat cartea: **{title}**.
     
    Scrie o recomandare în stil conversațional, prietenos și în limba română,
    apoi adaugă și următorul rezumat detaliat al cărții:

    {full_summary}

    Textul trebuie să fie format din 3-4 propoziții și să fie concis.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    image_prompt = f"O copertă de carte ilustrată care reflectă tema cărții '{title}'. Stil artistic, simplu, evocator."

    image_response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = image_response.data[0].url

    text_to_speak = response.choices[0].message.content
    audio_filename = f"static/audio_{uuid4().hex}.mp3"


    tts = gTTS(text=text_to_speak, lang="ro")
    tts.save(audio_filename)

    audio_url = f"http://localhost:5000/{audio_filename}"

    return jsonify({
        "found": True,
        "title": title,
        "recommendation": response.choices[0].message.content,
        "image_url": image_url,
        "audio_url": audio_url
    })

if __name__ == "__main__":
    app.run(debug=True)
