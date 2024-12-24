from setuptools import setup, find_packages

setup(
    name="letter-sort-game",
    version="1.0.0",
    author="Kaal",
    description="A CLI-based letter sorting game.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "letter-sort=game.main:main"
        ]
    },
    install_requires=["tabulate"],
    python_requires=">=3.6",
)
