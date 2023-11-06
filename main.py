import sys
from src.CD_Classifier import logging, CustomException
from src.CD_Classifier.e_pipeline.stg_01_data_ingestion import DataIngestionPipeline
from src.CD_Classifier.e_pipeline.stg_02_base_model import BaseModelPipeline
from src.CD_Classifier.e_pipeline.stg_03_training import TrainingPipeline
# -----------------------------------------------------------------------------
STAGE_NAME = "Data--Ingestion--Stage"

try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
    DT_Pipe = DataIngestionPipeline()
    DT_Pipe.main()
    logging.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.info(CustomException(e, sys))
    raise CustomException(e, sys)

# -----------------------------------------------------------------------------
STAGE_NAME = "Base--Model--Preparation"

try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
    DT_Pipe = BaseModelPipeline()
    DT_Pipe.main()
    logging.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.info(CustomException(e, sys))
    raise CustomException(e, sys)


# -----------------------------------------------------------------------------
STAGE_NAME = "Training--the--Data"

try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
    DT_Pipe = TrainingPipeline()
    DT_Pipe.main()
    logging.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.info(CustomException(e, sys))
    raise CustomException(e, sys)
