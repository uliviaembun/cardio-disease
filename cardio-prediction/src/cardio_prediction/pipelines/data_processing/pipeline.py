from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_cardio

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_cardio,
                inputs="raw_cardio_data",          # Harus sama persis dengan nama di catalog.yml
                outputs="preprocessed_cardio_data", # Harus sama persis dengan nama di catalog.yml
                name="preprocess_cardio_node",      # Nama bebas, untuk penanda visual di Kedro-Viz
            ),
        ]
    )