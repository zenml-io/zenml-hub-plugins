# Llama Index Hub Loader Steps
This includes a step to load documents using the Llama Index Hub document loaders, as described more fully
[in their official documentation](https://llamahub.ai/).

To use the step, you must pass in custom parameters to the step to define
exactly which document loader you want to use, and how you want to use it. For
example, to use the Discord loader, you would use the step in the following way:

```python
params = LlamaIndexLoaderParameters(
    loader_name="DiscordReader",
    authentication_kwargs={"discord_token": "<TOKEN_GOES_HERE>"},
    loader_custom_kwargs={"channel_ids": ["<CHANNEL_ID_GOES_HERE>"]},
)

discord_loader = llama_index_loader_step(params=params)
```
