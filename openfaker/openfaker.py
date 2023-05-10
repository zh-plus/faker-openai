from openfaker.bot import Bot
from openfaker.prompter import NamePrompter, AddressPrompter

from openfaker.utils import json2dict


class Faker:
    def __init__(self):
        self.bot = Bot()

    def name(self, num=1, locale='US'):
        json_str = self.bot.query(NamePrompter(num, locale))
        result = json2dict(json_str)

        # Rationality Assessment
        if result['total_num'] != num:
            raise ValueError(f"Expected {num} names, but got {result['num']} names.")

        return result['list'] if num > 1 else result['list'][0]

    def address(self, num=1):
        json_str = self.bot.query(AddressPrompter(num))
        result = json2dict(json_str)

        # Rationality Assessment
        if result['total_num'] != num:
            raise ValueError(f"Expected {num} addresses, but got {result['num']} addresses.")

        return result['list'] if num > 1 else result['list'][0]
