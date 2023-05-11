# OpenFaker

*OpenFaker* is a Python package that utilizes OpenAI's GPT series model to generate fake data.

**This new project is rapidly underway, and we welcome any issues or pull requests.**

## Basic Usage

Install with pip:

```shell
pip install openfaker
```

To generate data, create and initialize a faker generator using the `faker.Faker()` method. Access properties named after the type of data you want to generate.

```python
from openfaker import Faker
from openfaker.utils import setup_openai

setup_openai('<api-key>')  # Get your API key from https://platform.openai.com/account/api-keys

faker = Faker()
faker.name()
# 'John Doe'

faker.address(2)
# ['426 Jordy Lodge', 'Cartwrightshire, SC 88120-6700']
```

## Todo

- Add basic faker data types (reference to [faker-js](https://github.com/faker-js/faker) and [faker-python](https://github.com/joke2k/faker))
    - [ ] Fine-grained address (city, country, street, etc.)
    - [ ] Fine-grained name (first name, last name, job, etc.)
    - [ ] Color
    - [ ] Company
    - [ ] Internet
    - [ ] Image
- [ ] Store commonly used fake data locally to avoid calling the OpenAI API for small amounts of data.
- [ ] Test the stability of the prompt.

## Credits

- https://github.com/faker-js/faker
- https://github.com/joke2k/faker
- https://github.com/openai/openai-python
- https://github.com/flyingcircusio/pycountry
