from Travel_Package_prediction.entity import artifact_entity,config_entity
from Travel_Package_prediction.exception import Travel_Exception
from Travel_Package_prediction.logger import logging
from Travel_Package_prediction.predictor import ModelResolver
from Travel_Package_prediction.utils import load_object
from Travel_Package_prediction.config import TARGET_COLUMN
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
            


            # find location of previous model
            transformer_path = self.model_resolver.get_latest_transformer_path()
            model_path = self.model_resolver.get_latest_save_model_path()
            target_encoder_path = self.model_resolver.get_latest_target_encoder_path()

            # previous model
            transformer = load_object(File_path=transformer_path)
            model = load_object(file_path = model_path)
            target_encoder = load_object(file_path = target_encoder_path)

            # New model
            current_transformer = load_object(file_path = self.data_transformation_artifact.transform_object_path)
            current_model = load_object(file_path = self.model_trainer_artifact.model_path)
            current_target_encoder = load_object(file_path=self.data_transformation_artifact.target_encoder_path)


            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            target_df = test_df[TARGET_COLUMN]
            y_true = target_df


            input_features_name = list(transformer.feature_name_in_)
            for i in input_features_name:
                if test_df[i].dtypes=="object":
                    test_df[i] = target_encoder.fit_transform(test_df[i])

            input_arr = transformer.transform(test_df[input_features_name])
            y_pred = model.predict(input_arr)



            # comparision between new model and old model
            previous_model_score = r2_score(y_true= y_true,y_pred = y_pred)


            # accuracy of current trained model
            input_features_name = list(current_transformer.feature_name_in_)
            input_arr = current_transformer.transform(test_df[input_features_name])
            y_pred = current_model.predict(input_arr)
            y_true = target_df

            current_model_score = r2_score(y_true = y_true, y_pred = y_pred)


            # Final camparision between both model
            if current_model_score < previous_model_score :
                logging.info(f"current trained model is not better than previous model")
                raise Exception("current model is not better than previous model")
            

            mode_evaluation_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True, 
            improved_accuracy= current_model_score-previous_model_score)
            

            return model_evaluation_artifact    

        except Exception as e:
            raise Travel_Exception(e,sys)
        



# we can store output in cloud platform
# aws ->s3 bucket
# Database ->Model pusher



