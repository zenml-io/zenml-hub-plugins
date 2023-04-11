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
"""Step that loads the breast cancer dataset."""

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from zenml.steps import Output, step


@step
def breast_cancer_data_loader() -> Output(
    X_train=pd.DataFrame,
    X_test=pd.DataFrame,
    y_train=pd.Series,
    y_test=pd.Series,
):
    """Load the breast cancer dataset as tuple of Pandas DataFrame / Series."""
    breast_cancer_dataset = load_breast_cancer(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        breast_cancer_dataset.data, breast_cancer_dataset.target, test_size=0.2, shuffle=True, random_state=42
    )
    return X_train, X_test, y_train, y_test
