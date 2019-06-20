import os
def fuc():
    print(os.getcwd())
def fuc2():
    print(os.path.curdir)
os.makedirs(os.path.join(os.path.curdir,'niubi.txt'))