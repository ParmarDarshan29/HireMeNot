#!/bin/bash

# HireMeNot Setup Script
# This script automates the initial setup process

echo "🔥 HireMeNot Setup Script 🔥"
echo "=============================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
echo "✅ Virtual environment created"
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt --quiet
echo "✅ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "⚙️  Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created (please edit it with your API keys)"
else
    echo "⚠️  .env file already exists, skipping..."
fi
echo ""

# Run migrations
echo "🗄️  Running database migrations..."
python3 manage.py migrate
echo "✅ Database migrations complete"
echo ""

# Ask if user wants to create superuser
echo "👤 Do you want to create an admin superuser? (y/n)"
read -r create_superuser

if [ "$create_superuser" = "y" ] || [ "$create_superuser" = "Y" ]; then
    echo "Creating superuser..."
    python3 manage.py createsuperuser
    echo ""
fi

# Final instructions
echo ""
echo "=============================="
echo "✨ Setup Complete! ✨"
echo "=============================="
echo ""
echo "📝 Next Steps:"
echo ""
echo "1. Edit the .env file with your API keys:"
echo "   - For OpenRouter: Add OPENROUTER_API_KEY"
echo "   - For Local AI: Set USE_LOCAL_AI=true and install Ollama"
echo ""
echo "2. Start the development server:"
echo "   python3 manage.py runserver"
echo ""
echo "3. Open your browser to:"
echo "   http://localhost:8000"
echo ""
echo "4. Upload a resume and watch it get roasted! 🔥"
echo ""
echo "📚 For more info, check out:"
echo "   - README.md (full documentation)"
echo "   - QUICKSTART.md (quick start guide)"
echo "   - sample_resume.txt (test resume)"
echo ""
echo "Happy roasting! 😎"
