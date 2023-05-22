import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="blackbaud",
    version="1.0.0-alpha",
    author="Ömer Boratav",
    author_email="oboratav@stjohns.bc.ca",
    description="A python module to make the SKY API easier to work with",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjs-bc/python-blackbaud",
    license="AGPLv3",
    project_urls={"Bug Tracker": "https://github.com/sjs-bc/python-blackbaud/issues"},
    packages=["blackbaud"],
    install_requires=[
        "requests",
        "requests-oauthlib",
        "requests-cache[json,redis]",
        "limits",
        "lxml",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
