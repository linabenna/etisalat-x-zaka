import streamlit as st

st.set_page_config(page_title="KURVE - Computer Science", layout="wide")

# Inject CSS to style Streamlit like your HTML design
st.markdown("""
    <style>
    * {
      box-sizing: border-box;
    }

    html, body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      color: #333;
      overflow-x: hidden;
    }

    .title {
      font-size: 32px;
      font-weight: 600;
      margin: 30px 40px 10px;
      padding: 40px 40px 30px;
    }

    .sidebar-button {
      width: 100%;
      padding: 10px 12px;
      border: 1px solid #e0e0e0;
      text-align: left;
      font-size: 14px;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      cursor: pointer;
      transition: background-color 0.2s, transform 0.1s;
      margin-bottom: 10px;
    }

    .sidebar-button:hover {
    }

    .question-box {
      padding: 20px;
      border-radius: 10px;
      font-weight: 600;
      margin-bottom: 20px;
    }

    .header {
      padding: 15px 40px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      position: sticky;
      top: 0;
      z-index: 1000;
    }

    .header h1 {
      color: #3b82f6;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .nav {
      display: flex;
      gap: 20px;
    }

    .nav a {
      text-decoration: none;
      color: #555;
      font-weight: 500;
    }

    .nav a:hover {
      color: #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
  <h1><img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='30'/> KURVE</h1>
  <div class="nav">
    <a href="#">Home</a>
    <a href="#">Subjects ▾</a>
    <a href="#">Login</a>
  </div>
</div>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>Computer Science</div>", unsafe_allow_html=True)

# Questions
questions = [
    "Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.",
    "Explain quicksort algorithm.",
    "Define polymorphism.",
    "What is a pointer?",
    "Describe Dijkstra’s algorithm.",
    "What is the OSI model?",
    "Explain recursion.",
    "What is a hash table?",
    "Define Big O notation.",
    "What is a linked list?",
    "Describe virtual memory.",
    "What is inheritance?"
]

# Layout
col1, col2, col3 = st.columns([1, 4, 1])

# Sidebar (Question Buttons)
with col1:
    selected = st.radio("Questions", [f"Q{i+1}" for i in range(len(questions))], label_visibility="collapsed")

# Main Display Area
with col2:
    index = int(selected[1:]) - 1
    st.markdown(f"<div class='question-box'>{questions[index]}</div>", unsafe_allow_html=True)
    st.text_area("Submit your solution", height=150)

# Control Buttons
with col3:
    st.button("?", help="Help")
    st.button("C", help="Clear")

