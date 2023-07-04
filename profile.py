from pathlib import Path
import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profiepic.png"


PAGE_TITLE = "Digital CV | KORUPURI JYOTHIRMAI"
PAGE_ICON = "🧖‍♀️"
NAME = "KORUPURI JYOTHIRMAI"
DESCRIPTION = """
Data Scientist
"""
EMAIL = "kurupurijyothirmai2000@gmail.com"
SOCIAL_MEDIA = {
    "linkedin":"LinkedIn: http://www.linkedin.com/in/korupuri-jyothirmai-211704256",
    "Github":"GitHub: https://github.com/Korupuri-Jyothirmai",
    "Kaggle":"Kaggle: https://www.kaggle.com/korupurijyothirmai"
}
PROJECTS = {
    """🏆 WEB BASED SERIVCE TO MONITOR AUTOMATIC IRRIGATION SYSTEM FOR AGRICULTURE USING SENSORS. I have done this project during my academics. """:'.',
 
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.image(profile_pic, width=230,caption='K JYOTHIRMAI')

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- QUALIFICATIONS ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Qulifications")
st.write(
    """
- \t\t✔️ XII: Sri Chaitanya Juniour Collage \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCGPA: 8.7, YOP: 2018
- \t\t✔️ UG: Bonam Venkata Chalamayya Collage of Engineering- JNTUK\t\t\t\t\tCGPA: 8.00, YOP: 2022.
- \t\t✔️ PGP: Post Graduation Program in Computational Datascience (upGrad INSOFE)\t\t\t\t\t\t\t\tDuration: May 2022–April 2023
- Excellent team player and displaying a strong sense of initiative on tasks
- Strong communication and presentation skills
"""
)


# --- SKILLS ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
-	👩‍💻Programming: Python (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn), C, SQL
-	📊Data Analysis: Data Cleaning, Statistical Modeling, Data Visualization 
-	💻Machine Learning: Supervised learning, Unsupervised learning
-	🧿Deep Learning: ANN, CNN, RNN, [CV, NLP]
-     Bigdata:Hadoop,Spark.
-	🪄Tools: My SQL, Git, Docker, Excel, Tableau
-   ⚙️OS: Windows, Linux
-   ☁️cloud services: AZURE
"""
)


# --- Compititions---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Competitions")
st.write("---")

# --- JOB 3
st.write('\n')
st.write("🚧","[Regression with a Tabular Paris Housing Price Dataset] | Kaggle competition – Playground Series 3 Episode 6")

st.write(
    """
- ► Purpose: To predict the price of houses in Paris
- ► Conducted data cleaning and pre-processing along with visualization
- ► Analyzed various attributes (house features) and their relation with target (house price)
- ► Constructed various machine learning regression models
"""
)


# --- JOB 1
st.write("🚧", """**[Binary Classification with a Tabular Credit Card Fraud Dataset]** | Kaggle competition – Playground Series 3 Episode 4""")
st.write("[Rank: 343th of 678 | Top 51%](https://www.kaggle.com/competitions/playground-series-s3e4)")
st.write(
    """
- ► Purpose: To predict whether a credit card transaction is fraudulent or not
- ► Handled severely imbalanced data and built various supervised machine learning classification algorithms
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", """[Ordinal Regression with a Tabular Wine Quality Dataset] | Kaggle competition – Playground Series 3 Episode 5""")
st.write("[Rank: 293rd of 901 | Top 33%](https://www.kaggle.com/competitions/playground-series-s3e5)")
st.write(
    """
- ► Purpose: To predict the Wine Quality
- ► Conducted data cleaning and pre-processing along with visualization
- ► Feature Engineering of chemical properties to reduce dimensions of data
- ► Constructed various machine learning classification models
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Projects and Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- Hobbies ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Hobbies and Interests")
st.write("---")
st.write("""
- Badminton 🏸
- Programming 💻
- handcraft🪡🧶
    """)
