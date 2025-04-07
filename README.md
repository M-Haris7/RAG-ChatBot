# RAG-ChatBot

## Overview
RAG-ChatBot is a Retrieval-Augmented Generation (RAG) chatbot application that processes URLs, retrieves relevant documents, and combines them with web search results to answer user queries. It is built using Python and Streamlit, leveraging modern libraries like LangChain, FAISS, and Groq's LLM.


Just provide a URL (e.g., from Wikipedia), and ask your question. The bot will:
- Scrape and chunk data from the anime webpage.
- Search the web using DuckDuckGo for real-time info.
- Use both sources to generate an accurate, LLM-based answer.

🚀 Tech Stack

| Component              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🧠 LLM                 | LLaMA 3.3 70B via Groq API                                                   |
| 📦 Embeddings          | HuggingFace Transformers - MiniLM (sentence-transformers/all-MiniLM-L6-v2) |
| 🧩 Vector Store        | FAISS - Facebook AI Similarity Search                                       |
| 🔎 Search Engine       | DuckDuckGo - Real-time web search API                                       |
| 🧱 Framework           | LangChain for chaining and orchestration                                   |
| 🌐 Web Scraping        | langchain_community.WebBaseLoader                                           |
| 🎨 Frontend            | Streamlit - Interactive Web UI                                              |

🛠️ Features

✅ Ask questions about any anime by just pasting a URL  
✅ Combines web search and page scraping for better context  
✅ Accurate, bullet-pointed responses with source references  
✅ User-friendly UI with zero coding required  
✅ Powered by open-source libraries and Hugging Face models  



🧪 How It Works

1. User inputs a URL (e.g., from Wikipedia)
2. rag.py:
   - Loads the webpage
   - Chunks content using RecursiveCharacterTextSplitter
   - Creates embeddings via Hugging Face
   - Stores them in a FAISS vector store
3. app.py:
   - Takes a user query
   - Uses retriever + DuckDuckGo for dual-context
   - Feeds both into a Groq-powered LLaMA 3.3 70B model
   - Returns a bullet-pointed, context-based answer

📂 File Structure

├── Rag.py                # Handles DuckDuckGo search, RAG setup, FAISS store  
├── app.py                # Streamlit UI, integrates LLM and all backend logic  
├── requirements.txt      # All dependencies  
├── your_image.png        # Homepage banner

🧑‍💻 Getting Started

1. Clone the repo
   git clone https://github.com/M-Haris7/RAG-ChatBot.git
   
   cd AI-Anime-Chatbot-with-RAG

3. Install dependencies
   pip install -r requirements.txt

4. Setup environment
   - Create a .env file and add your GROQ API key:
     GROQ_API_KEY=your_groq_api_key

5. Run the app
   streamlit run app.py

💡 Example Usage

🔗 URL: https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood  
❓ Question: "Who are the main characters and their powers?"  
✅ Response:
- Edward Elric is a skilled alchemist who lost his arm and leg in a failed transmutation. [RAG]
- Alphonse Elric is Edward's brother, whose soul is bound to a suit of armor. [RAG]
- Roy Mustang is a Flame Alchemist and a key figure in the military. [Search]



🧾 License

MIT License

🙌 Acknowledgements

- LangChain
- Hugging Face Transformers
- FAISS by Facebook
- DuckDuckGo Search
- Groq Cloud
- Streamlit

