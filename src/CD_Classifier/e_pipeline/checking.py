from CD_Classifier.b_entity.config_entity import (DataIngestionConfig,
                                                  PrepareBaseModelConfig,
                                                  PrepareCallbacksConfig,
                                                  TrainingConfig,
                                                  EvaluationConfig)
from CD_Classifier.f_utils.common import read_yaml, create_directories
from CD_Classifier import logging
from pathlib import Path
import os
import os
from CD_Classifier.a_constants import *


class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH):

        os.chdir('../../../')

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        logging.info(f"data ingestion config is ready to use")

        return data_ingestion_config


print(os.getcwd())
# os.chdir('../../../')
# print(os.getcwd())
# print(os.path.dirname(__file__))

cm = ConfigurationManager()
cm.get_data_ingestion_config()
