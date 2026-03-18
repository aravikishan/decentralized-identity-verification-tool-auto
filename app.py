from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
import os

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE = 'identity_verification.db'

# Ensure database and tables are created
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE user_identity (
            user_id TEXT PRIMARY KEY,
            document_type TEXT,
            document_content BLOB
        )
    ''')
    cursor.execute('''
        CREATE TABLE verification_status (
            user_id TEXT PRIMARY KEY,
            status TEXT,
            timestamp DATETIME
        )
    ''')
    # Seed data
    cursor.execute("INSERT INTO verification_status (user_id, status, timestamp) VALUES ('user123', 'Pending', ?)", (datetime.now(),))
    conn.commit()
    conn.close()

# Data models
class UserIdentity(BaseModel):
    user_id: str
    document_type: str
    document_content: bytes

class VerificationStatus(BaseModel):
    user_id: str
    status: str
    timestamp: datetime

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_home():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.get("/verify", response_class=HTMLResponse)
async def read_verify():
    return templates.TemplateResponse("verify.html", {"request": {}})

@app.get("/status", response_class=HTMLResponse)
async def read_status():
    return templates.TemplateResponse("status.html", {"request": {}})

@app.get("/api-docs", response_class=HTMLResponse)
async def read_api_docs():
    return templates.TemplateResponse("api_docs.html", {"request": {}})

@app.post("/api/verify")
async def verify_identity(user_id: str, document_type: str, file: UploadFile = File(...)):
    content = await file.read()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_identity (user_id, document_type, document_content) VALUES (?, ?, ?)", (user_id, document_type, content))
    cursor.execute("INSERT INTO verification_status (user_id, status, timestamp) VALUES (?, ?, ?)", (user_id, 'Pending', datetime.now()))
    conn.commit()
    conn.close()
    return {"message": "Verification submitted successfully."}

@app.get("/api/status/{user_id}", response_model=VerificationStatus)
async def get_verification_status(user_id: str):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, status, timestamp FROM verification_status WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return VerificationStatus(user_id=row[0], status=row[1], timestamp=row[2])
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/api/documents/{user_id}")
async def get_user_documents(user_id: str):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT document_type, document_content FROM user_identity WHERE user_id = ?", (user_id,))
    documents = cursor.fetchall()
    conn.close()
    if documents:
        return {"documents": [{"document_type": doc[0], "document_content": doc[1]} for doc in documents]}
    raise HTTPException(status_code=404, detail="Documents not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
