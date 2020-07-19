import os
cwd = str(os.getcwd())
print(cwd)

uneditPath = '{0}'.format(cwd)

path = uneditPath.split('lib\\run_scripts',1)[0]
    
print(path)
