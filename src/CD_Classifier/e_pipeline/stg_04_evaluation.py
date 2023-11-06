import sys
from CD_Classifier import logging, CustomException
from CD_Classifier.c_config.configuration import ConfigurationManager
from CD_Classifier.d_components.evaluation import Evaluation


STAGE_NAME = "Evaluation--of--Model"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        # Configuring evaluation directories/ creating paths for evaluation directories
        config = ConfigurationManager()
        # Creating the evaluation configuration instance
        eval_config = config.get_validation_config()

        # Loading eval config into Evaluating instance
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logging.info(
            f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        eval_pipline = EvaluationPipeline()
        eval_pipline.main()
        logging.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
