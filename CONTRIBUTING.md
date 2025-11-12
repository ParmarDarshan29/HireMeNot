# Contributing to HireMeNot 🔥

Thanks for your interest in contributing! This project is meant to be fun, so don't stress too much. 😎

## How to Contribute

### 🐛 Report Bugs
- Use GitHub Issues
- Describe what happened vs. what you expected
- Include error messages and screenshots if possible
- Mention your OS, Python version, and Django version

### 💡 Suggest Features
- Check if the feature already exists or is in progress
- Explain the use case and benefit
- Keep it aligned with the project's humorous tone

### 🔨 Submit Code

#### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/HireMeNot.git
cd HireMeNot
```

#### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

#### 3. Make Changes
- Write clean, readable code
- Follow existing code style
- Add comments where helpful
- Test your changes

#### 4. Test Locally
```bash
python manage.py runserver
# Test all affected features
```

#### 5. Commit & Push
```bash
git add .
git commit -m "Add: brief description of changes"
git push origin feature/your-feature-name
```

#### 6. Create Pull Request
- Go to your fork on GitHub
- Click "Pull Request"
- Describe what you changed and why
- Reference any related issues

## Code Style Guidelines

### Python
- Follow PEP 8 style guide
- Use meaningful variable names
- Keep functions focused and small
- Add docstrings to functions

### HTML/CSS
- Use consistent indentation (2 or 4 spaces)
- Keep templates readable
- Use Bootstrap classes when possible
- Test on mobile devices

### JavaScript
- Use ES6+ features
- Keep it simple and readable
- Add comments for complex logic

## Project Structure

```
HireMeNot/
├── roaster/              # Main Django app
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin interface
│   ├── utils/            # Utility functions
│   │   ├── api.py        # AI API calls
│   │   └── pdf_extractor.py  # PDF processing
│   └── templates/        # HTML templates
└── hiremenot/            # Django project settings
```

## What to Contribute

### 🌟 Priority Features
- [ ] Better error handling for edge cases
- [ ] More AI providers (Claude, Gemini, etc.)
- [ ] Resume tips alongside roasts
- [ ] Social media sharing improvements
- [ ] Mobile UI enhancements

### 🎨 Fun Ideas
- [ ] More Easter eggs and animations
- [ ] Custom roast styles (professional, savage, nice)
- [ ] Resume score system
- [ ] Meme templates with roast text
- [ ] Voice narration of roasts

### 🐛 Known Issues
- Check GitHub Issues for bugs to fix

## Testing

Before submitting:
1. ✅ Test your changes work as expected
2. ✅ Check for console errors
3. ✅ Test on different screen sizes
4. ✅ Ensure migrations run without errors
5. ✅ Test with and without API keys

## Questions?

- Open a GitHub Issue
- Tag it as "question"
- We're friendly, don't worry!

## Code of Conduct

- Be respectful and inclusive
- Keep feedback constructive
- Remember: we're here to have fun and learn
- The roasts are for resumes, not people 😄

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thanks for helping make HireMeNot even better! 🔥
