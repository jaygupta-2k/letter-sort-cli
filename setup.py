"""
This file is part of ColorSort.
Copyright (C) 2024 Jay Gupta.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

See the GNU General Public License for more details.
"""

from setuptools import setup, find_packages

setup(
    name="color-sort-game",
    version="1.0.0",
    author="Jay Gupta",
    description="A CLI-based color sorting game.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "color-sort=game.main:main"
        ]
    },
    install_requires=["tabulate","colorama"],
    python_requires=">=3.6",
)
