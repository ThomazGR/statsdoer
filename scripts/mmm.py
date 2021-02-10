# media, mediana, moda e describe

import pandas as pd
import matplotlib.pyplot as plt
import uuid


def media(dataframe, fcai, tpose):
    if fcai:
        df = pd.read_csv(dataframe, index_col=0)
    else:
        df = pd.read_csv(dataframe)

    if tpose:
        df = df.T
    else:
        pass

    df = df.mean()
    return df


def mediana(dataframe, fcai, tpose):
    if fcai:
        df = pd.read_csv(dataframe, index_col=0)
    else:
        df = pd.read_csv(dataframe)

    if tpose:
        df = df.T
    else:
        pass

    df = df.median()
    return df


def moda(dataframe, fcai, tpose):
    if fcai:
        df = pd.read_csv(dataframe, index_col=0)
    else:
        df = pd.read_csv(dataframe)

    if tpose:
        df = df.T
    else:
        pass

    df = df.mode()
    return df


def describe(dataframe, fcai, tpose):
    if fcai:
        df = pd.read_csv(dataframe, index_col=0)
    else:
        df = pd.read_csv(dataframe)

    if tpose:
        df = df.T
    else:
        pass

    df = df.describe()
    return df


def plotmean(dataframe, fcai, tpose):
    if fcai:
        df = pd.read_csv(dataframe, index_col=0)
    else:
        df = pd.read_csv(dataframe)

    if tpose:
        df = df.T
    else:
        pass

    df = df.mean()
    plt.plot(df)
    plt.title("Mean Plot")
    idfig = str(uuid.uuid4())
    png = ".png"
    idfinal = "".join((idfig, png))
    plt.savefig(fname=idfinal)
    return df, idfinal