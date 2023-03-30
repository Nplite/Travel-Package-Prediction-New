from Travel_Package_prediction.exception import Travel_Exception
from Travel_Package_prediction.logger import logging
from typing import Optional
from Travel_Package_prediction.predictor import ModelResolver
from Travel_Package_prediction.utils import load_object
import numpy as np
from datetime import datetime
import pandas as pd
import os,sys


PREDICTION_DIR = "prediction"

def start_batch_prediction(input_file_path):
    try:
        os.makedirs(PREDICTION_DIR, exist_ok=True)
        model_resolver = ModelResolver(model_registry="saved_model")
        # Data Load
        df = pd.read_csv(input_file_path)
        df.replace("na":np.NAN, inplace= True)

        # Data validation
        transformer = load_object(file_path=model_resolver.get_latest_transformer_path())
        target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())

        input_features_name = list(transformer.feature_names_in_)
        for i in input_features_name:
            if df[i].dtypes=="object":
                df[i] = target_encoder.fit_transform(df[i])


        input_arr = transformer.transform(df[input_features_name])

        model = load_object(file_path=model_resolver.get_latest_dir_path)
        prediction = model.predict(input_arr)

        df['prediction'] = prediction

        prediction_file_name = os.path.basename(input_file_path).replace(".csv", f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.csv")

        prediction_file_name = os.path.join(PREDICTION_DIR, prediction_file_name)
        df.to_csv(prediction_file_name, index=False, header=True)
        return prediction_file_name


    except Exception as e:
        raise Travel_Exception(e,sys)