'''
This is an end-to-end LLM project using langchain.
A news research tool has been built using langchain, opeai API and streamlit.
'''

Prerequisites:
-> openai api_key from https://platform.openai.com


Technical Architecture

Document Loader (UnstructuredURLLoader) -> Splits(RecursiveTextSplitter) -> Vector DB(FAISS) -> 
Retrieval(RetrievalQAWithSourcesChain) -> Prompt -> LLM(openAI) -> Answer


Below urls have been entered into the bot for getting an answer from LLM:

https://www.moneycontrol.com/sports/cricket/ipl/it-s-been-a-360-degree-turnaround-hardik-pandya-reflects-on-roller-coaster-last-few-months-article-12966763.html

https://www.moneycontrol.com/sports/cricket/ipl-7-big-players-set-to-miss-ipl-2025-videoshow-12872262.html

https://www.moneycontrol.com/sports/cricket/ipl-auction-10-most-expensive-players-in-the-history-of-ipl-auction-videoshow-12870830.html

Answer screenshot attached to the project.

Steps to run the project:

1. Clone repo to the local
2. openai api_key from https://platform.openai.com
3. create .env using command "nano .env"
4. update api_key in .env (api_key should start with sk-proj)
5. create virtual environment venv 
6. activate venv
7. run the streamlit app using "streamlit run main.py"
