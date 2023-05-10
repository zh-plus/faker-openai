from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='openfaker',
    packages=find_packages(exclude=[]),
    version='0.0.1',
    license='MIT',
    description='Generate fake data with OpenAI\'s GPT-3 API.',
    author='Hao Zheng',
    author_email='zhenghaosustc@gmail.com',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/zh-plus/faker-openai',
    keywords=[
        'openai-gpt3',
        'fake-data',
        'data generation'
    ],
    install_requires=[
        'openai',
        'pycountry',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        "Operating System :: OS Independent",
    ],
)
