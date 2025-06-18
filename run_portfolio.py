#!/usr/bin/env python3
"""
Portfolio Runner Script
Simple script to run the Abhishek Jha portfolio application
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import PIL
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def run_portfolio():
    """Run the portfolio application"""
    if not check_dependencies():
        return
    
    print("🚀 Starting Abhishek Jha's Portfolio...")
    print("📱 The application will open in your browser at: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        # Run the Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py", "--server.headless", "true"])
    except KeyboardInterrupt:
        print("\n👋 Portfolio stopped. Thanks for visiting!")
    except Exception as e:
        print(f"❌ Error running portfolio: {e}")

if __name__ == "__main__":
    run_portfolio() 