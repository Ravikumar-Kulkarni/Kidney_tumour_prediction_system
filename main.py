from src.cnnClassifier import *
from src.cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.base_model_pipeline import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.cnnClassifier.pipeline.model_eval_pipeline import EvaluationPipeline



STAGE_NAME = "Data Ingestion stage"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  data_ingestion = DataIngestionTrainingPipeline()
  data_ingestion.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e

STAGE_NAME = "Prepare base model"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  prepare_base_model = PrepareBaseModelTrainingPipeline()
  prepare_base_model.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e  


STAGE_NAME = "Model training"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  model_trainer = ModelTrainingPipeline()
  model_trainer.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e  


STAGE_NAME = "Model evaluation"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  model_eval = EvaluationPipeline()
  model_eval.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e  
