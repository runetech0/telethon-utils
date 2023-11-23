import setuptools

required_packages = [
    "aiohttp",
]

NAME = "telethon_utils"

setuptools.setup(
    name=NAME,
    version="0.1.0",
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="Useful helper util functions for telethon",
    url="",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
    package_data={NAME: ["py.typed"]}
)
