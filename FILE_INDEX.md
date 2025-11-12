# 📑 HireMeNot - Complete File Index

## 📂 Project Structure

```
HireMeNot/
├── 📁 hiremenot/                    # Django Project Configuration
│   ├── __init__.py                  # Python package marker
│   ├── asgi.py                      # ASGI configuration
│   ├── settings.py                  # Main Django settings
│   ├── urls.py                      # Root URL configuration
│   └── wsgi.py                      # WSGI configuration
│
├── 📁 roaster/                      # Main Django Application
│   ├── 📁 migrations/               # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py          # Initial migration (Roast model)
│   │
│   ├── 📁 templates/                # HTML Templates
│   │   └── 📁 roaster/
│   │       ├── base.html            # Base template with navbar/footer
│   │       ├── home.html            # Homepage with upload form
│   │       ├── results.html         # Roast results display
│   │       └── leaderboard.html     # Top roasts leaderboard
│   │
│   ├── 📁 utils/                    # Utility Modules
│   │   ├── __init__.py
│   │   ├── api.py                   # AI API integration
│   │   └── pdf_extractor.py         # PDF text extraction
│   │
│   ├── __init__.py
│   ├── admin.py                     # Django admin configuration
│   ├── apps.py                      # App configuration
│   ├── models.py                    # Database models (Roast)
│   ├── tests.py                     # Unit tests (placeholder)
│   ├── urls.py                      # App URL patterns
│   └── views.py                     # View functions
│
├── 📁 media/                        # User uploads directory
│
├── 📄 manage.py                     # Django management script
├── 📄 requirements.txt              # Python dependencies
├── 📄 .env                          # Environment variables (gitignored)
├── 📄 .env.example                  # Environment variables template
├── 📄 .gitignore                    # Git ignore rules
├── 📄 setup.sh                      # Automated setup script
├── 📄 sample_resume.txt             # Sample resume for testing
│
└── 📚 Documentation/
    ├── 📄 README.md                 # Main project documentation
    ├── 📄 QUICKSTART.md             # 5-minute setup guide
    ├── 📄 USER_GUIDE.md             # User manual
    ├── 📄 PROJECT_SUMMARY.md        # Technical overview
    ├── 📄 DEPLOYMENT.md             # Deployment instructions
    ├── 📄 CONTRIBUTING.md           # Contribution guidelines
    ├── 📄 CHECKLIST.md              # Project completion checklist
    └── 📄 LICENSE                   # MIT License
```

## 📋 File Descriptions

### Core Django Files

#### `manage.py`
- Django's command-line utility
- Used for: migrations, runserver, createsuperuser, etc.
- Entry point for Django management commands

#### `hiremenot/settings.py`
- Main Django configuration
- Database settings
- Installed apps
- Middleware configuration
- Static/media file settings
- Environment variable loading

#### `hiremenot/urls.py`
- Root URL configuration
- Includes roaster app URLs
- Admin panel URL
- Media file serving (development)

### Application Files

#### `roaster/models.py`
- **Roast Model**: Stores resume and roast data
  - `resume_text`: TextField - original resume
  - `roast_text`: TextField - AI-generated roast
  - `timestamp`: DateTimeField - creation time
  - `upvotes`: IntegerField - vote count

#### `roaster/views.py`
- **home()**: Homepage view
- **upload_resume()**: Handle resume submission
- **results()**: Display roast results
- **roast_again()**: Regenerate roast
- **upvote()**: Handle upvoting
- **leaderboard()**: Show top roasts

#### `roaster/urls.py`
- URL patterns for roaster app
- Maps URLs to view functions
- Named URL patterns for reverse lookups

#### `roaster/admin.py`
- Django admin interface configuration
- Roast model registration
- Custom admin display options

### Utility Files

#### `roaster/utils/api.py`
**Functions:**
- `generate_resume_roast(resume_text, use_local)`: Main roast generator
- `_call_openrouter(prompt)`: OpenRouter API integration
- `_call_local_ai(prompt)`: Ollama local AI integration
- `get_random_meme(query)`: Giphy API integration

**Features:**
- Dual AI provider support
- Error handling
- Customizable prompts
- Temperature control

#### `roaster/utils/pdf_extractor.py`
**Functions:**
- `extract_text_from_pdf(pdf_file)`: Extract text from PDF
- `validate_resume_text(text, min_length, max_length)`: Validate text

**Features:**
- Multi-page PDF support
- Error handling for invalid PDFs
- Text validation

### Template Files

#### `roaster/templates/roaster/base.html`
- Base template for all pages
- Navigation bar
- Footer
- CSS styling (embedded)
- JavaScript utilities
- Message display system

#### `roaster/templates/roaster/home.html`
- Homepage with upload form
- Tabbed interface (PDF/Text)
- Form validation
- Hero section
- Feature cards

#### `roaster/templates/roaster/results.html`
- Roast display with animations
- Action buttons
- Meme/GIF display
- Resume preview (collapsible)
- Share functionality
- Easter eggs

#### `roaster/templates/roaster/leaderboard.html`
- Top 10 roasts display
- Ranked list with medals
- Upvote buttons
- Roast previews
- Empty state handling

### Configuration Files

#### `.env` (Not in Git)
- Environment variables for local development
- API keys
- Configuration flags
- Database URL (optional)

#### `.env.example`
- Template for `.env` file
- Shows all required variables
- Includes comments and examples
- Safe to commit to Git

#### `requirements.txt`
```
Django>=5.2,<6.0
python-dotenv>=1.0.0
pdfplumber>=0.11.0
requests>=2.31.0
Pillow>=10.0.0
```

#### `.gitignore`
- Python bytecode files
- Virtual environments
- Database files
- Media uploads
- Environment variables
- IDE files

