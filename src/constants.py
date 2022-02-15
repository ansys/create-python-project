# Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use,
# distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
DOT_FILES_TO_RENAME = {'flake8': '.flake8',
                       'gitignore': '.gitignore',
                       'gitattributes': '.gitattributes'}


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


GIT_RECC_LOG = f"""{Colors.OKCYAN}We recommend you track your project using git 
and store it in a remote repository, such as on ADO or GitHub. 
This can be done by following these instructions provided you already have git 
installed.
    1- Navigate to the created project directory on the command line 
    2- Make the directory into a git repo and link it to a remote origin
        2.1 [Optional] -  git init
        2.2 [Optional] -  git remote add origin <git_repository_url>
        2.3 [Optional] -  git add . && git commit -m \"initial commit\"
        2.4 [Optional] -  git push origin main {Colors.OKCYAN} 

"""
