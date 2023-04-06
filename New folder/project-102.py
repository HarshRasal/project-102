import os
import shutil

directory = 'C:\Python'

# Create subdirectories for each file type
for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
        file_extension = os.path.splitext(file)[1]
        if file_extension != '':
            file_extension = file_extension[1:]
            if not os.path.exists(os.path.join(directory, file_extension)):
                os.mkdir(os.path.join(directory, file_extension))

# Move files to appropriate subdirectory
for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
        file_extension = os.path.splitext(file)[1]
        if file_extension != '':
            file_extension = file_extension[1:]
            shutil.move(os.path.join(directory, file), os.path.join(directory, file_extension, file))
            
