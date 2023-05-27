from langchain.document_loaders import TextLoader
from langchain.indexs import VectorstoreIndexCreator

text_loader = TextLoader('CauseAndEffectOfHomelessness.txt',encoding-'utf8') 
index=VectorstoreIndexCreater().from_loaders([text_loader])
query="Why peope become homeless?"
index.query(query)