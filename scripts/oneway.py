from scipy.stats import f_oneway
import pandas as pd
import sys

# F_oneway not finished
def anova(dataframe, colunas, fcai, tpose):
    if fcai:
        df = pd.read_csv(dataframe, index_col=0)
    else:
        df = pd.read_csv(dataframe)

    if tpose:
        df = df.T
    else:
        pass

    dfs = map(lambda arg: df[arg], colunas)

    f, p = f_oneway(*dfs)

    return f, p