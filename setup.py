"""
...
\n
Copyright © 2023 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import setup

with open("README.md", "r", encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name="mighty_logger",
    version="0.7.0",

    author="Kalynovsky 'Nakamura Akira' Valentin",
    author_email="nakama3942@gmail.com",

    description="Powerful functional logger",
    long_description=readme,
    long_description_content_type="text/markdown",

    url="https://github.com/Nakama3942/mighty_logger",

    license="Apache License, Version 2.0, see LICENSE file",

    packages=[
        'mighty_logger',
        'mighty_logger.src',
        'mighty_logger.basic',
        'mighty_logger.basic.lib_types'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Logging",
    ],
    project_urls={
        'Releases': 'https://github.com/Nakama3942/mighty_logger/releases',
    },
    python_requires='>=3.11',
)
