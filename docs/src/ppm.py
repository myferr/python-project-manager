import os
import sys
import inquirer
import pyfiglet
from colorama import Fore, Back, Style

def os_do(dothis):
    os.system(dothis)

def ppm(arg):
    
    if ( arg == "about" ):
        print(pyfiglet.figlet_format("Python-Project-Manager"))
        print(">>>>Python-Project-Manager (PPM) is a command-line tool for python project management.")
        print(f"Documentation and help are provided at:{Fore.LIGHTBLUE_EX} https://github.com/myferr/python-project-manager/docs/ {Style.RESET_ALL}")
        
    if ( arg == "setup" ):
        questions = [
            inquirer.List(
                "project-type",
                message="What type of project do you want to setup",
                choices=["default", "github-project", "personal-project"],
            ),
        ]

        answers = inquirer.prompt(questions)
        if (answers['project-type'] == "default"):
            os.mkdir("src")
            os_do("echo print('Hello, world!') > ./src/main.py")
            project_type = "default"
            print(f"{Fore.LIGHTYELLOW_EX} Project type: {Fore.LIGHTCYAN_EX}{project_type}{Style.RESET_ALL} | './src', './src/main.py' created.")
        if (answers['project-type'] == "github-project"):
            project_type = "github-project"
            os.mkdir("src")
            os_do("echo print('Hello, world!') > ./src/main.py")
            os_do("echo . > .gitignore")
            os_do("echo . > project.toml")
            os_do("echo # Hello, world! > README.md")
            project_type = "personal-project"
            print(f"{Fore.LIGHTYELLOW_EX} Project type: {Fore.LIGHTCYAN_EX}{project_type}{Style.RESET_ALL} | './src', './src/main.py', 'project.toml', '.gitignore', 'README.md' created.")
        if (answers['project-type'] == "personal-project"):
            os.mkdir("src")
            os_do("echo print('Hello, world!') > ./src/main.py")
            project_type = "personal-project"
            print(f"{Fore.LIGHTYELLOW_EX} Project type: {Fore.LIGHTCYAN_EX}{project_type}{Style.RESET_ALL} | './src', './src/main.py' created.")
    if ( arg == "help" ):
        print(f"For help and information go to:{Fore.LIGHTBLUE_EX} https://github.com/myferr/python-project-manager/README.md {Style.RESET_ALL}")
    
    if ( arg == "get" ):
        os_do(f"pip install {sys.argv[2]}")
        
    if ( arg == "gh-clone" ):
        os_do(f"git clone {sys.argv[2]}")
        
ppm(sys.argv[1])
