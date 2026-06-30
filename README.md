# Sonar Rock vs Mine Detector

Flask-based web app jo sonar signal data se predict karta hai ki underwater object rock hai ya mine.

## Tech Stack
- Model Training: Google Colab, scikit-learn
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- Deployment: Render

## How it works
1. Sonar dataset (60 features) par model train kiya gaya Google Colab mein
2. Trained model ko pickle file ke roop mein save kiya
3. Flask app banayi jo model load karke real-time predictions deti hai
4. Render par deploy kiya gaya

## Live Demo
[link yahan daalna deploy hone ke baad]