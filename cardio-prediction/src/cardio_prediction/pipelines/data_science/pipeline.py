from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs="preprocessed_cardio_data", # Data bersih dari pipeline sebelumnya!
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="cardio_model",
                name="train_model_node",
            ),
        ]
    )