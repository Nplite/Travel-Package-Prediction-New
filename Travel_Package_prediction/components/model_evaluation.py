from Travel_Package_prediction.entity import artifact_entity,config_entity
from Travel_Package_prediction.exception import Travel_Exception
from Travel_Package_prediction.logger import logging
from Travel_Package_prediction.predictor import ModelResolver
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from Travel_Package_prediction import utils
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score




class ModelEvaluation:
    def __init(self,
               model_evaluation_config:config_entity.ModelEvaluationConfig,
               data_ingestion_artifact : artifact_entity.DataIngestionArtifact,
               data_transformation_artifact: artifact_entity.DataTransformationArtifact,
               model_trainer_artifact: artifact_entity.ModelTrainingArtifact):
        
        try:
            self.model_evaluation_config = model_evaluation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver()


        except Exception as e:
            raise Travel_Exception(e,sys)
        

    def initiate_model_evaluation(self)-> artifact_entity.ModelEvaluationArtifact:
        try:
            latest_dir_path = self.model_resolver.get_latest_dir_path()

            if latest_dir_path== None:
                model_evaluation_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,improved_accuracy=None)
                logging.info(f"Model evaluation artifact: {model_evaluation_artifact}")

                return model_evaluation_artifact
        except Exception as e:
            raise Travel_Exception(e,sys)



