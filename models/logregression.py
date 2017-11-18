
import pandas as pd
import numpy as np

import os

class LogRegressionModel(class):
    """
    Logistic regression model for restaurant model prediction.
    """

    def __init__(self, datadir):
        self.datadir = datadir


#    def loaddata(self):
#        """Loads data from files and stores in dataframes."""
#        geoplaces = pd.read_csv(os.path.join(self.datadir, "geoplaces2.csv"), index_col=0)
#        geoplaces = pd.DataFrame(geoplaces, columns=)

