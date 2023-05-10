import json
import os
import openai

from openfaker.exceptions import OpenaiApiKeyNotFoundException


def get_api_key():
    return os.environ.get("OPENAI_API_KEY")


def setup_openai(api_key):
    if api_key:
        openai.api_key = api_key
    elif api_key := get_api_key():
        openai.api_key = api_key
    else:
        raise OpenaiApiKeyNotFoundException()


def check_openai():
    try:
        openai.Model.list()
    except openai.error.AuthenticationError:
        raise OpenaiApiKeyNotFoundException()


def json2dict(json_str):
    """ Convert json string to python dict. """
    # print(json_str)
    return json.loads(json_str)
