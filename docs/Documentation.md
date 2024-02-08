# The Documentation

Welcome to the **PPM Documentation**! 👋
This is a complete guide on how to use and operate **PPM**.


## How to install..

To install **PPM** you will need Git and use the following command in your terminal / command-line
or you can download this repo manually.

To install **PPM** using Git open your terminal / command line and go to your desktop's directory and use the following command in your terminal / command-line:

```
git clone https://github.com/myferr/python-project-manager/
```

After that go to the `src` directory and use the following command: `python finish.py`! That will let you use `python ppm.py` anywhere in your terminal.

## A Guide to PPM arguments

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


## A Guide to PPM Setup

<img src="Pasted image 20240208052658.png">
> PPM Setup menu

There are three project types.
* `default`
* `github-project`
* `personal-project`

When you select a project type PPM creates the project files and folders that your project type needs.

### How to select project type

To select your project type, run the command to enter the setup menu `python ppm.py setup`
after that you can use your up and down arrow keys ( `^`  `V`) to navigate which project type to choose.

Press enter to select the project type.

### Project files.

**`default` Project Files:**
* `src` - folder
* `main.py` - file (located in `src`)

**`github-project` Project Files:**
* `src` - folder
* `main.py` - file (located in `src`)
* `project.toml` - file
* `.gitignore` - file
* `README.md` - file

**`personal-project` Project Files:**
* `src` - folder
* `main.py` - file (located in `src`)

> *`default` and `personal` are the same project types*
