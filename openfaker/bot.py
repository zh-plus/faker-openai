import openai

from openfaker.prompter import Prompter
from openfaker.utils import json2dict


class Bot:
    def __init__(self, model='gpt-3.5-turbo'):
        self.model = model

    def message(self, message):
        completion = openai.ChatCompletion.create(model=self.model, messages=[{
            'role': 'user',
            'content': str(message)
        }], )
        return completion.choices[0].message.content

    def query(self, prompter: Prompter):
        json_str = self.message(prompter)
        print(json_str)
        return json2dict(json_str)
