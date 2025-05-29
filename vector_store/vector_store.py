from chromadb import Client
from chromadb.config import Settings

def init_vector_store(persist_directory: str = 'vector_db'):
    client = Client(Settings(chroma_db_impl='duckdb+parquet', persist_directory=persist_directory))
    return client.get_or_create_collection('memory_collection')

# Example usage
if __name__ == '__main__':
    collection = init_vector_store()
    print(f"Initialized vector collection: {collection.name}")
