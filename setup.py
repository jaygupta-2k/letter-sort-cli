from setuptools import setup, find_packages

setup(
    name="color-sort-game",
    version="1.0.0",
    author="Kaal",
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
