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
from langchain.document_loaders import NotionDirectoryLoader
from langchain.document_loaders import YoutubeLoader


class LangchainYoutubeLoaderStepParameters(BaseParameters):
    """Parameters for the Langchain Youtube Loader Step.

    See Langchain documentation for more information here:
    https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/youtube.html

    Note that you may also need to install pytube and/or youtube-transcript-api
    depending on your use case.

    Attributes:
        youtube_url: URL of the Youtube video to be loaded.
    """

    youtube_url: str


@step
def langchain_youtube_document_loader(
    params: LangchainYoutubeLoaderStepParameters,
) -> List[Document]:
    """Load Youtube videos and their transcripts as langchain documents.

    Args:
        params: Parameters for the Langchain YouTube Loader Step.

    Returns:
        List of documents.
    """
    loader = YoutubeLoader.from_youtube_url(
        params.youtube_url, add_video_info=True
    )
    return loader.load()
