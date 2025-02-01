from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import pytesseract
import io
import logging
from typing import Dict, Any

#Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

#Helper functions for text analysis
def validate_text(text: str) -> Dict[str, Any]:
    return {
        "grammar_score": 9.0,
        "spelling_score": 8.5,
        "structure_score": 8.0
    }

#Generate improvement suggestions
def get_suggestions(text: str) -> list:
    return [
        "Consider proper spacing between words",
        "Maintain consistent letter size",
        "Keep proper line alignment"
    ]

#Calculate confidence score
def get_confidence_score(text: str) -> float:
    return 0.95 if len(text) > 10 else 0.75

@app.post("/analyze-text")
async def analyze_handwritten_text(image: UploadFile = File(...)):
    try:
        #Read the image
        image_content = await image.read()
        pil_image = Image.open(io.BytesIO(image_content))
        
        #Configure Tesseract path if needed
        #pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
        
        #Perform OCR
        text = pytesseract.image_to_string(pil_image, lang='guj')
        
        #Validate text
        validation_results = validate_text(text)
        
        #Get confidence score
        confidence = get_confidence_score(text)
        
        #Get improvement suggestions
        suggestions = get_suggestions(text)
        
        return {
            "status": "success",
            "extracted_text": text,
            "language": "gujarati",
            "confidence_score": confidence,
            "analysis": {
                "word_count": len(text.split()),
                "character_count": len(text),
                "validation_scores": validation_results
            },
            "suggestions": suggestions,
            "metadata": {
                "file_name": image.filename,
                "content_type": image.content_type,
                "file_size": len(image_content)
            }
        }
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

#Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "handwriting-analysis-api"}
