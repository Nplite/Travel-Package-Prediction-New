from Travel_Package_prediction.entity import artifact_entity,config_entity
from Travel_Package_prediction.exception import Travel_Exception
from Travel_Package_prediction.logger import logging
from Travel_Package_prediction.predictor import ModelResolver
from Travel_Package_prediction.utils import load_object, save_object
from Travel_Package_prediction.config import TARGET_COLUMN
from Travel_Package_prediction.entity.artifact_entity import DataTransformationArtifact, ModelTrainingArtifact, ModelPusherArtifact
from Travel_Package_prediction.entity.config_entity import ModelPusherConfig
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from Travel_Package_prediction import utils
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
   


class ModelPusher:
     
    def __init__(self, model_pusher_config:ModelPusherConfig,
                  data_transformation_artifact:DataTransformationArtifact,
                  model_trainer_artifact:ModelTrainingArtifact):
          


        try:
            self.model_pusher_config = model_pusher_config
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver(model_registry=self.model_pusher_config.save_model_dir)

        except Exception as e:
            raise Travel_Exception(e,sys)
        
    def initiate_model_pusher(self)->ModelPusherArtifact:
        try:
             # load model and target  encoder data
             transformer = load_object(file_path = self.data_transformation_artifact.transform_object_path)
             model = load_object(file_path = self.model_trainer_artifact.model_path)
             target_encoder = load_object(file_path = self.data_transformation_artifact.target_encoder_path)
                


             # Model pusher dir
             save_object(file_path=self.model_pusher_config.pusher_transformer_path, obj = transformer)
             save_object(file_path=self.model_pusher_config.pusher_model_dir, obj=model)
             save_object(file_path=self.model_pusher_config.pusher_target_encoder_path, obj=target_encoder)




             # save model
             transform_path = self.model_resolver.get_latest_save_transformer_path
             model_path = self.model_resolver.get_latest_save_model_path
             target_encoder_path = self.model_resolver.get_latest_save_target_encoder_path


             save_object(file_path = transform_path, obj=transformer)
             save_object(file_path=model_path, obj=model)
             save_object(file_path=target_encoder_path, obj=target_encoder)


             model_pusher_artifact = ModelPusherArtifact(pusher_model_dir =self.model_pusher_config.pusher_model_dir,
                                    saved_model_dir = self.model_pusher_config.save_model_dir)
             
             return model_pusher_artifact

        except Exception as e:
            raise Travel_Exception(e,sys)

     
        


        


















        try:
               pass 
        except Exception as e:
               raise Travel_Exception(e,sys)
          