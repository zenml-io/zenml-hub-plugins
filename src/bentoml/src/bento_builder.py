#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
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
"""Implementation of the BentoML bento builder step."""
import importlib
import os
from typing import Any, Dict, List, Optional

import bentoml
from bentoml import bentos
from bentoml._internal.bento import bento

from zenml.integrations.bentoml.constants import DEFAULT_BENTO_FILENAME
from zenml.logger import get_logger
from zenml.materializers import UnmaterializedArtifact
from zenml.steps import BaseParameters, step
from zenml.steps.step_context import StepContext
from zenml.utils import source_utils
from zenml.utils.materializer_utils import load_artifact

logger = get_logger(__name__)


class BentoMLBuilderParameters(BaseParameters):
    """BentoML Bento builder step parameters.

    Attributes:
        service: the name of the BentoML service to be deployed.
        model_name: the name of the model to be packaged.
        model_type: the type of the model.
        version: the version of the model if given.
        labels: the labels of the model if given.
        description: the description of the model if given.
        include: the files to be included in the BentoML bundle.
        exclude: the files to be excluded from the BentoML bundle.
        python: dictionary for configuring Bento's python dependencies,
        docker: dictionary for configuring Bento's docker image.
    """

    service: str
    model_name: str
    model_type: str
    version: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    description: Optional[str] = None
    include: Optional[List[str]] = None
    exclude: Optional[List[str]] = None
    python: Optional[Dict[str, Any]] = None
    docker: Optional[Dict[str, Any]] = None
    working_dir: Optional[str] = None


@step
def bento_builder_step(
    model: UnmaterializedArtifact,
    params: BentoMLBuilderParameters,
    context: StepContext,
) -> bento.Bento:
    """Build a BentoML Model and Bento bundle.

    This steps takes a model artifact of a trained or loaded ML model in a
    previous step and save it with BentoML, then build a BentoML bundle.

    Args:
        model: the model to be packaged.
        params: the parameters for the BentoML builder step.
        context: the step context.

    Returns:
        the BentoML Bento object.
    """
    # save the model and bento uri as part of the bento labels
    labels = params.labels or {}
    labels["model_uri"] = model.uri
    labels["bento_uri"] = os.path.join(
        context.get_output_artifact_uri(), DEFAULT_BENTO_FILENAME
    )

    # Load the model from the model artifact
    model = load_artifact(model)

    # Save the model to a BentoML model based on the model type
    try:
        module = importlib.import_module(f".{params.model_type}", "bentoml")
        module.save_model(params.model_name, model, labels=params.labels)
    except importlib.metadata.PackageNotFoundError:
        bentoml.picklable_model.save_model(
            params.model_name,
            model,
        )

    # Build the BentoML bundle
    bento = bentos.build(
        service=params.service,
        version=params.version,
        labels=labels,
        description=params.description,
        include=params.include,
        exclude=params.exclude,
        python=params.python,
        docker=params.docker,
        build_ctx=params.working_dir or source_utils.get_source_root(),
    )

    # Return the BentoML Bento bundle
    return bento
