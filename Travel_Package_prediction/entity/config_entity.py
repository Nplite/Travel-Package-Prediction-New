import os,sys
from Travel_Package_prediction.logger import logging
from Travel_Package_prediction.exception import Travel_Exception
from datetime import datetime


FILE_NAME = "TourismData.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
TRANSFORMER_OBJECT_FILE_NAME = "transformer.pkl"
TARGET_ENCODER_OBJECT_FILE_NAME = "target_encoder.pkl"
MODEL_FILE_NAME = "model.pkl"
class TrainingPipelineConfig:
    
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception  as e:
            raise Travel_Exception(e,sys)    


class DataIngestionConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="TRAVEL_PACKAGE_PREDICTION"
            self.collection_name="TRAVEL_PACKAGE_PREDICTION_PROJECT"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception  as e:
            raise Travel_Exception(e,sys)      

            
# Convert data into dict
    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise Travel_Exception(e,sys)   

class DataValidationConfig:
    def __init__(self,training_pipline_config: TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipline_config.artifact_dir, "data_validation")
        self.report_file_path = os.path.join(self.data_validation_dir,"report.yaml")
        self.missing_threshold:float = 0.3
        self.base_file_path = os.path.join("TourismData.csv")


class ModelTrainingConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir - os.path.join(training_pipeline_config.artifact_dir, "model_trainer")
        self.model_path = os.path.join(self.model_trainer_dir, "model", MODEL_FILE_NAME)
        self.expected_accuracy = 0.7
        self.overfitting_threshold = 0.3
        