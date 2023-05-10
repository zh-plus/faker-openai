# OpenFaker

*OpenFaker* is a Python package that utilizes OpenAI's GPT series model to generate fake data.

**This new project is rapidly underway, and we welcome any issues or pull requests.**

## Basic Usage

Install with pip:

```shell
pip install openfaker
```

Use `faker.Faker()` to create and initialize a faker generator, which can generate data by accessing properties named
after the type of data you want.

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