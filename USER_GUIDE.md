# 📖 HireMeNot User Guide

Welcome to HireMeNot! This guide will help you get the most out of your resume roasting experience. 🔥

## 🎯 What is HireMeNot?

HireMeNot is a fun web application that uses AI to humorously "roast" your resume. Think of it as a friendly comedian pointing out all the clichés, buzzwords, and exaggerations in your resume – but in a way that's actually helpful (and hilarious)!

## 🚀 Getting Started

### Step 1: Access the Website

Open your browser and navigate to:
- **Local**: `http://localhost:8000`
- **Production**: `https://your-domain.com`

You'll see the homepage with:
- The HireMeNot logo with fire emoji 🔥
- Tagline: "Where Resumes Go to Die"
- Upload form

### Step 2: Prepare Your Resume

You have two options:

#### Option A: Upload PDF
1. Have your resume saved as a PDF file
2. File should be under 5MB
3. Must contain extractable text (not images)

#### Option B: Paste Text
1. Open your resume
2. Copy all the text
3. Ready to paste!

### Step 3: Submit Your Resume

#### Using PDF Upload:
1. Click the "📄 Upload PDF" tab
2. Click "Choose your resume (PDF only)"
3. Select your PDF file
4. Click "🔥 Roast My Resume! 🔥"

#### Using Text Input:
1. Click the "✍️ Paste Text" tab
2. Paste your resume text in the text area
3. Click "🔥 Roast My Resume! 🔥"

### Step 4: Wait for the Roast

- The AI is analyzing your resume
- This usually takes 5-15 seconds
- Be patient – good roasts take time! 😎

### Step 5: View Your Roast

You'll be redirected to the results page showing:

#### The Roast
- AI-generated humorous critique
- Witty observations about your resume
- Points out clichés and buzzwords
- Sarcastic but friendly tone

#### Visual Elements
- "REJECTED!" stamp animation
- Random meme/GIF (if Giphy is configured)
- Timestamp of when roasted
- Fire emoji borders 🔥

#### Action Buttons
- **🔄 Roast Again**: Generate a new roast for same resume
- **👍 Upvote**: Like this roast (helps leaderboard)
- **🐦 Share**: Share on Twitter/X
- **🏠 Home**: Return to homepage

#### Additional Features
- **View Original Resume**: Click to expand and see your original text
- **Fun Fact**: Random interesting tidbit about resumes

## 📊 Leaderboard

### What Is It?
A ranking of the funniest roasts based on upvotes from the community.

### How to Access
- Click "Leaderboard 🏆" in the navigation bar
- Or navigate to `/leaderboard/`

### Features
- Top 10 roasts displayed
- Medal icons for top 3 (🥇🥈🥉)
- Preview of each roast
- Upvote count
- Link to full roast
- Upvote button for each roast

### How to Get on Leaderboard
1. Get roasted
2. Share your roast link
3. Get people to upvote
4. Climb the ranks!

## 🎮 Hidden Features & Easter Eggs

### Konami Code
Type: ↑ ↑ ↓ ↓ ← → ← → B A

Effect: Extra animation on results page!

### Hover Effects
- Hover over cards for lift animation
- Hover over buttons for glow effect
- Interactive UI elements throughout

### Stamp Animation
- Watch the "REJECTED!" stamp appear
- Animated entrance on results page
- Rotated for authentic feel

## 💡 Tips for Best Results

### Resume Quality
- Longer resumes = better roasts
- Include typical buzzwords for more humor
- Real content works better than gibberish

### Text Length
- Minimum: 50 characters
- Maximum: 10,000 characters
- Sweet spot: 500-2000 characters

### What Makes a Good Roast
The AI roasts:
- Overused buzzwords ("synergy", "leverage", "proactive")
- Vague descriptions
- Excessive jargon
- Exaggerations
- Generic skills ("team player", "hard worker")

## 🔧 Troubleshooting

### "Please upload a PDF file"
- Make sure file extension is `.pdf`
- Not `.doc`, `.docx`, or other formats

### "No text could be extracted"
- Your PDF might be image-based
- Try copying text and using "Paste Text" option
- Or convert PDF to searchable PDF first

### "Resume is too short"
- Minimum 50 characters required
- Add more content or use a fuller resume

### "Resume is too long"
- Maximum 10,000 characters
- Trim down or submit in sections

### "Failed to generate roast"
- API might be unavailable
- Check your internet connection
- Try again in a moment
- If persists, contact admin

### Slow Loading
- AI processing takes time
- Typical wait: 5-15 seconds
- Longer resumes take longer
- Be patient!

## 🎨 UI Overview

