

import os
import glob
from dotenv import load_dotenv
import gradio as gr



#Imports for langchain
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_chroma import Chroma
#from langchain.vectorstores import FAISS
import numpy as np
from sklearn.manifold import TSNE
import plotly.graph_objects as go

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document
from langchain.document_loaders import PyMuPDFLoader


# In[3]:


model="gpt-4o-mini"
db_name="vector_db"


# In[4]:


# Load env variables to .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY","your-key")


# In[5]:


folders = glob.glob("../data/contract_dataset/*")
documents = []
for folder in folders:
    doc_type = os.path.basename(folder)
    for file_path in glob.glob(f"{folder}/**/*.*", recursive=True):
        print(file_path)
        ext = os.path.splitext(file_path)[-1].lower()
        try:
            if ext in [".txt", ".md", ".csv"]:
                loader = TextLoader(file_path)
            elif ext == ".pdf":
                loader = PyMuPDFLoader(file_path)  # Use PDF-compatible loader
            elif ext == ".json":
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                documents.append(Document(page_content=content, metadata={"source": file_path, "doc_type": doc_type}))
    
            else:
                print(f"Skipping unsupported file: {file_path}")
                continue
            folder_docs = loader.load()
            for doc in folder_docs:
                doc.metadata["doc_type"] = doc_type
                documents.append(doc)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")





## I am not chunking, as document looks small one.. lets see if required.

doc_types = set(doc.metadata["doc_type"] for doc in documents)
print(f"Document types:{', '.join(doc_types)}")


# In[9]:


## Put the chunks of data in to vector store that associates vector embeddings with each cunk
embeddings = OpenAIEmbeddings()


# In[10]:


# Check if Chroma data store already exists - if exist then delete the collection to start from scratch
if(os.path.exists(db_name)):
    Chroma(persist_directory=db_name,embedding_function=embeddings).delete_collection()


# In[11]:


vectorstore = Chroma.from_documents(documents=documents,embedding=embeddings,persist_directory=db_name)
print(f"Vectorstore created with: {vectorstore._collection.count()} documents.")






## Gradio Magic
def chat(message, history):
    result = conversation_chain.invoke({"question": message})
    return result["answer"]   




view = gr.ChatInterface(chat).launch()

