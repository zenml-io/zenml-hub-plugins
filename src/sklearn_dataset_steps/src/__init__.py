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

from .sklearn_breast_cancer_loader_step import breast_cancer_data_loader
from .sklearn_diabetes_loader_step import diabetes_data_loader
from .sklearn_iris_loader_step import iris_data_loader
from .sklearn_wine_loader_step import wine_data_loader
from .sklearn_digits_loader_step import digits_data_loader
from .sklearn_openml_loader_step import (
    openml_data_loader,
    OpenMLDataLoaderStepParameters,
)
