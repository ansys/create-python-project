# Copyright (c) 2022, Ansys Inc. Unauthorised use, distribution or duplication is prohibited

# This is a sample Python project
from datetime import datetime


def print_date_and_time():
    # Use a breakpoint in the code line below to debug your script.
    return datetime.today().strftime('%Y-%m-%d-%H:%M:%S')  # Press Ctrl+F8 to toggle the breakpoint if you are using
    # PyCharm.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Hello! Welcome, we are {print_date_and_time()}')
