from openfaker.bot import Bot
from openfaker.checker import total_num_check
from openfaker.prompter import NamePrompter, AddressPrompter, ColorPrompter


class Faker:
    def __init__(self):
        self.bot = Bot()

    def name(self, num=1, locale='US'):
        result = self.bot.query(NamePrompter(num, locale))

        # Rationality Assessment
        total_num_check(result, num)

        return result['list'] if num > 1 else result['list'][0]

    def address(self, num=1):
        result = self.bot.query(AddressPrompter(num))

        # Rationality Assessment
        total_num_check(result, num)

        return result['list'] if num > 1 else result['list'][0]

    def color(self, num=1, fmt='rgb'):
        result = self.bot.query(ColorPrompter(num))

        # Rationality Assessment
        total_num_check(result, num)

        return result['list'] if num > 1 else result['list'][0]
