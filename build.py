import os

home_path = os.path.abspath(".")
os.chdir(home_path)

with open('run.cmd', 'w') as _file:
    _file.write('cd '+home_path+"\n")
    _file.write("python main.py")
