import setuptools

required_packages = [
    "aiohttp",
]


setuptools.setup(
    name="telethon_utils",
    version="0.1.0",
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="Some helper utils for telethon",
    url="",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
)
