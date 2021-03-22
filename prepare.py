import pandas as pd
import numpy as np

# Fuction for adding kills per minute (kpm) to dataframe
def kpm(df):
    df['kpm'] = df.kc / df.length

# Function for adding categorical bins of movie popularity based on Rotten Tomatoes score
def pop_cat(df):
    df['pop_cat'] = pd.cut(df.rt_score, bins=[0, 0.30, 0.69, 1], labels=['low', 'medium', 'high'])

# Function containing any additional feature to the movie data dataframe
def add_movie_features(df):
    kpm(df)
    pop_cat(df)