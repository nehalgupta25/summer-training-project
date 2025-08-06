# 🎧 Most Streamed Spotify Songs 2024

This project analyzes the most-streamed songs on Spotify using **Python for data cleaning** and **Power BI for visualization**.

## 📊 Project Objective
To explore music streaming trends by analyzing a real dataset from Spotify and presenting the findings through a visually interactive dashboard.

## 📦 Dataset
- **Source**: [Kaggle – Most Streamed Spotify Songs 2024](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024) 
- **Fields include**:  
  - Track  
  - Artist  
  - Album
  - All Time Rank
  - Track score
  - Release date  
  - Popularity score  
  - Playlist reach
  - Playlist count
  - Explicit Track
  - Stream   

## 🛠️ Tools & Technologies
- **Python**:  
  - `pandas` – data cleaning, filtering, and transformation  
  - `numpy` – numerical operations  
  - `matplotlib` & `seaborn` – basic visualization during testing

- **Power BI**:  
  - Dashboard creation  
  - DAX measures

## 🧹 Data Cleaning Steps
Using Python (Pandas), we performed:
- Null value checks and replacements
- Renamed inconsistent column headers
- Removed duplicates
- Changed datatypes where required
- Exported the cleaned dataset to CSV

## 📈 Dashboard Highlights (Power BI)
The dashboard includes:
- 📌 **KPI Cards** for total streams, total artists, total tracks, and average popularity  
- 📊 **Bar Chart** showing top artists by stream count  
- 📈 **Line Chart** to visualize streaming trends by year  
- 🍩 **Donut Charts** for popularity groupings and explicit/clean track ratios  
- 🧠 **Custom DAX measures** for Monthly Streams, MoM Growth %, and more  
- 🎛️ **Gauge Chart** to show total streams and popularity group

## 👨‍💻 Contributors
- **Nehal Gupta** (Group Leader)  
- Madhu  
- Omika  
- Riya Sehgal  

## 👨‍🏫 Faculty Guide
- **Divyank Chauhan Sir**

## 📂 Folder Structure
- `cleaned_dataset.csv` – final data used in Power BI  
- `spotify_dashboard.pbix` – Power BI report file  
- `data_cleaning.py` – Python script used for preprocessing  
- `dashboard_view.png` – dashboard screenshot  
- `README.md` – project summary

## 📬 Contact
Feel free to reach out via ([https://www.linkedin.com/in/nehal-gupta-6610b8288/]) 


## 🔖 License
This project is for academic and learning purposes only.
