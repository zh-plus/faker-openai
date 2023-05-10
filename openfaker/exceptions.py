class OpenaiApiKeyNotFoundException(Exception):
    """Raised when the OpenAI API key is not passed or not found in the environment variables."""

    def __init__(self):
        super().__init__(
            "OpenAI API key not found. Please use setup your api key by `setup_openai(<API-KEY>)`"
            " or set it as an environment variable `OPENAI_API_KEY`."
        )
