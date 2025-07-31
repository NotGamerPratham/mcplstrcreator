from setuptools import setup, find_packages

setup(
    name="mc-plugin-strcreator",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "mc-plugin-create = mc_plugin_strcreator.cli:main"
        ]
    },
    author="NotGamerPratham",
    author_email="contact@notgamerpratham.com",
    description="A tool to scaffold Minecraft plugin structure with pom.xml and Main.java",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NotGamerPratham/mcplstrcreator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
