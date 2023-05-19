import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="blackbaud",
    version="0.0.1",
    author="Ömer Boratav",
    author_email="oboratav@stjohns.bc.ca",
    description="A python module to make the SKY API easier to work with",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjs-bc/python-blackbaud",
    project_urls={"Bug Tracker": "https://github.com/sjs-bc/python-blackbaud/issues"},
    packages=["blackbaud"],
    install_requires=["requests", "requests-oauthlib", "requests-cache[json,redis]", "limits", "lxml"],
)
