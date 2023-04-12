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
from langchain.document_loaders import NotionDirectoryLoader
from zenml.steps import BaseParameters, step


class LangchainNotionLoaderStepParameters(BaseParameters):
    """Parameters for the Langchain Notion Loader Step.

    See Langchain documentation for more information here: https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/notion.html

    Attributes:
        file_path: Path to the Notion file to be loaded.
    """

    file_path: str


@step
def langchain_notion_document_loader_step(
    params: LangchainNotionLoaderStepParameters,
) -> List[Document]:
    """Load Notion database files as langchain documents.

    Args:
        params: Parameters for the Langchain Notion Loader Step.

    Returns:
        List of documents.
    """
    loader = NotionDirectoryLoader("Notion_DB")
    return loader.load()
