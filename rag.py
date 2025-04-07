import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader # for web scraping
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from duckduckgo_search import DDGS 

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def search_duckduckgo(query):
    """
    Search DuckDuckGo for the given query and return the results.
    """
    try:
        with DDGS() as ddgs:
            results = [r['body'] for r in ddgs.text_search(query, max_results=1)] # loop is not needed as we only want the first result but we can keep it for future use if we want to get more results
            return "\n".join(results) # join the results with new line
        
    except Exception as e:
        print(f"Error searching DuckDuckGo: {e}")
        return None
    

def setup_rag_chain(url):
    """
    Loads the document from the URL, splits it into chunks, and creates a vector store.
    """
    try:
        # Load the document from the URL
        loader = WebBaseLoader(url)
        documents = loader.load()
        if not documents:
            print("No documents found.")
            return None
        
        # Split the document into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_doc = text_splitter.split_documents(documents)

        # Create a vector store using FAISS and HuggingFace embeddings
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_store = FAISS.from_documents(split_doc, embeddings) # create the vector store with the documents and embeddings

        return vector_store.as_retriever(search_kwargs={"k": 5}) # return the retriever with top 5 results
    
    except Exception as e:
        print(f"Error setting up RAG chain: {e}")
        return None
