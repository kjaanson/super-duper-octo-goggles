from sklearn.ensemble import RandomForestClassifier
from .basemodel import BaseModel


class RandomForestModel(BaseModel):
    """Random forest model for restaurant rating prediction."""

    def _trainmodel(self):
        """Trains model."""
        model = RandomForestClassifier()
        self.model = model.fit(self.df_X.values, y=self.df_y.values)
