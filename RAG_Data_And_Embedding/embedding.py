from qdrant_client import QdrantClient
from uuid import uuid4
import json
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
client = QdrantClient(url="http://localhost:6321")


embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

documents = []
with open('data_rag_gpt/docs_mis.jsonl', 'r') as f:
    for line in f:
        doc = json.loads(line)
        documents.append(Document(
            page_content=doc,
        ))
prev_id = None
id = str(uuid4())
ids = [id]
for text in documents:
    next_id =str(uuid4())
    text.metadata = {"prev_id": prev_id, "id": id, "next_id": next_id}
    prev_id = id
    id = next_id
    ids.append(id)


client.create_collection(
    collection_name="kltn_collection_v3",
    vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name="kltn_collection_v3",
    embedding=embeddings,
)

vector_store.add_documents(documents=documents, ids=ids)