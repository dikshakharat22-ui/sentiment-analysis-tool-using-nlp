Running Locally:
1. Download the project from Replit
Click the three dots menu (⋮) in Replit
Select "Download as zip"
Extract it on your computer
2. Install Python (if you don't have it)
You need Python 3.11 or newer
Download from python.org
3. Install dependencies
Open terminal/command prompt in the project folder and run:

pip install flask textblob gunicorn
4. Download TextBlob data
python -m textblob.download_corpora
5. Run the app
python app.py
6. Open in browser
Go to: http://localhost:5000
Your site will be running!
