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
"""Step that loads an OpenML dataset."""

from typing import Optional

import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from zenml.steps import BaseParameters, Output, step


class OpenMLDataLoaderStepParameters(BaseParameters):
    """OpenML Data Loader step parameters.

    Attributes:
        dataset_name: Name of the OpenML dataset.
        dataset_version: Version of the OpenML dataset.
        dataset_parser: Parser to use for the OpenML dataset.
    """

    dataset_name: str = "miceprotein"
    dataset_version: Optional[int] = 4
    dataset_parser: Optional[str] = "auto"


@step
def openml_data_loader(
    params: OpenMLDataLoaderStepParameters,
) -> Output(
    X_train=pd.DataFrame,
    X_test=pd.DataFrame,
    y_train=pd.Series,
    y_test=pd.Series,
):
    """Load an OpenML dataset as tuple of Pandas DataFrame / Series."""
    openml_dataset = fetch_openml(
        name=params.dataset_name,
        version=params.dataset_version,
        parser=params.dataset_parser,
        as_frame=True,
    )
    X_train, X_test, y_train, y_test = train_test_split(
        openml_dataset.data,
        openml_dataset.target,
        test_size=0.2,
        shuffle=True,
        random_state=42,
    )
    return X_train, X_test, y_train, y_test
