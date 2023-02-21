from zenml.steps import step


@step
def my_step():
    print("Hello world!")
