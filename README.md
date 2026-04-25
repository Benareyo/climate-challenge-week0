# 🌍 Climate Data Analyzer (Week 0 Challenge)

## 📌 Project Overview

The **Climate Data Analyzer** is a Python + Streamlit project that allows users to upload and analyze simple climate datasets (temperature and humidity).

It is part of the **African Climate Trend Analysis Challenge**, which introduces data engineering and exploratory data analysis (EDA) concepts using real-world climate thinking.

---

## 🎯 Objectives

This project helps to:
- Load and explore CSV climate data
- Select and filter columns dynamically
- Visualize relationships between variables
- Compute simple statistical insights
- Build an interactive dashboard using Streamlit

---

## 🚀 Features

✔ Upload CSV file  
✔ Preview dataset  
✔ Select temperature and humidity columns  
✔ Filter data using temperature slider  
✔ Temperature distribution plot  
✔ Temperature vs humidity scatter plot  
✔ Correlation analysis  
✔ Simple interpretation messages  

---

## 🧰 Tech Stack

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Project Structure

climate-challenge-week0/

├── app.py                  # Main Streamlit app  
├── requirements.txt        # Project dependencies  
├── README.md               # Documentation  

├── src/  
│   ├── visualizer.py       # Plot functions  
│   ├── data_loader.py      # Data loading logic  

├── scripts/  
│   └── run_analysis.py     # CLI runner script  

├── tests/  
└── notebooks/  

---

## ▶️ How to Run

### 1. Clone repo
git clone https://github.com/Benareyo/climate-challenge-week0.git  
cd climate-challenge-week0  

---

### 2. Create virtual environment
python -m venv venv  
venv\Scripts\activate  

---

### 3. Install dependencies
pip install -r requirements.txt  

---

### 4. Run app
streamlit run app.py  

---

## 📊 Sample CSV Format

temp,humidity  
30,60  
32,65  
28,55  

---

## 🧠 What the App Does

- Shows dataset preview  
- Lets you choose columns dynamically  
- Filters data based on temperature  
- Plots:
  - Temperature distribution
  - Temperature vs humidity relationship  
- Calculates correlation between variables  

---

## 🚧 Future Improvements

- Add real African climate dataset (Task 2)  
- Add multi-country comparison  
- Improve dashboard design  
- Add time-series analysis  
- Deploy to Streamlit Cloud  

---

## 👨‍💻 Author

Built as part of the **African Climate Trend Analysis Week 0 Challenge**

Focus:
- Data Engineering basics  
- EDA (Exploratory Data Analysis)  
- Git & GitHub workflow  
- Streamlit dashboard development  

---

## 📌 Status

✔ Git setup complete  
✔ Streamlit app working  
✔ Basic analysis implemented  
🔜 Moving to Task 2 (real climate data analysis)