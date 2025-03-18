'''
This is an end-to-end LLM project using langchain.
A news research tool has been built using langchain, opeai API and streamlit.
'''

Prerequisites:
-> openai api_key from https://platform.openai.com


Technical Architecture

Document Loader (UnstructuredURLLoader) -> Splits(RecursiveTextSplitter) -> Vector DB(FAISS) -> 
Retrieval(RetrievalQAWithSourcesChain) -> Prompt -> LLM(openAI) -> Answer
