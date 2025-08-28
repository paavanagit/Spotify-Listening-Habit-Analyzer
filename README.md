Spotify Listening Habit Analyzer

Analyze your Spotify listening habits in Python with heatmaps, top artists, trends, and optional genre insights using the Spotify Web API.

Overview

This Python mini project fetches a user’s recently played tracks from Spotify and analyzes listening patterns. It generates insightful visualizations including:

Heatmap of listening frequency by weekday and hour

Bar chart of top artists

Trend chart of daily plays

Optional genre enrichment to explore favorite music styles

It’s beginner-friendly, fully automated, and provides near real-time insights into your music listening behavior.

Features

Fetch recent Spotify tracks using the Spotify Web API and Spotipy

Extract features like hour, weekday, and play counts

Visualize data using Matplotlib and Seaborn

Optional genre analysis for deeper insights

Continuous mode to refresh data every 5 minutes

Requirements

Python 3.x

Libraries: pandas, numpy, matplotlib, seaborn, spotipy
Usage

Open spotify_real_time.py in Spyder or any Python IDE

Run the script (F5 in Spyder)

Authorize your Spotify account when prompted

Visualizations will pop up and update every 5 minutes in continuous mode

Notes

Press stop in Spyder to end the loop

Adjust time.sleep(300) to change the refresh interval (seconds)

Optional genre enrichment may take longer due to API requests

Technologies Used

Python

Pandas, NumPy

Matplotlib, Seaborn

Spotipy (Spotify Web API wrapper)
