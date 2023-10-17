import pandas as pd
import sweetviz as sv

# ---------------------------------------------------------------------------- #
#                                    Codigo                                    #
# ---------------------------------------------------------------------------- #

def load_data():    
    df = pd.read_csv('data/Credit_data.csv')
    return df

def eda(df:pd):
    print(df.head())
    print(df.describe())
    my_report = sv.analyze(df)
    my_report.show_html('reports/eda.html') 

if __name__ == "__main__":

    eda(load_data())