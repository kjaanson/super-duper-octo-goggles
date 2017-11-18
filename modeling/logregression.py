
import pandas as pd
import numpy as np

import os
import sys

from sklearn.linear_model import LogisticRegression
import pickle

from .basemodel import BaseModel

class LogRegModel(BaseModel):
    """
    Logistic regression model for restaurant rating prediction. Can be used for generating other models also if
    _preprocessing and _trainmodel methods are overridden.
    """

    def _trainmodel(self):
        """Trains model."""
        model = LogisticRegression()
        self.model = model.fit(self.df_X.values, y = self.df_y.values)

if __name__ == '__main__':

    dir = sys.argv[1]
    output_modelfile = sys.argv[2]

    model = LogRegModel(dir)

    # TODO print model score et into log

    with open(os.path.join(output_modelfile),"wb") as model_file:
        pickle.dump(model, model_file)



