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


from typing import List

from langchain.docstore.document import Document
from langchain.document_loaders.csv_loader import CSVLoader
from zenml.steps import BaseParameters, step


class LangchainCSVLoaderStepParameters(BaseParameters):
    """Parameters for the Langchain CSV Loader Step.

    Attributes:
        file_path: Path to the CSV file to be loaded.
    """

    file_path: str


@step
def langchain_csv_document_loader_step(
    params: LangchainCSVLoaderStepParameters,
) -> List[Document]:
    """Load csv files with a single row per document.

    Args:
        params: Parameters for the Langchain CSV Loader Step.

    Returns:
        List of documents.
    """
    loader = CSVLoader(file_path=params.file_path)
    return loader.load()
