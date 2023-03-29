from Travel_Package_prediction.entity import artifact_entity,config_entity
from Travel_Package_prediction.exception import Travel_Exception
from Travel_Package_prediction.logger import logging
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from Travel_Package_prediction import utils
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score






class ModelTrainer:
    def __init__(self,model_trainer_config:config_entity.ModelTrainingConfig, 
                 data_transfomation_artifact: artifact_entity.DataTransformationArtifact):
        


        try:
            self.model_trainer_config = model_trainer_config
            self.data_transfomation_artifact = data_transfomation_artifact

        except  Exception as e:
            raise Travel_Exception(e,sys)
        

    def train_model(self,x,y):
        try:
            rf = RandomForestRegressor()
            rf.fit(x,y)
            return rf
        except Exception as e:
            raise Travel_Exception(e,sys)
        


def initiate_model_trainer(self,)->artifact_entity.ModelTrainingArtifact:
    try:
        train_arr = utils.load_numpy_array_data(file_path=self.data_transfomation_artifact.transformed_train_path)
        test_arr = utils.load_numpy_array_data(file_path=self.data_transfomation_artifact.transformed_test_path)



        x_train, y_train = train_arr[:,:-1], test_arr[:,-1]
        x_test, y_test = test_arr[:,:-1], test_arr[:,-1]

        model = self.train_model(x= x_train, y = y_train)

        yhat_train = model.predict(x_train)
        r2_train_score = r2_score(y_true=y_train,y_pred= yhat_train)


        yhat_test = model.predict(x_test)
        r2_test_score = r2_score(y_true=y_test,y_pred= yhat_test)



        if r2_test_score < self.model_trainer_config.expected_accuracy:
            raise Exception(f"Model is not good as it is not able to give  \
                             expected accuracy:{self.model_trainer_config.expected_accuracy}:model actual score: {r2_test_score}")

       
        diff = abs(r2_train_score - r2_test_score)


        if diff > self.model_trainer_config.overfitting_threshold:
            raise Exception(f" Train model and Test score difference :{diff} is more than overfitting threshold {self.model_trainer_config.overfitting_threshold}")
        

        utils.save_object(file_path = self.model_trainer_config.model_path, obj= model)

        model_trainer_artifact = artifact_entity.ModelTrainingArtifact(model_path=self.model_trainer_config.model_path,
                                                               r2_test_score = r2_train_score, r2_test_score = r2_test_score)
        
















    except Exception as e:
        raise Travel_Exception(e,sys)
        

      
         

        






    
