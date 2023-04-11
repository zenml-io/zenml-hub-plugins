#  Copyright (c) ZenML GmbH 2023. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.


from zenml.pipelines import pipeline


@pipeline
def qa_pipeline(document_loader, index_generator, question_answerer):
    """Define a question answering pipeline.

    Args:
        document_loader: A step that loads langchain documents.
        index_generator: A step that generates an index from the documents.
        question_answerer: A step that answers questions based on the index.
    """
    documents = document_loader()
    index = index_generator(documents)
    question_answerer(index)


def build_zenml_docs_qa_pipeline(question: str, load_all_paths: bool = True):
    """Build a question answering pipeline about the ZenML docs.

    Args:
        question: The question to ask.
        load_all_paths: Whether to load all paths or only the introduction.

    Returns:
        A ZenML pipeline that can answer questions about the ZenML docs.
    """
    from src.steps.docs_loader import DocsLoaderParameters, docs_loader_step
    from src.steps.index_generator import index_generator_step
    from src.steps.question_answerer import (
        QAParameters,
        question_answerer_step,
    )

    return qa_pipeline(
        document_loader=docs_loader_step(
            DocsLoaderParameters(load_all_paths=load_all_paths)
        ),
        index_generator=index_generator_step(),
        question_answerer=question_answerer_step(
            QAParameters(question=question)
        ),
    )
