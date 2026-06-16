from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from db import SessionLocal, Document

import json
import os

from pdf_reader import read_pdf
from docx_reader import read_docx

from analyzer import analyze_document


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():

    return {
        "message": "AI Document Intelligence System Running"
    }



@app.post("/analyze")
async def analyze(file: UploadFile):

    try:

        # create uploads folder on Render if missing
        os.makedirs("uploads", exist_ok=True)


        path = "uploads/" + file.filename


        with open(path, "wb") as f:
            f.write(await file.read())


        if file.filename.endswith(".pdf"):

            text = read_pdf(path)


        elif file.filename.endswith(".docx"):

            text = read_docx(path)


        else:

            return {
                "error": "Only PDF and DOCX allowed"
            }


        result = analyze_document(text)


        db = SessionLocal()


        document = Document(
            filename=file.filename,
            extracted_text=text,
            analysis=json.dumps(result)
        )


        db.add(document)
        db.commit()
        db.close()


        return {
            "status": "success",
            "analysis": result
        }


    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }



@app.get("/documents")
def get_documents():

    try:

        db = SessionLocal()

        documents = db.query(Document).all()

        db.close()

        return documents


    except Exception as e:

        return {
            "error": str(e)
        }
