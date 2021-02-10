import pandas as pd
import numpy as np
from scipy.stats import normaltest


def norm(sample, fcai, tpose):
    if fcai:
        samp = pd.read_csv(sample, index_col=0)
    else:
        samp = pd.read_csv(sample)

    if tpose:
        samp = samp.T
    else:
        pass

    zk, p = normaltest(samp)
    return zk, p
