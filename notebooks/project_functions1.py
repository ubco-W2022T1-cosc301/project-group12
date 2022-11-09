import pandas as pd
import numpy as py
import matplotlib.pylab as plt
import seaborn as sns
def load_and_process(path_to_csv_file):
    df_cleaner = (
        pd.read_csv('../data/raw/anime.csv')
    )
    def clean_Type(row):
        atype = ['Unknown']
        if row.Type in atype:
            return 'Other'
        return row.Type
    def clean_df(playlist):
        df_cleaned=df_cleaner.copy()
        df_cleaned['Type']=df_cleaned.apply(lambda row:clean_Type(row),axis=1)
        return df_cleaned
    df_cleaned = clean_df(df_cleaner)
    df_cleaned = df_cleaned[df_cleaned['Popularity']>0]
    df_cleaned = df_cleaned[df_cleaned['Completed']>0]

    df = (
        df_cleaned
        .drop(df_cleaned.columns[[0,1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34]],axis=1,inplace=False)
        .dropna(axis=0)
        .rename(columns={'Completed':'Full Anime Completions'})
    )
    return df


