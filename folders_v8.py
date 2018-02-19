import os

file_path = os.chdir(input('Where would you like to create the directories?: '))
cwd = os.getcwd(os.chdir(input('Where would you like to create the directories?: ')))
print(file_path)

"""
directory = os.path.dirname(file_path)

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
    os.makedirs(directory)
"""
