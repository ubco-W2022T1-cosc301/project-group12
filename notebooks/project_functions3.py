import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
    
    #Method Chain 1 (Custom columns)
    
    df= pd.read_csv('../data/raw/anime.csv', usecols=['Score','Type','Episodes','Ranked'])

    # Method Chain 2 (Removing null values)

    df1 = (
          pd.read_csv('../data/raw/anime.csv')
          .dropna(axis=0)
        
        #Method Chain 3 (Removing Redundant/ Duplicate values)
        
        def duplication():
    

(
    
 if len(df[df.duplicated()]) > 0:
    print("No. of duplicated entries: ", len(df[df.duplicated()]))
    print(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)).head())
else:
    print("No duplicated entries found")
    
df.drop_duplicates(inplace=True)
          
      )
    # Method Chain 4 (Removing unimportant data/ Like null and unknown values)
    
    df2= ( df=df[df['Episodes']>0]
df=df[df['Ranked'].between(1,100)]
df=df[df['Watching']>0.00]
df=df[df['Completed']>0.00]
df=df[df['Dropped']>0.00]
df=df[df['On-Hold']>0.00]
df=df[df['Score-10']>0.00]
df=df[df['Score-1']>0.00]
         


         )
    
df2.to_csv('processed3.csv')




df2=load_and_process('..data/raw/anime.csv')