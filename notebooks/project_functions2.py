import pandas as pd

def load_and_process(data):

    df = (
    pd.read_csv(data, usecols = ["Name", "Score", "Source", "Studios", "Ranked", "Popularity", "Completed"])
    .pipe(lambda x: x.loc[x['Studios'] != "Unknown"]) 
    .pipe(lambda x: x.loc[x['Score'] != "Unknown"])
    .pipe(lambda x: x.loc[x['Ranked'] != "Unknown"])
    .pipe(lambda x: x.loc[x['Source'] != "Unknown"])
    )
    # load data and remove rows with unknowns

    df2 = (
    df
    .pipe(lambda x: x.loc[x['Popularity'] > 0])
    .pipe(lambda x: x.loc[x['Completed'] > 0])
    .assign(Score = df.Score.astype('float64'))
    .assign(Popularity = df.Popularity.astype('int64'))
    .assign(Ranked = df.Ranked.astype('int64'))
    )
    # remove animes that nobody has ever fully completed and convert score, ranked and popularity to numerical types

    return df2