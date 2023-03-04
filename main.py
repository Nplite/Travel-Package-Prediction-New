from Travel_Package_prediction.logger import logging
from Travel_Package_prediction.exception import InsuranceException
from Travel_Package_prediction.utils import get_collection_as_dataframe
import sys, os
from Travel_Package_prediction.entity.config_entity import DataIngestionConfig
from Travel_Package_prediction.entity import config_entity
#from Travel_Package_prediction.components.data_ingestion import DataIngestion
#from Travel_Package_prediction.components.data_validation import DataValidation

#from Travel_Package_prediction.components.data_transformation import DataTransformation

#def test_logger_and_expection():
   # try:
       # logging.info("Starting the test_logger_and_exception")
        #result = 3/0
       # print(result)
       # logging.info("Stoping the test_logger_and_exception")
    #except Exception as e:
      #  logging.debug(str(e))
       # raise InsuranceException(e, sys)

if __name__=="__main__":
    try:
          #start_training_pipeline()
          #test_logger_and_expection()
        get_collection_as_dataframe(database_name ="TRAVEL_PACKAGE_PREDICTION", collection_name = 'TRAVEL_PACKAGE_PREDICTION_PROJECT')
        #training_pipeline_config = config_entity.TrainingPipelineConfig()
         
    except Exception as e:
        print(e)