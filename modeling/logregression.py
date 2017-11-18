from sklearn.linear_model import LogisticRegression
from .basemodel import BaseModel


class LogRegModel(BaseModel):
    """Logistic regression model for restaurant rating prediction."""

    def _trainmodel(self):
        """Trains model."""
        model = LogisticRegression()
        self.model = model.fit(self.df_X.values, y=self.df_y.values)
