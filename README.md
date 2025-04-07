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

✅ Ask questions about any article by just pasting a URL  
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
   
   cd <your_project_file>

3. Install dependencies
   pip install -r requirements.txt

4. Setup environment
   - Create a .env file and add your GROQ API key:
     GROQ_API_KEY=your_groq_api_key

5. Run the app
   streamlit run app.py

💡 Example Usage

🔗 URL: https://en.wikipedia.org/wiki/Attack_on_Titan_(TV_series)
❓ Question: "What are the themes of this anime?"  
✅ Response:
The anime "Attack on Titan" has several themes, including:
-Action [Source: RAG]
-Dark fantasy [Source: RAG]
-Post-apocalyptic [Source: RAG]
The anime also explores sociopolitical commentary and depth, making allusions to historical crises such as the Holocaust [Source: RAG]
However, it has been noted that the anime does not take a clear stance on these issues [Source: RAG]
The themes of freedom and the cost of freedom are also present, with the song "Jiyū no Daishō" (lit. "Cost of Freedom") by Linked Horizon being featured in the anime [Source: RAG]
Other themes present in the anime include the human condition, survival, and the struggle against oppressive forces [Source: RAG]
Note: The information about the themes of the human condition, survival, and the struggle against oppressive forces is not explicitly mentioned in the provided context, but it can be inferred based on the genre and plot of the anime. [Source: RAG]



🧾 License

MIT License

🙌 Acknowledgements

- LangChain
- Hugging Face Transformers
- FAISS by Facebook
- DuckDuckGo Search
- Groq Cloud
- Streamlit

