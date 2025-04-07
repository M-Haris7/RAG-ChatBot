import streamlit as st
import os
from rag import search_duckduckgo, setup_rag_chain
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(page_title="RAG with DuckDuckGo and Groq", page_icon=":guardsman:", layout="centered")
st.title("RAG with DuckDuckGo and Groq")
st.caption("Enter a url & ask questions about it.")

st.image("images.png")

# Initialize session state variables

# st.session_state is used to store variables that need to persist across reruns of the app
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "processed_url" not in st.session_state:
    st.session_state.processed_url = ""

url = st.text_input("Enter a URL:", key="url_input")

if url:
    # Check if the URL has already been processed
    if st.session_state.processed_url != url:
        # If the URL is new, process it and update the session state
        with st.spinner("Processing URL..."):
            st.session_state.retriever = setup_rag_chain(url)
            st.session_state.processed_url = url
            if st.session_state.retriever:
                st.success("URL processed successfully!")
            else:
                st.error("Failed to process URL. Please check the URL and try again.")
                st.session_state.processed_url = ""  # Reset the processed URL if processing fails
    if st.session_state.retriever and st.session_state.processed_url == url:
        st.markdown("------")
        question = st.text_input("Ask a question:", key=f"query_{st.session_state.processed_url}")
        if question:
            with st.spinner("Thinking..."):
                try:
                    # retreive documents from FAISS vector store
                    retreived_docs = st.session_state.retriever.invoke(question)
                    rag_context = "\n".join([doc.page_content for doc in retreived_docs]) # join the documents with new line

                    # search DuckDuckGo for the question
                    duckduckgo_results = search_duckduckgo(question)

                    # Combine the retrieved documents and DuckDuckGo results
                    combined_context = f"RAG DATA:{rag_context}\n\nWEB SEARCH{duckduckgo_results}"

                    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=1, groq_api_key=os.getenv("GROQ_API_KEY")) # use the Groq API key from the environment variable
                    prompt = ChatPromptTemplate.from_template(
                        """
                        Answer the following question based on the provided context.
                        Use both retrieved documents and web search results.
                        Answer in Bullet points with all the relevant details.
                        Always tell source of your answer between [Search , RAG].
                        If the information isn't in the context, say you couldn't find it.

                        Context:
                        {context}

                        Question: {input}

                        Answer:
                        """
                    )
                    formatted_prompt = prompt.format_prompt(context=combined_context, input=question) # format the prompt with the context and question

                    # Get the answer from the LLM
                    response = llm.invoke(formatted_prompt)
                    st.markdown("**Answer:**")
                    st.success(response.content) # display the answer
                except Exception as e:
                    st.error(f"Error processing question: {str(e)}")

elif not url and st.session_state.processed_url:
    st.info("Please enter a new URL to process.")
    st.session_state.retreiver = None  # Reset the retriever if no URL is entered
    st.session_state.processed_url = ""  # Reset the processed URL if no URL is entered
else:
    st.info("Please enter a URL to process.")
   

