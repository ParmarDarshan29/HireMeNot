# HireMeNot - Project Summary

## 🎯 Project Overview

**HireMeNot** is a humorous Django web application that uses AI to "roast" resumes in a fun, meme-style interface. The project demonstrates full-stack web development, AI API integration, and modern UI/UX design.

## ✨ Features Implemented

### Core Features
- ✅ Resume upload (PDF or plain text)
- ✅ PDF text extraction using pdfplumber
- ✅ AI-powered roast generation via OpenRouter API
- ✅ Alternative local AI support via Ollama
- ✅ Results page with animated roast display
- ✅ "Roast Again" functionality for same resume
- ✅ Database storage of all roasts
- ✅ Upvoting system for roasts
- ✅ Leaderboard showing top roasts

### UI/UX Features
- ✅ Dark theme with gradient accents
- ✅ Animated elements and transitions
- ✅ Responsive Bootstrap 5 layout
- ✅ Mobile-friendly design
- ✅ Easter eggs (Konami code, stamp animation)
- ✅ Social media share functionality
- ✅ Giphy meme integration (optional)

### Technical Features
- ✅ Environment variable management (.env)
- ✅ Modular code architecture
- ✅ Error handling and validation
- ✅ Django admin interface
- ✅ Clean URL routing
- ✅ AJAX upvote functionality
- ✅ Collapsible resume preview

## 📁 Project Structure

```
HireMeNot/
├── hiremenot/                 # Django project configuration
│   ├── __init__.py
│   ├── settings.py           # Main settings (includes .env support)
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
│
├── roaster/                   # Main Django app
│   ├── __init__.py
│   ├── models.py             # Roast model definition
│   ├── views.py              # View logic (home, upload, results, etc.)
│   ├── urls.py               # App URL patterns
│   ├── admin.py              # Admin interface configuration
│   ├── apps.py
│   ├── tests.py
│   │
│   ├── migrations/           # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── utils/                # Utility modules
│   │   ├── __init__.py
│   │   ├── api.py            # AI API integration
│   │   └── pdf_extractor.py  # PDF text extraction
│   │
│   └── templates/            # HTML templates
│       └── roaster/
│           ├── base.html     # Base template with navbar/footer
│           ├── home.html     # Homepage with upload form
│           ├── results.html  # Roast results display
│           └── leaderboard.html  # Top roasts leaderboard
│
├── media/                     # Uploaded files directory
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── .env                      # Environment variables (gitignored)
├── .gitignore                # Git ignore rules
├── README.md                 # Main documentation
├── QUICKSTART.md             # Quick start guide
├── CONTRIBUTING.md           # Contribution guidelines
├── setup.sh                  # Automated setup script
├── sample_resume.txt         # Sample resume for testing
└── LICENSE                   # MIT License
```

## 🔧 Technology Stack

### Backend
- **Django 5.2+**: Web framework
- **Python 3.8+**: Programming language
- **SQLite**: Database (default)
- **python-dotenv**: Environment variable management

### Frontend
- **Bootstrap 5**: CSS framework
- **HTML5/CSS3**: Markup and styling
- **JavaScript (ES6+)**: Interactive features
- **Google Fonts (Poppins)**: Typography

### APIs & Services
- **OpenRouter API**: Cloud AI for roast generation
- **Ollama**: Local AI alternative
- **Giphy API**: Random meme/GIF integration (optional)

### Libraries
- **pdfplumber**: PDF text extraction
- **requests**: HTTP requests
- **Pillow**: Image processing

## 🎨 Design Features

