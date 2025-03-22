# Project Repository Structure and Files

# 1. data_fetch.ipynb
#    Notebook that fetches track metadata and audio features from Spotify API.

# 2. EDA.ipynb
#    Exploratory Data Analysis notebook including descriptive stats, distribution plots, correlation, and regression analysis.

# 3. final_audio_features_dataset.csv
#    Final dataset combining track metadata and audio features (2023 to present).

# 4. README.md
#    Project overview, motivation, methodology, and conclusions.


# -------- README.md (in markdown format) --------

# Spotify Song Popularity Analysis

## 🎵 Objective
To understand the key audio features that influence a song's popularity on Spotify, using data extracted from the Spotify API and analyzing it through statistical, exploratory, and regression techniques.

## ❓ Research Question
**"What factors influence the popularity of songs on Spotify, and how can these factors be leveraged to improve song recommendations?"**

## 📊 Dataset Overview
We collected data for **18,000 songs** released between **January 2023 and present**, including:
- **Track Metadata**: Name, Artist, Track ID, Release Date, Popularity Score
- **Audio Features**: Danceability, Energy, Loudness, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, Duration

## ⚙️ Data Collection Process
- Used **Spotify API** with the `spotipy` Python library to extract metadata.
- Extracted audio features using manual API requests (bypassing Spotipy's `audio_features()` due to rate limits).
- Overcame **rate limiting (429 errors)** by chunking track IDs, rotating client credentials, and waiting strategically.

## 🧪 Analysis Conducted
1. **Descriptive Analysis**: Mean popularity score was 44.
2. **Distribution Plots**: Normal distributions for Danceability, Energy, and Tempo.
3. **Scatter Plots**:
   - Positive correlation: Danceability, Loudness → Popularity
   - Negative correlation: Instrumentalness, Valence → Popularity
4. **Correlation Heatmap**: Verified relationships between features.
5. **Regression Analysis**:
   - Significant predictors: Danceability (+), Loudness (+), Instrumentalness (−), Valence (−)
   - R² ≈ 0.14 → Suggests additional external factors influence popularity (e.g., artist fame).

## 🧠 Conclusion
- **Positive Impact**: Danceability, Loudness
- **Negative Impact**: Instrumentalness, Valence
- Recommendations can be improved by prioritizing high danceability/loudness and low instrumentalness/valence.

## 🔮 Future Work
- Integrate additional metadata (e.g., artist popularity, genre, playlist inclusion).
- Leverage ML models and clustering for mood/genre analysis.
- Incorporate user behavior and sentiment analysis.


## 📁 Files in This Repository
- `data_fetch.ipynb` → Spotify data extraction code
- `EDA.ipynb` → EDA and regression analysis
- `final_audio_features_dataset.csv` → Merged dataset used for analysis
- `README.md` → Project overview and documentation

---