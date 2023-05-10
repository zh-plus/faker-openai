from abc import abstractmethod, ABCMeta
import pycountry as pyc

json_format = {
    'name': '{"total_num": <returned-number>, "list": [<returned-name-list>]}',
    'address': '{"total_num": <returned-number>, "list": [<returned-address-list>]}',
}


class Prompter(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass


class HelloEchoPrompter(Prompter):
    def __str__(self):
        return 'You are a echo bot, start echo: hello'


class NamePrompter(Prompter):
    def __init__(self, num=1, locale='US'):
        self.num = num
        self.locale = locale

    def __str__(self):
        country_name = pyc.countries.get(alpha_2=self.locale).name
        return f'As a fake name generator, please generate {self.num} different {country_name} names at single paragraph.' \
               f' The paragraph have the following format: {json_format["name"]}.' \
               f' DO NOT return any other words before or after that paragraph.' \
               f' DO NOT use ellipses in that paragraph.' \
               f' Use the {country_name} language to generate names.'


class AddressPrompter(Prompter):
    def __init__(self, num=1, locale='US'):
        self.num = num
        self.lang = locale

    def __str__(self):
        country_name = pyc.countries.get(alpha_2=self.lang).name
        return f'As a fake name generator, please generate {self.num} different {country_name} address at single paragraph.' \
               f' The paragraph have the following format: {json_format["address"]}.' \
               f' DO NOT return any other words before or after that paragraph.' \
               f' DO NOT use ellipses in that paragraph.' \
               f' Use the {country_name} language to generate addresses.'
