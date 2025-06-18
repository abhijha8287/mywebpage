@echo off
echo 🚀 Starting Abhishek Jha's Portfolio...
echo.
echo 📱 The application will open in your browser at: http://localhost:8501
echo ⏹️  Press Ctrl+C to stop the application
echo.
echo ----------------------------------------
echo.

python -m streamlit run app.py --server.headless true

pause 