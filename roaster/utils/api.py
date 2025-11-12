"""
API utilities for generating resume roasts using OpenRouter or local AI
"""
import os
import requests
from typing import Optional


def generate_resume_roast(resume_text: str, use_local: bool = False) -> str:
    """
    Generate a funny, witty roast for the given resume text.
    
    Args:
        resume_text: The resume text to roast
        use_local: If True, use local Ollama API instead of OpenRouter
        
    Returns:
        The AI-generated roast text as a string
        
    Raises:
        Exception: If the API call fails or returns an error
    """
    
    prompt = """You are RoastBot, an HR comedian who roasts resumes for fun. 
Roast this resume in a funny and sarcastic way, pointing out clichés, overused phrases, and exaggerations.
Keep it lighthearted and clean humor. Be savage but friendly, witty but not mean.

Resume:
{resume_text}

Your Roast:"""
    
    full_prompt = prompt.format(resume_text=resume_text)
    
    if use_local:
        return _call_local_ai(full_prompt)
    else:
        return _call_openrouter(full_prompt)


def _call_openrouter(prompt: str) -> str:
    """
    Call the OpenRouter API to generate a roast.
    
    Args:
        prompt: The formatted prompt to send
        
    Returns:
        The generated roast text
    """
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found in environment variables. "
            "Please add it to your .env file or set use_local=True to use Ollama."
        )
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": os.getenv('SITE_URL', 'http://localhost:8000'),
        "X-Title": "HireMeNot"
    }
    
    # Using a fast and free model
    model = os.getenv('OPENROUTER_MODEL', 'meta-llama/llama-3.2-3b-instruct:free')
    
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8,  # Higher temperature for more creative/funny responses
        "max_tokens": 500
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        roast = result['choices'][0]['message']['content'].strip()
        return roast
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"OpenRouter API call failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise Exception(f"Unexpected API response format: {str(e)}")


def _call_local_ai(prompt: str) -> str:
    """
    Call a local Ollama API to generate a roast.
    
    Args:
        prompt: The formatted prompt to send
        
    Returns:
        The generated roast text
    """
    # Default Ollama endpoint
    url = os.getenv('OLLAMA_URL', 'http://localhost:11434/api/generate')
    model = os.getenv('OLLAMA_MODEL', 'llama3.2')
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.8,
            "num_predict": 500
        }
    }
    
    try:
        response = requests.post(url, json=data, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        roast = result.get('response', '').strip()
        
        if not roast:
            raise Exception("Empty response from local AI")
            
        return roast
        
    except requests.exceptions.RequestException as e:
        raise Exception(
            f"Local AI API call failed: {str(e)}. "
            "Make sure Ollama is running (ollama serve) and the model is installed."
        )
    except (KeyError, ValueError) as e:
        raise Exception(f"Unexpected local AI response format: {str(e)}")


def get_random_meme(query: str = "funny") -> Optional[str]:
    """
    Fetch a random GIF from Giphy API.
    
    Args:
        query: Search term for the GIF
        
    Returns:
        URL of the GIF, or None if the call fails
    """
    api_key = os.getenv('GIPHY_API_KEY')
    
    if not api_key:
        # Return a fallback meme if no API key
        return None
    
    url = "https://api.giphy.com/v1/gifs/random"
    params = {
        "api_key": api_key,
        "tag": query,
        "rating": "pg-13"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        gif_url = result['data']['images']['original']['url']
        return gif_url
        
    except Exception:
        # Silently fail and return None - meme is optional
        return None
