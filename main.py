from Travel_Package_prediction.entity.artifact_entity import DataIngestionArtifact
from Travel_Package_prediction.logger import logging
from Travel_Package_prediction.exception import Travel_Exception
from Travel_Package_prediction.utils import get_collection_as_dataframe
import sys, os
from Travel_Package_prediction.entity.config_entity import DataIngestionConfig
from Travel_Package_prediction.entity import config_entity
from Travel_Package_prediction.components.data_ingestion import DataIngestion
from Travel_Package_prediction.components.data_validation import DataValidation




if __name__=="__main__":
    try:
       
       training_pipeline_config = config_entity.TrainingPipelineConfig()
       
      #data ingestion
       data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
       print(data_ingestion_config.to_dict())
       data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
       data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        print(e)

     # Data Validation
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,
                         data_ingestion_artifact = DataIngestionArtifact)
        
        data_validation_artifact = data_validation.initiate_data_validation()