### Setup Files

#### `setup.sh`
- Automated setup script
- Creates virtual environment
- Installs dependencies
- Runs migrations
- Creates .env file
- Offers to create superuser

**Usage:**
```bash
chmod +x setup.sh
./setup.sh
```

#### `sample_resume.txt`
- Example resume text
- For testing the application
- Contains typical buzzwords
- Ready to copy/paste

### Documentation Files

#### `README.md` (Main Documentation)
- Project overview
- Installation instructions
- Usage guide
- Features list
- Tech stack
- Configuration
- Troubleshooting

#### `QUICKSTART.md` (Quick Start Guide)
- 5-minute setup
- Two AI options (OpenRouter/Ollama)
- Basic usage
- Troubleshooting tips
- Sample resume included

#### `USER_GUIDE.md` (User Manual)
- Complete user documentation
- Step-by-step instructions
- Feature explanations
- Tips and tricks
- Easter eggs guide
- FAQ section

#### `PROJECT_SUMMARY.md` (Technical Overview)
- Comprehensive project overview
- Complete file structure
- Technology stack details
- API integration guide
- Database schema
- Learning outcomes

#### `DEPLOYMENT.md` (Deployment Guide)
- Multiple deployment options:
  - Heroku
  - Railway
  - DigitalOcean
  - VPS (Ubuntu)
- Configuration for production
- Security checklist
- Performance tips

#### `CONTRIBUTING.md` (Contribution Guide)
- How to contribute
- Code style guidelines
- Project structure
- Testing requirements
- Pull request process
- Feature ideas

#### `CHECKLIST.md` (Project Status)
- Complete feature checklist
- Implementation status
- Testing checklist
- Documentation checklist
- Deployment readiness
- Project statistics

#### `LICENSE`
- MIT License
- Open source
- Free to use and modify
- Attribution required

## 📊 File Statistics

### By Category

**Python Code:**
- Core files: 8
- Utility files: 2
- Total Python files: 10
- Approximate LOC: 600+

**Templates:**
- HTML files: 4
- Approximate LOC: 800+

**Documentation:**
- Markdown files: 8
- Approximate LOC: 2000+

**Configuration:**
- Config files: 4
- Setup scripts: 1

**Total Files:** 27 files + directories

### Lines of Code (Approximate)

| Category | Files | Lines |
|----------|-------|-------|
| Python | 10 | 600 |
| HTML/CSS | 4 | 800 |
| JavaScript | embedded | 100 |
| Documentation | 8 | 2000 |
| Configuration | 4 | 100 |
| **Total** | **27** | **3600** |

## 🎯 Key Files to Know

### For Development:
1. `roaster/views.py` - Main application logic
2. `roaster/models.py` - Database structure
3. `roaster/utils/api.py` - AI integration
4. `hiremenot/settings.py` - Configuration

### For Frontend:
1. `roaster/templates/roaster/base.html` - Base template
2. `roaster/templates/roaster/home.html` - Homepage
3. `roaster/templates/roaster/results.html` - Results page

### For Setup:
1. `requirements.txt` - Dependencies
2. `.env.example` - Environment template
3. `setup.sh` - Automated setup
4. `README.md` - Main guide

### For Deployment:
1. `DEPLOYMENT.md` - Deploy guide
2. `.env` - Environment config
3. `hiremenot/settings.py` - Django settings
4. `requirements.txt` - Dependencies

## 🔍 Finding Files

### To modify the roast prompt:
→ `roaster/utils/api.py` (line ~20)

### To change UI colors:
→ `roaster/templates/roaster/base.html` (CSS section)

### To adjust database model:
→ `roaster/models.py`

### To add new pages:
1. Create template in `roaster/templates/roaster/`
2. Add view in `roaster/views.py`
3. Add URL in `roaster/urls.py`

### To configure API keys:
→ `.env` file

### To modify admin interface:
→ `roaster/admin.py`

## 📚 Documentation Cross-Reference

| Need to... | Read this file |
|------------|----------------|
| Get started quickly | QUICKSTART.md |
| Learn all features | README.md |
| Use the application | USER_GUIDE.md |
| Understand the code | PROJECT_SUMMARY.md |
| Deploy to production | DEPLOYMENT.md |
| Contribute code | CONTRIBUTING.md |
| Check completion | CHECKLIST.md |
| Review license | LICENSE |

## 🎓 Learning Path

### Beginner:
1. Read README.md
2. Run setup.sh
3. Try the application
4. Read USER_GUIDE.md

### Intermediate:
1. Explore code structure
2. Modify roaster/views.py
3. Customize templates
4. Add features

### Advanced:
1. Study PROJECT_SUMMARY.md
2. Implement new AI providers
3. Optimize performance
4. Deploy to production

## 🔗 File Dependencies

```
manage.py
└── hiremenot/settings.py
    └── roaster/
        ├── models.py → admin.py
        ├── views.py → templates/
        ├── urls.py → views.py
        └── utils/
            ├── api.py
            └── pdf_extractor.py
```

## ✨ Important Notes

### Never Commit:
- `.env` (contains secrets)
- `db.sqlite3` (database)
- `media/` contents (uploads)
- `__pycache__/` (Python cache)

### Always Commit:
- `.env.example` (template)
- `requirements.txt` (dependencies)
- All `.py` files (code)
- All `.html` files (templates)
- All `.md` files (docs)

### Generated Files:
- `db.sqlite3` (by Django)
- `__pycache__/` (by Python)
- `migrations/000X_*.py` (by makemigrations)

---

**This index covers all 27 files in the HireMeNot project! 🔥**

© HireMeNot — We roast so you improve. 💼🔥
