import os

def createDir(parent, dir_name):
    path = os.path.join(parent, dir_name)
    if os.path.isdir(parent):
        try:
            os.mkdir(path)
        except FileExistsError:
            print(f'Directory {dir_name} already exist')
        except FileNotFoundError:
            print(f'Path {parent} doesn\'t exist')
        else:
            return path
    return None

root = os.getcwd()
root = createDir(root, "my_project")
if root is None:
    exit(1)
createDir(root, "settings")
createDir(root, "mainapp")
createDir(root, "adminapp")
createDir(root, "authapp")