# NLP Sentiment Analysis & Recommendation System

## Overview
This is a web-based NLP Sentiment Analysis and Recommendation System built from a GitHub import. The project presents information about binary and multi-class sentiment analysis using various machine learning and deep learning models, along with a movie recommendation system.

## Project Status
✅ Fully set up and running in Replit environment

## Tech Stack
- **Backend**: Python 3.11, Flask
- **Sentiment Analysis**: TextBlob
- **Production Server**: Gunicorn
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

## Project Structure
```
/
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Web interface
├── static/                 # Static assets (if needed)
└── .gitignore             # Python gitignore
```

## Features
1. **Interactive Sentiment Analysis Tool**: Users can input text and get real-time sentiment analysis with polarity and subjectivity scores
2. **Project Information Display**: Comprehensive presentation of the research project including:
   - Datasets used (IMDB Reviews, Tweets)
   - ML models (Random Forest, Logistic Regression)
   - Deep Learning models (RNN, AvgNet, CNN)
   - Recommendation system details
   - Key findings and results

## Running the Project
- **Development**: Workflow runs `python app.py` on port 5000
- **Production**: Configured with Gunicorn for autoscale deployment

## Deployment Configuration
- **Type**: Autoscale (stateless web application)
- **Command**: `gunicorn --bind=0.0.0.0:5000 --reuse-port app:app`

## Recent Changes (October 1, 2025)
- Created complete web application from empty repository
- Set up Flask backend with TextBlob sentiment analysis
- Created responsive web interface with gradient design
- Configured development workflow and deployment settings
- Downloaded necessary NLTK corpora for TextBlob

## Notes
- The sentiment analysis uses TextBlob's pre-trained models
- The web interface displays project information from the original README
- Users can test sentiment analysis on their own text inputs
