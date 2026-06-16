# 🚀 AI Document Intelligence System

A full-stack **AI-powered document analysis system** built with **Python, FastAPI, and Groq LLaMA 3.1**.

Upload PDF or DOCX documents and let AI extract meaningful insights including document type, summaries, important information, and key entities in structured JSON format.

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
│
```

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
- Cloud deployment
- Document dashboard
- RAG-based document search
- Multiple AI model support
- Advanced analytics

---

## 👨‍💻 Built With

Python + FastAPI + Groq LLaMA 3.1

A GenAI automation project demonstrating document processing, AI integration, and backend development.
