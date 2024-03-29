from Travel_Package_prediction.components.model_trainer import ModelTrainer
from Travel_Package_prediction.entity.artifact_entity import DataIngestionArtifact
from Travel_Package_prediction.logger import logging
from Travel_Package_prediction.exception import Travel_Exception
from Travel_Package_prediction.utils import get_collection_as_dataframe
import sys, os
from Travel_Package_prediction.entity.config_entity import DataIngestionConfig
from Travel_Package_prediction.entity import config_entity
from Travel_Package_prediction.components.data_ingestion import DataIngestion
from Travel_Package_prediction.components.data_validation import DataValidation
from Travel_Package_prediction.components.data_transformation import DataTransformation
from Travel_Package_prediction.components import ModelEvaluation
from Travel_Package_prediction.components.model_pusher import ModelPusher



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
                                        data_ingestion_artifact = data_ingestion_artifact)
        
        data_validation_artifact = data_validation.initiate_data_validation()

      # Data Transformation

        data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config=data_transformation_config, 
                                                   data_ingestion_artifact = data_ingestion_artifact)
        data_transformation_artifact = data_transformation.initiate_data_transformation()

      # Model Trainer

        model_trainer_config = config_entity.ModelTrainingConfig(training_pipeline_config=training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config= model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()

      # Model Evaluation
        model_evaluation_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
        model_evaluation = ModelEvaluation(model_evaluation_config = model_evaluation_config,
        data_ingestion_artifact = data_ingestion_artifact,
        data_transformation_artifact = data_transformation_artifact,
        model_trainer_artifact = model_trainer_config)
        model_evaluation_artifact = model_evaluation.initiate_model_evaluation()

      # Model pusher
        model_pusher_config = config_entity.ModelPusherConfig(training_pipeline_config=training_pipeline_config)
        model_pusher = ModelPusher(model_pusher_config= model_pusher_config,
                                   data_transformation_artifact=data_transformation_artifact,
                                   model_trainer_artifact=model_trainer_artifact)
        
        Model_pusher_artifact = model_pusher.initiate_model_pusher()
    


    except Exception as e:
        print(e)
        