### Homepage
- **Header**: HireMeNot logo with navigation
- **Hero Section**: Title and tagline
- **Upload Form**: Tabbed interface (PDF/Text)
- **Info Cards**: Three feature highlights
- **Footer**: Tagline and disclaimer

### Results Page
- **Header**: "You've Been Roasted!"
- **Roast Box**: Bordered box with roast text
- **Meme Section**: Random funny GIF
- **Action Buttons**: 4 main actions
- **Resume Preview**: Collapsible original text
- **Fun Fact**: Interesting information

### Leaderboard
- **Header**: Trophy emoji and title
- **Roast Cards**: Ranked list of top roasts
- **Medal Icons**: Visual ranking (top 3)
- **Upvote Buttons**: Interactive voting
- **Back Button**: Return to home

## 🌈 Theme & Design

### Colors
- **Background**: Dark gradient (navy/black)
- **Accent**: Fire gradient (orange to pink)
- **Text**: Light gray on dark background
- **Buttons**: Gradient with hover effects

### Fonts
- **Main**: Poppins (Google Fonts)
- **Weights**: 300 (light), 400 (regular), 600 (semibold), 700 (bold)

### Animations
- Fire emoji flicker
- Card hover lifts
- Button glows
- Stamp rotation
- Border glow pulse
- Fade-in transitions

## 📱 Mobile Usage

### Responsive Design
- Works on all screen sizes
- Optimized for phones & tablets
- Touch-friendly buttons
- Readable text sizes

### Mobile Tips
- Use portrait orientation
- Tap navigation burger menu (☰)
- Use "Paste Text" for easier input
- Scroll to see full roast

## 🔐 Privacy & Data

### What We Store
- Resume text
- Generated roast
- Timestamp
- Upvote count

### What We DON'T Store
- Your name (unless in resume text)
- Email address
- IP address
- Personal identifiers

### Data Usage
- Used only for roast generation
- Visible on leaderboard (if upvoted)
- Not shared with third parties
- Stored in local database

## ⚙️ Settings & Configuration

### AI Provider (Admin Only)
- **OpenRouter**: Cloud-based AI
- **Ollama**: Local AI (free)
- Configured via `.env` file

### API Keys (Admin Only)
- **OpenRouter**: For cloud AI
- **Giphy**: For memes (optional)
- Set in environment variables

## 🎓 Understanding Your Roast

### What to Look For

#### Buzzword Callouts
AI will mock overused terms like:
- "Synergy"
- "Leverage"
- "Proactive"
- "Think outside the box"
- "Self-starter"

#### Vague Descriptions
AI notices when you're not specific:
- "Managed projects" (what kind?)
- "Increased efficiency" (by how much?)
- "Strong communication skills" (prove it!)

#### Generic Skills
AI roasts common fillers:
- "Microsoft Office expert" (who isn't?)
- "Team player" (groundbreaking!)
- "Hard worker" (said everyone ever)

### How to Improve

The roast is funny, but hints at real issues:

1. **Be Specific**: Use numbers and details
2. **Show Results**: Quantify achievements
3. **Avoid Clichés**: Use original language
4. **Prove Claims**: Back up with examples
5. **Be Unique**: Stand out from the crowd

## 🤝 Sharing & Social

### Share on Twitter/X
1. Click "🐦 Share" button
2. Opens Twitter with pre-filled text
3. Edit message if desired
4. Tweet to share your roast!

### Get Upvotes
1. Share your roast link with friends
2. Ask them to upvote
3. Climb the leaderboard
4. Achieve internet fame! 🌟

## ❓ FAQ

### Is this serious?
No! It's for fun. But the feedback might actually help! 😏

### Will this improve my resume?
Maybe! The AI points out real issues, just with humor.

### Can I roast multiple resumes?
Yes! Upload as many as you want.

### How does the AI work?
It uses language models trained on internet text to generate humorous critiques.

### Is my data safe?
Yes! We only store what's needed. No personal tracking.

### Can I delete my roast?
Contact admin if you need a roast removed.

### What if the roast is too mean?
It's meant to be funny, not hurtful. If you're offended, remember it's just AI humor!

### Can I customize the roast style?
Not currently, but it's a planned feature!

### Is this free?
Yes! Though it uses APIs that may have costs/limits.

## 📞 Support

### Having Issues?
1. Check troubleshooting section above
2. Review the README.md
3. Check GitHub Issues
4. Contact the admin

### Want to Contribute?
- See CONTRIBUTING.md
- Submit bug reports
- Suggest features
- Share feedback!

## 🎉 Have Fun!

Remember:
- This is satire and entertainment
- Don't take it too seriously
- But maybe take the advice seriously? 😉
- Share funny roasts with friends
- Upvote the best ones!

---

**Ready to get roasted? Let's go! 🔥**

© HireMeNot — We roast so you improve. 💼🔥
