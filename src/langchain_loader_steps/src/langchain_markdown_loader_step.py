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


from typing import Optional, List, Union

from datasets import DatasetDict, load_dataset
from zenml.steps import BaseParameters, step
from langchain.docstore.document import Document
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import UnstructuredMarkdownLoader


class LangchainMarkdownLoaderStepParameters(BaseParameters):
    """Parameters for the Langchain Markdown Loader Step.

    Attributes:
        file_path: Path to the Markdown file to be loaded.
    """

    file_path: str


@step
def langchain_markdown_document_loader(
    params: LangchainMarkdownLoaderStepParameters,
) -> List[Document]:
    """Load markdown files as langchain documents.

    Args:
        params: Parameters for the Langchain Markdown Loader Step.

    Returns:
        List of documents.
    """
    loader = UnstructuredMarkdownLoader(params.file_path)
    return loader.load()
