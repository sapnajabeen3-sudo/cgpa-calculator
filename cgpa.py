import streamlit as st

st.set_page_config(page_title="SEMESTER GPA CALCULATOR", page_icon="🎓", layout="wide")

# YE 3 QUOTES IMPORTANT HAIN - INKE ANDAR HI CSS LIKHNA HAI
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Times+New+Roman&display=swap');

html, body, [class*="st"] {
    font-family: 'Times New Roman', serif!important;
}

.stApp {
    background-image: linear-gradient(rgba(10, 25, 80, 0.85), rgba(10, 25, 80, 0.85)), url("https://img.freepik.com/free-vector/dark-blue-low-poly-geometric-background_1035-18315.jpg");
    background-size: cover;
    background-attachment: fixed;
}

h1, h2, h3, p, label {
    color: white!important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'> 4th Semester</h1>", unsafe_allow_html=True)

# Baaki tumhara subject wala code yahan likhna
st.write("SEMESTER GPA CALCULATOR")
tab1, tab2 = st.tabs(["📝 GPA Calculator", "📊 Performance Chart"])

with tab1:
    st.subheader("SEMESTER GPA CALCULATOR")

    subjects = {
        "Artificial Intelligence Theory": 2,
        "Operating System Theory": 2,
        "Computer Networking": 3,
        "Probability & Statistics": 3,
        "Software Engineering": 3,
        "Civics": 2,
        "AI Lab": 1,
        "OS Lab": 1,
        "CN Lab": 1
    }

    grades_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

    total_points = 0
    total_credits = 0
    student_data = []

    for subj, default_credit in subjects.items():
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{subj}**")
        with col2:
            credit = st.number_input(f"Credits_{subj}", min_value=1, max_value=5, value=default_credit, label_visibility="collapsed", key=subj+"_c")
        with col3:
            grade = st.selectbox(f"Grade_{subj}", list(grades_points.keys()), label_visibility="collapsed", key=subj+"_g")

        points = grades_points[grade] * credit
        total_points += points
        total_credits += credit
        student_data.append({"Subject": subj, "Credits": credit, "Grade": grade, "Points": points})

    if st.button("🔥 Calculate GPA", use_container_width=True, type="primary"):
        gpa = total_points / total_credits if total_credits > 0 else 0
        col1, col2, col3 = st.columns(3)
        col1.metric("Current GPA", f"{gpa:.2f} / 4.00")
        col2.metric("Total Credits", total_credits)
        col3.metric("Total Points", f"{total_points:.1f}")
        st.session_state['student_data'] = student_data
        st.success("✅ GPA Calculated Successfully!")

with tab2:
    st.subheader("📊 Your Performance Chart")
    if 'student_data' in st.session_state:
        import pandas as pd
        df = pd.DataFrame(st.session_state['student_data'])
        st.bar_chart(df.set_index('Subject')['Points'])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("👆 Pehle 'Calculate GPA' dabao taake chart ban sake")