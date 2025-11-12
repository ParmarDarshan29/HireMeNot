from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import os

from .models import Roast
from .utils.pdf_extractor import extract_text_from_pdf, validate_resume_text
from .utils.api import generate_resume_roast, get_random_meme


def home(request):
    """Homepage with upload form"""
    return render(request, 'roaster/home.html')


@require_http_methods(["POST"])
def upload_resume(request):
    """Handle resume upload and generate roast"""
    try:
        # Get resume text from either file upload or text input
        resume_text = None
        
        # Check if PDF file was uploaded
        if 'resume_file' in request.FILES:
            pdf_file = request.FILES['resume_file']
            
            # Validate file type
            if not pdf_file.name.lower().endswith('.pdf'):
                messages.error(request, "Please upload a PDF file")
                return redirect('home')
            
            # Extract text from PDF
            try:
                resume_text = extract_text_from_pdf(pdf_file)
            except ValueError as e:
                messages.error(request, str(e))
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Failed to read PDF: {str(e)}")
                return redirect('home')
        
        # Check if text was provided directly
        elif 'resume_text' in request.POST:
            resume_text = request.POST.get('resume_text', '').strip()
        
        # Validate we have some text
        if not resume_text:
            messages.error(request, "Please provide a resume (upload PDF or paste text)")
            return redirect('home')
        
        # Validate resume text
        is_valid, error_msg = validate_resume_text(resume_text)
        if not is_valid:
            messages.error(request, error_msg)
            return redirect('home')
        
        # Check if using local AI or OpenRouter
        use_local = os.getenv('USE_LOCAL_AI', 'false').lower() == 'true'
        
        # Generate the roast
        try:
            roast_text = generate_resume_roast(resume_text, use_local=use_local)
        except Exception as e:
            messages.error(request, f"Failed to generate roast: {str(e)}")
            return redirect('home')
        
        # Get a random meme
        meme_url = get_random_meme(query="roasted")
        
        # Save to database
        roast = Roast.objects.create(
            resume_text=resume_text,
            roast_text=roast_text
        )
        
        # Store roast ID in session for "Roast Again" feature
        request.session['last_roast_id'] = roast.id
        
        # Redirect to results page
        return redirect('results', roast_id=roast.id)
        
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return redirect('home')


def results(request, roast_id):
    """Display roast results"""
    roast = get_object_or_404(Roast, id=roast_id)
    
    # Get a meme for the results page
    meme_url = get_random_meme(query="funny")
    
    context = {
        'roast': roast,
        'meme_url': meme_url,
    }
    
    return render(request, 'roaster/results.html', context)


@require_http_methods(["POST"])
def roast_again(request, roast_id):
    """Regenerate roast for the same resume"""
    roast = get_object_or_404(Roast, id=roast_id)
    
    try:
        # Check if using local AI or OpenRouter
        use_local = os.getenv('USE_LOCAL_AI', 'false').lower() == 'true'
        
        # Generate a new roast with the same resume
        new_roast_text = generate_resume_roast(roast.resume_text, use_local=use_local)
        
        # Create a new roast entry
        new_roast = Roast.objects.create(
            resume_text=roast.resume_text,
            roast_text=new_roast_text
        )
        
        messages.success(request, "New roast generated! 🔥")
        return redirect('results', roast_id=new_roast.id)
        
    except Exception as e:
        messages.error(request, f"Failed to generate new roast: {str(e)}")
        return redirect('results', roast_id=roast_id)


@require_http_methods(["POST"])
def upvote(request, roast_id):
    """Upvote a roast"""
    roast = get_object_or_404(Roast, id=roast_id)
    roast.upvotes += 1
    roast.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'upvotes': roast.upvotes})
    
    messages.success(request, "Thanks for the upvote! 👍")
    return redirect('results', roast_id=roast_id)


def leaderboard(request):
    """Display top roasts by upvotes"""
    top_roasts = Roast.objects.order_by('-upvotes', '-timestamp')[:10]
    
    context = {
        'top_roasts': top_roasts,
    }
    
    return render(request, 'roaster/leaderboard.html', context)

