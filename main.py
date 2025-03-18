import streamlit as st  
import pickle
import os
import time
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()


st.title(" News Bot : News Research Tool 📺")

st.sidebar.title(" News Article Urls")

file_path="faiss_store_openai.pkl"
main_placeholder=st.empty()

urls=[]
for i in range(3):
    url=st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button(" Process URLs ") 

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("DataLoading ... Started ...  ✅✅✅ ")
    data=loader.load()

    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("TextSplitter ... Started ...  ✅✅✅ ")
    docs = text_splitter.split_documents(data)

    # create embeddings and save it to FAISS Index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai=FAISS.from_documents(docs, embeddings)
    main_placeholder.text("EmbeddingVector ... Started Building...  ✅✅✅ ")
    time.sleep(2)

    # Save the FIASS index to local
    vectorstore_openai.save_local("faiss_store")
 
llm= OpenAI(temperature=0.7, max_tokens=500)    
query= main_placeholder.text_input("Question 📝: ")
if query:
    vectorstore=FAISS.load_local("faiss_store", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    chain =  RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
    result=chain({"question": query}, return_only_outputs=True)

    st.header("Answer")
    st.subheader(result["answer"])

    # Display sources, if available
    sources=result.get("sources", "")

    if sources:
        st.subheader("Sources 📚:")
        sources_list= sources.split("\n")

        for source in sources_list:
            st.write(source)


    