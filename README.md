# 🧠 Mani Shankar's Project Portfolio

Welcome to my **Data Science & Data Engineering Projects** repository!  
This repo serves as a collection of hands-on projects I’ve worked on across different domains including **cloud computing**, **data analytics**, **data engineering**, **machine learning**, and **software development**.

Each subfolder contains a self-contained project with code, data (if applicable), and documentation.

---

## 📂 Projects Overview

### 🎬 [Movie Analysis Using AWS & Tableau](./movie-analysis-aws-tableau)

A cloud-based data engineering project that leverages **AWS services** (S3, Glue, Athena, IAM) and **Tableau** for real-time movie data visualization.

- **Cloud Tools:** AWS S3, Glue, Athena, IAM
- **Visualization:** Tableau (connected to Athena)
- **Skills:** ETL, PySpark, Cloud Storage, SQL Analytics, Dashboarding

📄 [Project ReadMe](./movie-analysis-aws-tableau/README.md)

---

### 🎵 [Spotify Song Popularity Analysis](./spotify-popularity-analysis)

A data analysis project that investigates the **key audio features** influencing song popularity using **Spotify API** and regression techniques.

- **Tech:** Python, Spotipy, Pandas, Matplotlib, Seaborn
- **Key Analysis:** Correlation, Regression, Data Visualization
- **Dataset:** 18,000 tracks (Jan 2023 – Present)

📄 [Project ReadMe](./spotify-popularity-analysis/README.md)

---

### 🧠 [Parkinson's Disease Prediction System](./parkinsons-disease-prediction)

A machine learning and GUI-based project to predict **Parkinson's disease** using biomedical voice features. Includes a **Tkinter-based desktop app**.

- **Tech:** Python, Scikit-learn, Tkinter, XGBoost, SVM
- **Features:** Real-time predictions, full-screen GUI, CSV input
- **Use Case:** Healthcare and Medical Decision Support

📄 [Project ReadMe](./parkinsons-disease-prediction/README.md)

---

### 🔎 [Reddit Sentiment Analysis Using Python & PostgreSQL](./reddit-sentiment-analysis)

An end-to-end data engineering and analytics project that extracts Reddit posts using the **Reddit API**, performs **VADER sentiment analysis** (NLTK), and ingests the results into **PostgreSQL** for real-time dashboards.

- **Tech Stack:** Python, PRAW (Reddit API), NLTK (VADER), PostgreSQL, Tableau/Power BI
- **Focus Areas:** ETL, Scheduling (cron/Azure), CI/CD, Sentiment Analysis, Data Visualization
- **Dataset:** 50,000+ Reddit posts from chosen subreddits

📄 [Project ReadMe](./reddit-sentiment-analysis/README.md)

---

## 📁 Repo Structure
```bash
Projects:.
├───movie-analysis-aws-tableau
│   ├───data
│   ├───images
│   └───notebooks
├───parkinsons-disease-prediction
│   ├───assets
│   ├───data
│   ├───notebooks
│   └───src
├───reddit-sentiment-analysis
│   ├───analysis
│   ├───config
│   │   └───__pycache__
│   ├───data
│   │   ├───processed
│   │   └───raw
│   ├───db
│   │   └───migrations
│   ├───etl
│   └───visualization
│       └───dashboard_setup
└───spotify-popularity-analysis
```

---

## 🚀 How to Use This Repo

**1. Clone this repository:**
```bash
git clone https://github.com/ManiShankar6/Projects.git
cd Projects
```

**2. Navigate into any project folder to explore its content:**

```bash
cd movie-analysis-aws-tableau
```

**3. Follow the instructions in each project's README.md.**