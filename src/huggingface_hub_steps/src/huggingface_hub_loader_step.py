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


from typing import Optional

from datasets import DatasetDict, load_dataset
from zenml.steps import BaseParameters, step


class HuggingfaceHubDatasetLoaderStepParameters(BaseParameters):
    """Parameters for the Huggingface Hub Dataset Loader Step.

    Attributes:
        dataset_name: Name of the dataset to be loaded from the Huggingface Hub.
        dataset_configuration: Configuration of the dataset to be loaded from
            the Huggingface Hub.
    """

    dataset_name: str
    dataset_configuration: Optional[str] = None


@step
def huggingface_hub_dataset_loader(
    params: HuggingfaceHubDatasetLoaderStepParameters,
) -> DatasetDict:
    """Download datasets from the Huggingface Hub.

    Args:
        params: Parameters for the Huggingface Hub Dataset Loader Step.

    Returns:

    """
    return load_dataset(
        path=params.dataset_name, name=params.dataset_configuration
    )
