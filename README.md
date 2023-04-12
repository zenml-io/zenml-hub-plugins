# Official ZenML Hub Plugins

## Templates

- **plugin_template**: [ZenML Hub plugin template](https://github.com/zenml-io/zenml-hub-plugin-template) 
that can be used as a starting point for building new plugins
- **project_template**: Tool to auto-generate the basic scaffolding for new 
ZenML projects using `zenml init --template`

## Steps

### Loading Datasets

- **sklearn_dataset_steps**: Steps for loading popular datasets from `sklearn.datasets`
    - Digit: `sklearn_digits_loader_step`
    - Iris: `sklearn_iris_loader_step`
    - Diabetes: `sklearn_diabetes_loader_step`
    - Breast Cancer Wisconsin: `sklearn_breast_cancer_loader_step`
    - Wine: `sklearn_wine_loader_step`
    - OpenML: `sklearn_openml_loader_step`
- **torchvision_dataset_steps**: Steps for loading popular computer vision datasets from `torchvision.datasets`
    - MNIST: `pytorch_mnist_loader_step`
    - Fashion-MNIST: `pytorch_fashion_mnist_loader_step`
    - CIFAR-10: `pytorch_cifar10_loader_step`
    - CIFAR-100: `pytorch_cifar100_loader_step`
- **tensorflow_dataset_steps**: Steps for loading popular computer vision datasets from `tf.keras.datasets`
    - CIFAR-10: `tensorflow_cifar10_loader_step`
    - CIFAR-100: `tensorflow_cifar100_loader_step`
    - Fashion-MNIST: `tensorflow_fashion_mnist_loader_step`
    - IMDB: `tensorflow_imdb_loader_step`
    - MNIST: `tensorflow_mnist_loader_step`
    - Reuters: `tensorflow_reuters_loader_step`
- **huggingface_hub_steps**: Steps for loading datasets from the [HuggingFace Hub](https://huggingface.co/datasets)
    - Hub Dataset Loader: `huggingface_hub_loader_step`

### Using Stack Components

#### Model Deployers

- **bentoml_steps**:
    - `bento_builder_step`
    - `bentoml_model_deployer_step`
- **kserve_steps**: 
    - `kserve_model_deployer_step`
    - `kserve_custom_model_deployer_step`
- **mlflow_steps**: 
    - `mlflow_model_deployer_step`
    - `mlflow_model_registry_deployer_step`
- **seldon_steps**: 
    - `seldon_model_deployer_step`
    - `seldon_custom_model_deployer_step`
    - `seldon_mlflow_registry_deployer_step`

#### Data Validators

- **deepchecks_steps**: 
    - `deepchecks_data_drift_check_step`
    - `deepchecks_data_integrity_check_step`
    - `deepchecks_model_drift_check_step`
    - `deepchecks_model_validation_check_step`
- **evidently_steps**: 
    - `evidently_profile_step`
    - `evidently_report_step`
    - `evidently_test_step`
- **great_expectations_steps**: 
    - `great_expectations_profiler_step`
    - `great_expectations_validator_step`
- **whylogs_steps**: 
    - `whylogs_profiler_step`

#### Data Annotators

- **label_studio_steps**: 
    - `get_or_create_dataset`
    - `get_labeled_data`
    - `sync_new_data_to_label_studio`

#### Slack

- **slack_steps**:
    - `slack_alerter_post_step`
    - `slack_alerter_ask_step`
