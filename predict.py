from cog import BasePredictor, Input


class Predictor(BasePredictor):
    def setup(self):
        self.prefix = "howdy"

    def predict(self, text: str = Input(description="Text to prefix with 'hello '")) -> str:
        return self.prefix + " " + text