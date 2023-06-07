import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            logging.info("Prediction Pipeline started")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)
            logging.info("Prediction Pipeline Completed")
            return pred

        except Exception as e:
            logging.info("Exception occurred in prediction")
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, cement, blast_furnace_slag, fly_ash, water, superplasticizer, 
                coarse_aggregate, fine_aggregate, age):
        self.cement = cement
        self.blast_furnace_slag = blast_furnace_slag
        self.fly_ash = fly_ash
        self.water = water
        self.superplasticizer = superplasticizer
        self.coarse_aggregate = coarse_aggregate
        self.fine_aggregate = fine_aggregate
        self.age = age

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'cement': [self.cement],
                'blast_furnace_slag': [self.blast_furnace_slag],
                'fly_ash': [self.fly_ash],
                'water': [self.water],
                'superplasticizer': [self.superplasticizer],
                'coarse_aggregate': [self.coarse_aggregate],
                'fine_aggregate ': [self.fine_aggregate],
                'age': [self.age]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df

        except Exception as e:
            logging.info('Exception Occurred in prediction pipeline')
            raise CustomException(e, sys)
