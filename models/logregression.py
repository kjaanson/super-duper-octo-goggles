
import pandas as pd
import numpy as np

import os
import sys

from sklearn.linear_model import LogisticRegression
import pickle

class LogRegModel():
    """
    Logistic regression model for restaurant rating prediction. Can be used for generating other models also if
    _preprocessing and _trainmodel methods are overridden.
    """

    def __init__(self, datadir):
        self.datadir = datadir

        self._load_data()
        self._combine_data()
        self._preprocessing()
        self._trainmodel()

    def _load_data(self):
        """Loads data from files and stores in dataframes."""
        geoplaces = pd.read_csv(os.path.join(self.datadir, "geoplaces2.csv"), index_col=0)
        self.geoplaces = pd.DataFrame(geoplaces, columns=["smoking_area", "other_services", "dress_code", "accessibility"])

        parking = pd.read_csv(os.path.join(self.datadir, "chefmozparking.csv"), index_col=0)
        self.parking = parking

        ratings = pd.read_csv(os.path.join(self.datadir, "rating_final.csv"), index_col=1)
        self.ratings = ratings.drop(["food_rating", "service_rating"], axis=1)

    def _combine_data(self):
        """Combines data from geoplaces, parking and ratings table. Results in Pandas DataFrame that has all the
        features nessesary for model training."""

        geoplaces_and_parking = self.geoplaces.join(self.parking)
        full_feature_set = self.ratings.join(geoplaces_and_parking)

        self.df_raw_training_data = full_feature_set

        return self

    def _preprocessing(self):
        """Preprocesses data using pandas DataFrame get_dummies function. Sets self.df_X dataframe to be preprocessed
        features to be used for training and self.df_y dataframe of target classes."""

        df = self.df_raw_training_data

        df_smoking_area = pd.get_dummies(df.smoking_area, prefix="smoking_area")
        df_other_services = pd.get_dummies(df.other_services, prefix="other_services")
        df_dress_code = pd.get_dummies(df.dress_code, prefix="dress_code")
        df_accesibility = pd.get_dummies(df.accessibility, prefix="access")
        df_parking_lot = pd.get_dummies(df.parking_lot, prefix="parking")

        self.df_X = pd.concat([
            df_smoking_area,
            df_other_services,
            df_dress_code,
            df_accesibility,
            df_parking_lot
            ], axis=1)

        self.df_y = df[["rating"]]

    @property
    def _features_(self):
        """Returns list of column names that model is trained on."""
        return list(self.df_X.columns)

    def _trainmodel(self):
        """Trains model."""
        model = LogisticRegression()
        self.model = model.fit(self.df_X.values, y = self.df_y.values)

    def predict(self, feature_array):
        """Makes prediction based on the given feature array.
        TODO add error check for feature number here.
        """
        np_array = np.array([feature_array])

        return self.model.predict(np_array)

    @property
    def _desc_(self):
        return self.__doc__

if __name__ == '__main__':

    dir = sys.argv[1]
    output_modelfile = sys.argv[2]

    model = LogRegModel(dir)

    # TODO print model score et into log

    with open(os.path.join(output_modelfile),"wb") as model_file:
        pickle.dump(model, model_file)



