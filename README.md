# 🚀 AI Document Intelligence System

A full-stack **AI-powered document analysis system** built with **Python, FastAPI, and Groq LLaMA 3.1**.

Upload PDF or DOCX documents and let AI extract meaningful insights including document type, summaries, important information, and key entities in structured JSON format.

---

## 🌐 Live Demo

Frontend:
https://vineela959.github.io/ai-document-intelligence-system/

Backend API:
https://ai-document-intelligence-system-255u.onrender.com/docs

---

## ✨ Features

- 📄 Upload PDF and DOCX files
- 🔍 Automatic text extraction
- 🤖 AI-powered document understanding using Groq LLaMA 3.1
- 🧠 Generate structured JSON analysis
- 🏷️ Extract important entities and information
- 💾 Store analyzed documents using SQLite database
- ⚡ FastAPI REST API backend
- 🌐 Simple frontend interface
- ☁️ Live deployment on Render

---

## 🏗️ System Architecture

```
User Uploads Document
          |
          ↓
     FastAPI Backend
          |
          ↓
 PDF/DOCX Text Extraction
          |
          ↓
   Groq LLaMA 3.1 AI Analysis
          |
          ↓
 Structured JSON Response
          |
          ↓
      SQLite Database
```

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Groq API
- LLaMA 3.1

### Document Processing
- PyPDF
- python-docx

### Database
- SQLite
- SQLAlchemy

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- GitHub Pages (Frontend)
- Render (Backend)

---

## 📂 Project Structure

```
AI-Document-Intelligence-System/

│
├── app.py
├── analyzer.py
├── db.py
├── pdf_reader.py
├── docx_reader.py
├── requirements.txt
│
├── frontend/
│   └── index.html
```

---

## ⚙️ How It Works

1. User uploads a PDF/DOCX file
2. Backend extracts text from the document
3. Extracted text is sent to Groq LLaMA model
4. AI analyzes the content
5. System returns structured JSON response
6. Analysis is stored in database

---

## ⚙️ Installation

### Clone repository

```bash
git clone <your-repository-link>
```

Move into project folder:

```bash
cd AI-Document-Intelligence-System
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

Start FastAPI server:

```bash
uvicorn app:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

### Analyze Document

```
POST /analyze
```

Upload a PDF/DOCX file and receive AI analysis.

Example response:

```json
{
  "document_type": "Resume",
  "summary": "Developer experienced in building AI applications",
  "important_information": [
    "Experience: 3 years",
    "Role: Python Developer"
  ],
  "entities": [
    "Python",
    "FastAPI",
    "Machine Learning"
  ]
}
```

---

### Get Document History

```
GET /documents
```

Returns previously analyzed documents stored in database.

---

## 🚀 Future Improvements

- User authentication
- Cloud storage integration
- Dashboard UI
- RAG-based document search
- Multi-AI model support
- Advanced analytics

---

## 👨‍💻 Built With

Python + FastAPI + Groq LLaMA 3.1

A GenAI automation project demonstrating document processing, AI integration, and full-stack development.
