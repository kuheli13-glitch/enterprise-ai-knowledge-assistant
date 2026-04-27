from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.adapters.models import Document

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Enterprise AI Knowledge Assistant API is running"}


@router.get("/health")
def health_check():
    return {"status": "success", "message": "Server is healthy"}


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Only .txt files are supported currently"
        )

    content_bytes = await file.read()
    content_text = content_bytes.decode("utf-8")

    db: Session = SessionLocal()

    new_doc = Document(
        file_name=file.filename,
        file_type="txt",
        content=content_text
    )

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    db.close()

    return {
        "id": new_doc.id,
        "file_name": new_doc.file_name,
        "message": "File uploaded successfully"
    }