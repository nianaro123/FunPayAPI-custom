from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name="FunPayAPI",
    version="1.1.1",
    description="Custom patched FunPayAPI for personal project deployment.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="nianaro123",
    url="https://github.com/nianaro123/FunPayAPI-custom",
    packages=find_packages("."),
    include_package_data=True,
    license="GPL3",
    keywords="funpay api bot",
    install_requires=[
        "requests>=2.28,<3",
        "beautifulsoup4>=4.12.0",
        "requests_toolbelt>=0.10.1,<2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
    ],
)