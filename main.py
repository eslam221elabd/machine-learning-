from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from utils.mapping import map_query_to_category


# تعريف نموذج Pydantic لاستقبال الاستفسار
class QueryRequest(BaseModel):
    query: str

app = FastAPI()

@app.post("/query")
async def process_query(query_request: QueryRequest):
    """
    Receives a client query (with key "query"), uses the chatbot to detect
    the craftsmen category, then returns the sorted craftsmen data as JSON.
    """
    client_query = query_request.query
    
    if not client_query:
        raise HTTPException(status_code=400, detail="Query parameter 'query' is required")
    
    # Use the chatbot to detect the craftsmen category.
    detected_category = map_query_to_category(client_query)
    if not detected_category:
        raise HTTPException(status_code=500, detail="Could not detect a valid category")
    

    
    return {
        "detected_category": detected_category,
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
