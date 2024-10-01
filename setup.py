from setuptools import setup, find_packages

setup(
    name="gryszka_config_package",
    version="0.1.2",
    description="A package to read configuration from a YAML file",
    author="Gryszka",
    author_email="romanowicz.g@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["pyyaml"],
)