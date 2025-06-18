# 🚀 Abhishek Jha - Personal Portfolio

A beautiful, modern personal portfolio website built with Streamlit showcasing my skills, projects, and experience in Data Science and Machine Learning.

## ✨ Features

- **🏠 Home**: Welcome page with introduction and quick facts
- **👤 About**: Detailed information about education, background, and career goals
- **💼 Projects**: Showcase of 6 impressive Streamlit applications with live demos
- **🛠️ Skills**: Comprehensive display of technical skills and competencies
- **📄 Resume**: Structured resume view with downloadable PDF
- **📧 Contact**: Contact information and social links

## 🎨 Design Highlights

- **Modern UI**: Clean, professional design with custom CSS styling
- **Responsive**: Mobile-friendly layout that works on all devices
- **Interactive**: Smooth navigation with sidebar menu
- **Visual Appeal**: Beautiful color scheme, emojis, and engaging content
- **Professional**: Perfect for job applications and networking

## 🛠️ Technologies Used

- **Streamlit**: Main framework for the web application
- **Python**: Backend programming language
- **HTML/CSS**: Custom styling and layout
- **Pillow**: Image processing capabilities

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download
```bash
# If using git
git clone <repository-url>
cd portfolio-website

# Or simply download the files to your local machine
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run app.py
```

### Step 4: Access the Portfolio
Open your web browser and navigate to:
```
http://localhost:8501
```

## 📁 Project Structure

```
portfolio-website/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── resume.pdf         # Resume file (your actual resume)
└── resume.txt         # Text version of resume (auto-generated)
```

## 🚀 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. **Push to GitHub**: Upload your code to a GitHub repository
2. **Connect to Streamlit Cloud**: 
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and set the main file path to `app.py`
   - Click "Deploy"

### Alternative Deployment Options

- **Heroku**: Use the Streamlit buildpack
- **AWS/GCP**: Deploy using Docker containers
- **Local Server**: Run on your own server with proper configuration

## 🎯 Customization

### Personal Information
Edit the following sections in `app.py`:
- Personal details in the `show_contact()` function
- Education information in `show_about()`
- Skills and competencies in `show_skills()`

### Projects
Update the `projects` list in the `show_projects()` function:
```python
projects = [
    {
        "title": "Your Project Title",
        "description": "Project description...",
        "tech": ["Technology1", "Technology2"],
        "link": "https://your-app-url.com",
        "emoji": "🎯"
    },
    # Add more projects...
]
```

### Styling
Modify the CSS in the `st.markdown()` section to change:
- Colors and themes
- Font sizes and styles
- Layout and spacing
- Component styling

## 📊 Featured Projects

1. **Review Analysis App** - Sentiment analysis and review insights
2. **Detailed Summary Generator** - AI-powered content summarization
3. **5 Facts Generator** - Educational fact generation
4. **Learn and Test Yourself** - Interactive learning platform
5. **Post Generator** - Social media content creation
6. **Joke Generator** - AI-powered humor generation

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

- **Email**: abhijha8287@gmail.com
- **LinkedIn**: [linkedin.com/in/abhishekjha15](https://linkedin.com/in/abhishekjha15)
- **GitHub**: [github.com/abhijha8287](https://github.com/abhijha8287)

---

⭐ **Star this repository if you found it helpful!** 