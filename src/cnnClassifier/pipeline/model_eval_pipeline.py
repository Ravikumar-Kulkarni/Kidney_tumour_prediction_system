from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eval_component import Evaluation
from src.cnnClassifier import logger
import os


STAGE_NAME = "Evaluation stage"




class EvaluationPipeline:
    def __init__(self):
        
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Ravikumar-Kulkarni/Kidney_tumour_prediction_system.mlflow"
        # Set your DagsHub credentials (MLflow uses HTTP Basic Auth)
        os.environ["MLFLOW_TRACKING_USERNAME"] = "Ravikumar-Kulkarni"
        os.environ["MLFLOW_TRACKING_PASSWORD"] = "7fc4d9728a50e51850aa7e6d92d5a071337ef4fe"


    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

