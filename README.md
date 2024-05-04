# DISCLAIMER
This project is outdated and has been revamped to [here](https://github.com/myferr/ppm-2.0/)

# Python Project Manager

> [How to install..](docs/Documentation.md)

This is **Python Project Manager** *(PPM)* it's used for managing and creating Python project files. Such as `.gitignore`, `project.toml` and `src` directories.

There are three different kinds of projects in the **PPM Setup Menu**
* `default`
* `github-project`
* `personal-project`

<img src="images/Pasted image 20240208013335.png">

# Arguments

When no arguments are given this error will occur

<img src="images/Pasted image 20240208013432.png">
This is because arguments are necessary!

All **PPM** list of arguments:
* setup
* about
* help
* documentation
* get
* gh-clone
### *ARG:* Setup

When you run the command `python ppm.py setup` you'll be prompted the **PPM Setup Menu**. Once picking a project type you'll be prompted with questions and once they are complete **PPM** will setup and create your project files.
### *ARG:* About

When `python ppm.py about` is ran you're prompted with this:
<img src="images/Pasted image 20240208030208.png">
### *ARG:* Help

When you run `python ppm.py help` you're prompted with a link to this README

### *ARG:* Documentation

When you run `python ppm.py documentation` you're prompted with a link to the [documentation](docs/Documentation.md).

### *ARG:* gh-clone
> `gh-clone` is `git clone`

You use `gh-clone` just like `git clone`. `gh-clone` is used for cloning GitHub repos via *[Git](https://git-scm.com/)*. To use `gh-clone` run the following command: `python ppm.py gh-clone {GITHUB-REPO-URL}`

Replace `{GITHUB-REPO-URL}` with the URL/link of the GitHub repo you want to clone.
> `gh-clone` requires Git
### *ARG:* Get
> `get` is `pip install`

You use `get` just like `pip install`. `get` is used for downloading Python packages/modules via *[Python Pip](https://pypi.org/)*. To use `get` run the following command: `python ppm.py get {PACKAGE/MODULE NAME}`

Replace `{PACKAGE/MODULE NAME}` with the Python package/module name you want to download.
> `get` requires Pip

# Features

What **PPM** offers:
* `get` feature using *[pip](https://pypi.org/)*
* `setup` feature
* Creating project folders
* `gh-clone` feature using *[git](https://git-scm.com/)*
* Easy to read documentation

**PPM** is a very easy-to-use command line.


# Requirements

* *[Python Pip](https://pypi.org/)*
* *[Git](https://git-scm.com/)*
* [Python](https://www.python.org/downloads/)
