import setuptools
from telethon_utils._metadata import NAME, VERSION

required_packages = [
    "aiohttp",
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="Useful helper util functions for telethon",
    url="https://github.com/rehmanali1337/telethon-utils",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
    package_data={NAME: ["py.typed"]}
)
