# Quick Start Guide 🚀

## Getting Started in 5 Minutes

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Key (Choose One Option)

#### Option A: OpenRouter (Recommended - Free Tier Available)
1. Go to https://openrouter.ai/keys
2. Sign up and get your free API key
3. Edit `.env` file:
   ```
   USE_LOCAL_AI=false
   OPENROUTER_API_KEY=sk-or-v1-your-key-here
   ```

#### Option B: Local AI (Ollama - Completely Free)
1. Install Ollama: https://ollama.ai/
2. Pull a model: `ollama pull llama3.2`
3. Start Ollama: `ollama serve`
4. Edit `.env` file:
   ```
   USE_LOCAL_AI=true
   ```

### 3. Initialize Database
```bash
python manage.py migrate
```

### 4. Run the Server
```bash
python manage.py runserver
```

### 5. Open Your Browser
Navigate to: http://localhost:8000

## Test It Out!

### Sample Resume Text (Copy & Paste)
```
JOHN DOE
Email: johndoe@email.com | Phone: (555) 123-4567

SUMMARY
Results-driven professional with proven track record of excellence.
Passionate team player with great communication skills.
Self-starter who thinks outside the box.

EXPERIENCE
Senior Synergy Coordinator
ABC Corp | 2020 - Present
- Leveraged cross-functional partnerships to drive results
- Spearheaded mission-critical initiatives
- Proactively optimized workflows

SKILLS
- Expert in Microsoft Office
- Strong work ethic
- Detail-oriented
- Team player
```

## Tips

- The AI responds better to longer, more detailed resumes
- Try the "Roast Again" button for different variations
- Upvote your favorite roasts to see them on the leaderboard
- Share funny roasts with the Share button!

## Troubleshooting

### "OPENROUTER_API_KEY not found"
- Make sure you created the `.env` file (copy from `.env.example`)
- Add your API key or set `USE_LOCAL_AI=true`

### "Local AI API call failed"
- Check if Ollama is running: `ollama serve`
- Check if model is installed: `ollama list`
- Install model if needed: `ollama pull llama3.2`

### "No module named 'pdfplumber'"
- Run: `pip install -r requirements.txt`

## What's Next?

1. **Add a Giphy API Key** (optional)
   - Get free key at https://developers.giphy.com/
   - Add to `.env` as `GIPHY_API_KEY=your_key_here`
   - Get random memes with your roasts!

2. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```
   - Access admin at http://localhost:8000/admin
   - View and manage all roasts

3. **Customize the Roast Prompt**
   - Edit `roaster/utils/api.py`
   - Modify the prompt in `generate_resume_roast()` function

Enjoy roasting! 🔥
