# spotify_real_time.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ----------------- USER SETTINGS -----------------
CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "user-read-recently-played"

# ----------------- SPOTIFY AUTH -----------------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# ----------------- FETCH RECENT TRACKS -----------------
def fetch_recent_tracks(limit=200):
    results = sp.current_user_recently_played(limit=limit)
    rows = []
    for item in results['items']:
        played_at = pd.to_datetime(item['played_at'])
        track = item['track']
        artists = ", ".join([a['name'] for a in track['artists']])
        rows.append({
            'played_at': played_at,
            'artistName': artists,
            'trackName': track['name']
        })
    df = pd.DataFrame(rows)
    return df

# ----------------- FEATURE EXTRACTION -----------------
def extract_features(df):
    df['hour'] = df['played_at'].dt.hour
    df['weekday'] = df['played_at'].dt.day_name()
    df['date'] = df['played_at'].dt.date
    df['is_weekend'] = df['weekday'].isin(['Saturday', 'Sunday'])
    return df

# ----------------- VISUALIZATION -----------------
def plot_heatmap(df):
    order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    heat = df.pivot_table(index='weekday', columns='hour', values='trackName', aggfunc='count').reindex(order)
    plt.figure(figsize=(14,5))
    sns.heatmap(heat, fmt='.0f', linewidths=.5, cmap="YlGnBu")
    plt.title("Listening counts — weekday (rows) x hour (columns)")
    plt.xlabel("Hour of day")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def plot_top_artists(df, top_n=50):
    top_artists = df['artistName'].value_counts().head(top_n)
    plt.figure(figsize=(8,6))
    top_artists.sort_values().plot(kind='barh', color='orange')
    plt.title(f"Top {top_n} artists by play count")
    plt.xlabel("Plays")
    plt.tight_layout()
    plt.show()

def plot_daily_trend(df):
    daily = df.groupby('date').size()
    plt.figure(figsize=(12,4))
    daily.rolling(7).mean().plot(color='green')  # 7-day rolling mean
    plt.title("Plays per day (7-day rolling mean)")
    plt.ylabel("Plays")
    plt.tight_layout()
    plt.show()

# ----------------- MAIN (Continuous Mode) -----------------
if __name__ == "__main__":
    print("Starting continuous Spotify data fetching...")
    while True:
        df = fetch_recent_tracks(limit=200)
        df = extract_features(df)

        print("Generating visualizations...")
        plot_heatmap(df)
        plot_top_artists(df)
        plot_daily_trend(df)

        print("Waiting 5 minutes before next fetch...")
        time.sleep(300)  # 300 seconds = 5 minutes
