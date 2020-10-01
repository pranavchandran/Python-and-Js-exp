import os
from datetime import datetime
# print(dir(os))
# for getting the current working dir
# print(os.getcwd())
# change the working dir command
# os.chdir()
# print(os.listdir())

# os.mkdir('oscheck')
# makedirs will make subdirectories mkdir will not 
# os.makedirs()

# Delete dirs
# os.rmdir('oscheck')
# also u can use subdirs in removedirs
# os.removedirs('.......')

# Renaming files
# os.rename('sample1.csv','hacker.csv') 

# details of a file
# print(os.stat('hacker.csv').st_size)
# mod_time = os.stat('hacker.csv').st_mtime
# print(datetime.fromtimestamp(mod_time))

# printing like a tree
# os.walk()
# for dirpath, dirnames, filenames in os.walk('/home'):
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# print(os.environ.get('HOME'))
# print(os.environ)

# file_path = os.path.join(os.environ.get('HOME'),'teast.txt')
# print(file_path)

# print(os.path.exists('HOME/passwords.txt'))

# isdir and isfile 

print(os.path.splitext('HOME/passwords.txt'))

# .splitext

print(dir(os))

print(os.path.isfile('/home/insphere05/passwords.txt'))

# print(os.listdir('/home/insphere05'))