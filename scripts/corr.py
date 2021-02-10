from scipy.stats import f_oneway
import pandas as pd
import uuid


def correlation(dataframe, m_used, fcai, tpose):
    if fcai:
        df = pd.read_csv(dataframe, index_col=0)
    else:
        df = pd.read_csv(dataframe)

    if tpose:
        df = df.T
    else:
        pass
    corrmatrix = df.corr(method=m_used)
    return corrmatrix