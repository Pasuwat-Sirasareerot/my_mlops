from datetime import datetime
import os
from networksecurity.constant import training_pipeline

print(training_pipeline.PIPE_LINE_NAME)
print(training_pipeline.ARTIFACET_DIR)
print(training_pipeline.DATA_INGESTION_DIR_NAME)
print(training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR)
print(training_pipeline.DATA_INGESTION_INGESTED_DIR)
print(training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION)

class TrainingPipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
        self.pipeline_name = training_pipeline.PIPE_LINE_NAME
        self.artifact_name = training_pipeline.ARTIFACET_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp: str = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
            )
        self.feature_store_dir = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR
            )
        self.training_file_path = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME