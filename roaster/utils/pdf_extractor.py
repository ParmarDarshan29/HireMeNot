"""
PDF extraction utilities for resume processing
"""
import pdfplumber
from typing import Optional


def extract_text_from_pdf(pdf_file) -> str:
    """
    Extract text content from a PDF file.
    
    Args:
        pdf_file: Django UploadedFile object or file-like object
        
    Returns:
        Extracted text as a string
        
    Raises:
        ValueError: If the PDF is invalid or empty
        Exception: If extraction fails for other reasons
    """
    try:
        with pdfplumber.open(pdf_file) as pdf:
            if not pdf.pages:
                raise ValueError("PDF file is empty (no pages found)")
            
            text_parts = []
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
            
            full_text = "\n\n".join(text_parts).strip()
            
            if not full_text:
                raise ValueError("No text could be extracted from the PDF. It might be an image-based PDF.")
            
            return full_text
            
    except pdfplumber.PDFSyntaxError as e:
        raise ValueError(f"Invalid PDF file: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to extract text from PDF: {str(e)}")


def validate_resume_text(text: str, min_length: int = 50, max_length: int = 10000) -> tuple[bool, Optional[str]]:
    """
    Validate that the resume text is appropriate for roasting.
    
    Args:
        text: The resume text to validate
        min_length: Minimum required character count
        max_length: Maximum allowed character count
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not text or not text.strip():
        return False, "Resume text is empty"
    
    text_length = len(text.strip())
    
    if text_length < min_length:
        return False, f"Resume is too short (minimum {min_length} characters required)"
    
    if text_length > max_length:
        return False, f"Resume is too long (maximum {max_length} characters allowed)"
    
    return True, None