### Color Scheme
- Background: Dark gradients (#0d1117 → #1a1f2e)
- Accent: Fire gradient (orange #ff6b35 → pink #f72585)
- Text: Light (#e6edf3) and muted (#7d8590)

### Animations
- Fire emoji flicker
- Card hover effects
- Button transformations
- Stamp animation on results
- Glow border animation
- Fade-in transitions
- Pulse effects

### Typography
- Font: Poppins (300, 400, 600, 700)
- Gradient text for branding
- Responsive sizing

## 🔐 Configuration

### Environment Variables (.env)
```
USE_LOCAL_AI=false                    # Toggle AI provider
OPENROUTER_API_KEY=                   # OpenRouter API key
OPENROUTER_MODEL=                     # AI model name
OLLAMA_URL=http://localhost:11434    # Local Ollama endpoint
OLLAMA_MODEL=llama3.2                # Ollama model name
GIPHY_API_KEY=                        # Giphy API key (optional)
SITE_URL=http://localhost:8000       # Site URL
```

## 📊 Database Schema

### Roast Model
```python
class Roast(models.Model):
    resume_text = TextField()      # Original resume
    roast_text = TextField()       # AI-generated roast
    timestamp = DateTimeField()    # When created
    upvotes = IntegerField()       # Vote count
```

## 🚀 API Integration

### OpenRouter API
- Endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Model: `meta-llama/llama-3.2-3b-instruct:free` (default)
- Temperature: 0.8 (for creative responses)
- Max tokens: 500

### Ollama Local API
- Endpoint: `http://localhost:11434/api/generate`
- Model: `llama3.2` (default)
- Stream: false
- Temperature: 0.8

### Giphy API
- Endpoint: `https://api.giphy.com/v1/gifs/random`
- Rating: PG-13
- Fallback: Graceful failure if no key

## 🛣️ URL Routes

```
/                           # Homepage
/upload/                    # Resume upload handler (POST)
/results/<int:roast_id>/    # Display roast results
/roast-again/<int:roast_id>/ # Regenerate roast (POST)
/upvote/<int:roast_id>/     # Upvote roast (POST)
/leaderboard/               # Top roasts leaderboard
/admin/                     # Django admin interface
```

## 🎯 Key Functions

### roaster/utils/api.py
- `generate_resume_roast()`: Main AI roast generator
- `_call_openrouter()`: OpenRouter API integration
- `_call_local_ai()`: Ollama API integration
- `get_random_meme()`: Giphy API integration

### roaster/utils/pdf_extractor.py
- `extract_text_from_pdf()`: PDF text extraction
- `validate_resume_text()`: Text validation

### roaster/views.py
- `home()`: Homepage view
- `upload_resume()`: Handle resume upload
- `results()`: Display roast results
- `roast_again()`: Regenerate roast
- `upvote()`: Handle upvotes
- `leaderboard()`: Show top roasts

## 🎪 Special Features

### Easter Eggs
1. **Konami Code**: Type ↑↑↓↓←→←→BA for extra animation
2. **Rejected Stamp**: Animated stamp on results page
3. **Hover Effects**: Interactive UI elements

### Accessibility
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Mobile responsive
- High contrast colors

## 📝 Testing

### Manual Tests
- ✅ PDF upload with valid file
- ✅ Text paste with valid content
- ✅ Empty submission validation
- ✅ Invalid PDF handling
- ✅ API error handling
- ✅ Roast again functionality
- ✅ Upvote system
- ✅ Mobile responsiveness

## 🚧 Future Enhancements

### Planned Features
- Multiple AI provider selection
- Resume scoring system
- Custom roast intensity levels
- Export roast as image
- User accounts and history
- Roast categories/tags
- API rate limiting
- Caching for repeated roasts

### Performance Optimizations
- Redis caching
- Celery for async tasks
- PostgreSQL for production
- CDN for static files
- Compression middleware

## 📚 Documentation Files

1. **README.md**: Comprehensive project documentation
2. **QUICKSTART.md**: 5-minute setup guide
3. **CONTRIBUTING.md**: Contribution guidelines
4. **setup.sh**: Automated setup script
5. **sample_resume.txt**: Test resume example

## 🎓 Learning Outcomes

This project demonstrates:
- Django MVT architecture
- API integration (REST APIs)
- File upload handling
- PDF processing
- Environment configuration
- Database modeling
- Template inheritance
- AJAX requests
- Responsive design
- Error handling
- Security best practices

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- Django framework team
- Bootstrap contributors
- OpenRouter & Ollama teams
- Giphy API
- pdfplumber developers

---

**Built with 💻 and ☕ by the HireMeNot team**
**© HireMeNot — We roast so you improve. 💼🔥**
