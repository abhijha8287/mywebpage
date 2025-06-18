import streamlit as st
import base64
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Abhishek Jha - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    
    .project-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    
    .skill-badge {
        background-color: #1f77b4;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.25rem;
        font-size: 0.9rem;
    }
    
    .contact-info {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .profile-section {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .profile-pic {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        border: 5px solid #1f77b4;
        margin: 0 auto 1rem auto;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
def main():
    st.sidebar.title("🚀 Navigation")
    
    # Create individual buttons for each section
    if st.sidebar.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"
    
    if st.sidebar.button("👤 About", use_container_width=True):
        st.session_state.page = "about"
    
    if st.sidebar.button("💼 Projects", use_container_width=True):
        st.session_state.page = "projects"
    
    if st.sidebar.button("🛠️ Skills", use_container_width=True):
        st.session_state.page = "skills"
    
    if st.sidebar.button("📄 Resume", use_container_width=True):
        st.session_state.page = "resume"
    
    if st.sidebar.button("📧 Contact", use_container_width=True):
        st.session_state.page = "contact"
    
    # Initialize session state if not exists
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    
    # Display the selected page
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "about":
        show_about()
    elif st.session_state.page == "projects":
        show_projects()
    elif st.session_state.page == "skills":
        show_skills()
    elif st.session_state.page == "resume":
        show_resume()
    elif st.session_state.page == "contact":
        show_contact()

def show_home():
    # Profile picture at the top - small and round
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Display user's profile picture in round shape
        try:
            image = Image.open("mypic.jpg")
            # Create a circular mask for the image
            st.markdown("""
            <style>
            .profile-pic-container {
                text-align: center;
                margin-bottom: 1rem;
            }
            .profile-pic {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                object-fit: cover;
                border: 3px solid #1f77b4;
                display: block;
                margin: 0 auto;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Convert PIL image to base64 for HTML display
            import base64
            from io import BytesIO
            
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            st.markdown(f"""
            <div class="profile-pic-container">
                <img src="data:image/jpeg;base64,{img_str}" class="profile-pic" alt="Abhishek Jha">
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error loading image: {e}")
            # Fallback to placeholder if image fails to load
            st.markdown("""
            <div class="profile-pic-container">
                <img src="https://via.placeholder.com/120x120/1f77b4/ffffff?text=AJ" 
                     class="profile-pic" alt="Abhishek Jha">
            </div>
            """, unsafe_allow_html=True)
    
    # Title and subtitle after the profile picture
    st.markdown('<h1 class="main-header">Abhishek Jha</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Data Science Student | Machine Learning Enthusiast | Streamlit Developer</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ## 👋 Welcome to My Portfolio!
    
    I'm a passionate Data Science student at **IIT Madras** with a strong foundation in Machine Learning and data-driven problem-solving. 
    I love building innovative applications using cutting-edge technologies and turning complex data into meaningful insights.
    
    ### 🎯 What I Do
    - **Machine Learning & AI**: Develop predictive models and intelligent systems
    - **Data Analysis**: Transform raw data into actionable insights
    - **Web Applications**: Build interactive Streamlit apps for real-world problems
    - **Natural Language Processing**: Create chatbots and text analysis tools
    
    ### 🚀 Quick Facts
    - 🎓 Currently pursuing B.S in Data Science and Applications at IIT Madras
    - 🔬 Passionate about Gen AI and LangChain applications
    - 📊 Expert in data visualization and storytelling
    - 💻 Skilled in Python, SQL, and modern ML frameworks
    
    """)

def show_about():
    st.markdown('<h1 class="section-header">👤 About Me</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🎓 Education
    **B.S in Data Science and Applications**  
    *IIT Madras, Chennai* | *Expected Graduation: September 2027*
    
    ---
    
    ## 🎯 Professional Profile
    
    I'm an enthusiastic Data Science student at IIT Madras with a strong passion for Machine Learning and data-driven problem-solving. 
    I actively develop my expertise through rigorous coursework and hands-on projects. I'm eager to collaborate on impactful initiatives 
    and connect with professionals to contribute to meaningful advancements in the field.
    
    ### 🔬 Research Interests
    - **Machine Learning & AI**: Developing predictive models and intelligent systems
    - **Natural Language Processing**: Building chatbots and text analysis applications
    - **Data Visualization**: Creating compelling stories from complex datasets
    - **Generative AI**: Exploring the latest developments in Gen AI technologies
    
    ### 🎯 Career Goals
    - Contribute to innovative AI/ML solutions that solve real-world problems
    - Develop expertise in cutting-edge technologies like LangChain and Gen AI
    - Build a strong network of professionals in the data science community
    - Create impactful applications that make a difference in people's lives
    """)

def show_projects():
    st.markdown('<h1 class="section-header">💼 Projects</h1>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Review Analysis App",
            "description": "A sophisticated sentiment analyzer that extracts pros, cons, themes, and comprehensive summaries from user reviews. Built with advanced NLP techniques to provide actionable insights from customer feedback.",
            "tech": ["Python", "Streamlit", "NLP", "Sentiment Analysis"],
            "link": "https://sentimentresponder.streamlit.app",
            "emoji": "📊"
        },
        {
            "title": "Detailed Summary Generator",
            "description": "Creates comprehensive reports on any topic and provides concise 5-line summaries. Perfect for research, content creation, and quick information extraction from complex subjects.",
            "tech": ["Python", "Streamlit", "LangChain", "Text Generation"],
            "link": "https://<your-app-url>",
            "emoji": "📝"
        },
        {
            "title": "5 Facts Generator",
            "description": "Generates 5 factual statements about any user-defined topic using structured output parsing. Ensures accuracy and relevance while providing educational content in an engaging format.",
            "tech": ["Python", "Streamlit", "Structured Output", "API Integration"],
            "link": "https://5factgeneratorbyabhishek.streamlit.app",
            "emoji": "🔍"
        },
        {
            "title": "Learn and Test Yourself",
            "description": "An educational platform that generates comprehensive notes and quiz questions from any topic, then merges both into an interactive study guide for effective learning.",
            "tech": ["Python", "Streamlit", "Education Tech", "Quiz Generation"],
            "link": "https://learntestyourself.streamlit.app",
            "emoji": "🎓"
        },
        {
            "title": "Post Generator",
            "description": "Creates engaging Tweet and LinkedIn posts from any given topic using parallel LangChain chains. Optimized for social media engagement and professional networking.",
            "tech": ["Python", "Streamlit", "LangChain", "Social Media"],
            "link": "https://postgeneratorbyabhishek.streamlit.app",
            "emoji": "📱"
        },
        {
            "title": "Joke Generator",
            "description": "Generates contextually relevant jokes based on user topics and explains the humor behind each joke, making it both entertaining and educational.",
            "tech": ["Python", "Streamlit", "Humor Analysis", "NLP"],
            "link": "https://jokegeneratorbyabhishek.streamlit.app",
            "emoji": "😄"
        }
    ]
    
    for project in projects:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <div class="project-title">{project['emoji']} {project['title']}</div>
                <p>{project['description']}</p>
                <p><strong>Technologies:</strong> {', '.join(project['tech'])}</p>
                <a href="{project['link']}" target="_blank" style="color: #1f77b4; text-decoration: none;">
                    🔗 Live Demo
                </a>
            </div>
            """, unsafe_allow_html=True)

def show_skills():
    st.markdown('<h1 class="section-header">🛠️ Skills & Technologies</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💻 Programming Languages")
        skills = ["Python", "HTML", "CSS", "SQL"]
        for skill in skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("### 📊 Data Science & ML")
        skills = ["NumPy", "Pandas", "Matplotlib", "Seaborn", "Machine Learning Algorithms", "Feature Engineering", "Exploratory Data Analysis"]
        for skill in skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🤖 AI & Advanced Technologies")
        skills = ["LangChain", "Gen AI", "Natural Language Processing", "Sentiment Analysis"]
        for skill in skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("### 🛠️ Tools & Platforms")
        skills = ["Streamlit", "Git & GitHub", "MS Excel", "MySQL", "PostgreSQL"]
        for skill in skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Core Competencies")
    competencies = [
        "Data Visualization and Storytelling",
        "Machine Learning Model Development",
        "Web Application Development",
        "Database Management",
        "API Integration",
        "Project Management",
        "Problem Solving",
        "Team Collaboration"
    ]
    
    for comp in competencies:
        st.markdown(f"✅ {comp}")

def show_resume():
    st.markdown('<h1 class="section-header">📄 Resume</h1>', unsafe_allow_html=True)
    
    # Display resume content in a structured format
    st.markdown("""
    ## 📋 Professional Summary
    
    Enthusiastic Data Science student at IIT Madras with a strong passion for Machine Learning and data-driven problem-solving. 
    Actively developing expertise through rigorous coursework and hands-on projects. Eager to collaborate on impactful initiatives 
    and connect with professionals to contribute to meaningful advancements in the field.
    
    ---
    
    ## 🎓 Education
    
    **B.S in Data Science and Applications**  
    *IIT Madras, Chennai* | *Expected Graduation: September 2027*
    
    ---
    
    ## 💼 Technical Projects
    
    ### AI & Machine Learning Projects
    - **Career Guidance Chat Bot using LangChain** - Intelligent career counseling system
    - **Ed-Tech Chatbot using LangChain** - Educational assistance platform
    - **Healthcare Premium Prediction (Regression)** - ML model for insurance pricing
    - **Credit Risk Modelling (Classification)** - Financial risk assessment system
    
    ### Data Analysis Projects
    - **AtliQ Bank – Data Analysis** - Comprehensive banking data insights
    - **Hospitality Domain Data Analytics** - Industry-specific analysis
    - **Unemployment Analysis with Python** - Economic trend analysis
    - **Car Price Prediction with Machine Learning** - Automotive market analysis
    - **Sales Prediction using Python** - Business forecasting model
    
    ---
    
    ## 🛠️ Technical Skills
    
    ### Programming & Data Science
    - **Python** and Libraries: NumPy, Pandas, Matplotlib, Seaborn
    - **Machine Learning Algorithms** and implementation
    - **Feature Engineering & Selection** techniques
    - **Exploratory Data Analysis** methodologies
    
    ### AI & Advanced Technologies
    - **LangChain** for AI application development
    - **Gen AI** technologies and applications
    - **Natural Language Processing** and text analysis
    
    ### Tools & Databases
    - **MS Excel** for data manipulation and analysis
    - **SQL** and **MySQL** for database management
    - **PostgreSQL** for advanced database operations
    - **Git & GitHub** for version control and collaboration
    
    ### Web Technologies
    - **HTML, CSS** for web development
    - **Streamlit** for rapid application development
    
    ---
    
    ## 🎯 Interests & Specializations
    
    - **Data Visualization and Storytelling with Data**
    - **Generative AI** and its applications
    - **Machine Learning** model optimization
    - **Real-world problem solving** through data science
    """)
    
    # Add download button for resume
    st.markdown("---")
    st.markdown("### 📥 Download Resume")
    with open("resume.pdf", "rb") as file:
        pdf_data = file.read()
    
    st.download_button(
        label="📄 Download PDF Resume",
        data=pdf_data,
        file_name="Abhishek_Jha_Resume.pdf",
        mime="application/pdf"
    )

def show_contact():
    st.markdown('<h1 class="section-header">📧 Contact Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📍 Location")
        st.markdown("""
        <div class="contact-info">
            <strong>Address:</strong><br>
            M-122, Mohan Garden, Uttam Nagar<br>
            New Delhi 110059, India
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📞 Phone")
        st.markdown("""
        <div class="contact-info">
            <strong>Mobile:</strong><br>
            +91 8287706259
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📧 Email")
        st.markdown("""
        <div class="contact-info">
            <strong>Personal:</strong><br>
            abhijha8287@gmail.com
        </div>
        <div class="contact-info">
            <strong>Academic:</strong><br>
            23f3004013@ds.study.iitm.ac.in
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔗 Social Links")
        st.markdown("""
        <div class="contact-info">
            <strong>LinkedIn:</strong><br>
            <a href="https://www.linkedin.com/in/abhishekjha15" target="_blank">
                linkedin.com/in/abhishekjha15
            </a>
        </div>
        <div class="contact-info">
            <strong>GitHub:</strong><br>
            <a href="https://www.github.com/abhijha8287" target="_blank">
                github.com/abhijha8287
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 💬 Let's Connect!")
    st.markdown("""
    I'm always excited to connect with fellow data scientists, developers, and professionals! 
    Whether you want to discuss potential collaborations, share insights, or just say hello, 
    feel free to reach out through any of the channels above.
    
    **I'm particularly interested in:**
    - 🤝 Collaboration opportunities in AI/ML projects
    - 💼 Internship and job opportunities in Data Science
    - 🎓 Academic research partnerships
    - 🚀 Startup and innovation discussions
    """)

if __name__ == "__main__":
    main() 