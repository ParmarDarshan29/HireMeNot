# HireMeNot 🔥

**Where Resumes Go to Die**

A humorous Django web application that uses AI to roast resumes in a fun, meme-style interface. Upload your resume and get savage (but friendly) feedback from our AI comedian!

## Features

- **Resume Upload**: Support for PDF files or plain text input
- **AI-Powered Roasting**: Uses OpenRouter API or local Ollama for witty roasts
- **Fun UI**: Dark theme with animations and playful design
- **Roast Again**: Generate multiple roasts for the same resume
- **Upvoting System**: Vote for the funniest roasts
- **Leaderboard**: See the most popular roasts
- **Meme Integration**: Random GIFs from Giphy (optional)
- **Database Storage**: All roasts are saved with timestamps

## Tech Stack

- **Backend**: Django 5.2+
- **Frontend**: Bootstrap 5 with custom dark theme
- **AI**: OpenRouter API or Ollama (local)
- **PDF Processing**: pdfplumber
- **Database**: SQLite (default, can be changed)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Ollama for local AI

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ParmarDarshan29/HireMeNot.git
   cd HireMeNot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys:
   - For OpenRouter: Get a free API key at https://openrouter.ai/keys
   - For Giphy (optional): Get a key at https://developers.giphy.com/
   - Or set `USE_LOCAL_AI=true` to use Ollama locally

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser**
   Navigate to `http://localhost:8000`

## Using Local AI (Ollama)

If you want to run this completely free without external API calls:

1. **Install Ollama**
   - Visit https://ollama.ai/ and follow installation instructions
   
2. **Download a model**
   ```bash
   ollama pull llama3.2
   ```

3. **Start Ollama server**
   ```bash
   ollama serve
   ```

4. **Update .env**
   ```
   USE_LOCAL_AI=true
   ```

## Project Structure

```
HireMeNot/
├── hiremenot/           # Django project settings
│   ├── settings.py      # Main configuration
│   ├── urls.py          # Root URL routing
│   └── wsgi.py
├── roaster/             # Main app
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # App URL routing
│   ├── admin.py         # Admin configuration
│   ├── utils/           # Utility modules
│   │   ├── api.py       # AI API integration
│   │   └── pdf_extractor.py  # PDF processing
│   └── templates/       # HTML templates
│       └── roaster/
│           ├── base.html
│           ├── home.html
│           ├── results.html
│           └── leaderboard.html
├── media/               # Uploaded files
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## How It Works

1. **Upload**: User uploads a PDF resume or pastes text
2. **Extract**: System extracts text from PDF using pdfplumber
3. **Validate**: Checks text length and format
4. **AI Roast**: Sends text to AI with a humorous prompt
5. **Display**: Shows roast with animations and optional memes
6. **Save**: Stores roast in database for leaderboard

## API Configuration

### OpenRouter (Recommended for beginners)

- **Free tier available**: Most models have free options
- **Easy setup**: Just get an API key
- **Model**: Default uses `meta-llama/llama-3.2-3b-instruct:free`

### Ollama (For local/offline use)

- **Completely free**: Runs on your machine
- **Privacy**: No data sent to external services
- **Requires**: ~4GB RAM for small models
- **Speed**: Depends on your hardware

## Customization

### Change AI Model

Edit `.env`:
```
OPENROUTER_MODEL=meta-llama/llama-3.2-3b-instruct:free
# Or any other model from OpenRouter
```

### Modify Roast Prompt

Edit `roaster/utils/api.py`, function `generate_resume_roast()`:
```python
prompt = """Your custom prompt here..."""
```

### Adjust Temperature (Creativity)

In `roaster/utils/api.py`, change `temperature` value:
- Lower (0.5-0.7): More consistent, less random
- Higher (0.8-1.0): More creative, more varied

## Contributing

This is a fun project! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Share your funniest roasts!

## Disclaimer

**This project is for entertainment purposes only.**

- All roasts are AI-generated and meant to be humorous
- Not meant to offend or discriminate
- Use at your own discretion
- Don't take it seriously (but maybe take the feedback seriously? 😏)

## License

This project is open source and available under the MIT License.

## Support

If you encounter issues:

1. Check that all environment variables are set correctly
2. Ensure your API keys are valid
3. For Ollama: Make sure the service is running
4. Check Django logs for detailed error messages

## Credits

- Built with Django and Bootstrap
- AI powered by OpenRouter/Ollama
- Memes from Giphy
- Made with 💻 and ☕

---

**© HireMeNot — We roast so you improve. 💼🔥**
