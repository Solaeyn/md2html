from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="md2html",
    version="1.0.0",
    author="Solaeyn",
    description="A powerful CLI tool to convert Markdown files to beautifully styled HTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Solaeyn/md2html",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["styles/*.css", "styles/*.html"],
    },
    entry_points={
        "console_scripts": [
            "md2html=src.md2html:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=[
        "markdown>=3.3.0",
        "Jinja2>=3.0.0",
        "Pygments>=2.8.0",
    ],
) 