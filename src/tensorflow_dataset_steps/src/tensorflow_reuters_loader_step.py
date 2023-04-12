#  Copyright (c) ZenML GmbH 2023. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.


import numpy as np
import tensorflow as tf

from zenml.steps import Output, step


@step
def reuters_tf_loader() -> Output(
    x_train=np.ndarray,
    y_train=np.ndarray,
    x_test=np.ndarray,
    y_test=np.ndarray,
):
    """Download the Reuters dataset and store it as an artifact."""
    (x_train, y_train), (
        x_test,
        y_test,
    ) = tf.keras.datasets.reuters.load_data(seed=42)
    return x_train, y_train, x_test, y_test
