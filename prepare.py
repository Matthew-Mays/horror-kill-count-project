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

# Fuction for splitting data into train, validate, and test dataframes
def data_split(df):
    train_validate, test = train_test_split(df, test_size=.25, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.4, random_state=123)
    return train, validate, test