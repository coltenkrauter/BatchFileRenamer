import os.path
import time
from datetime import datetime
from PIL import Image

# TODO create a list of file types/extensions to be avoided
# TODO create a list of file types/extensions that will be the only files renamed
# TODO allow for location to be specified
# TODO allow for name format to be specified or chosen from a list


folder = 'test'
log = open('log.txt', 'a')

def date_taken(folder):
    date_taken = Image.open(folder)._getexif()[36867]
    return datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d h%Hm%Ms%S")

for root, dirs, files in os.walk(folder):
    print(len(files))
    for i, file in enumerate(files):
        old_file = os.path.join(root, file)
        old_filename, file_extension = os.path.splitext(old_file)
        message = ''
        try:
            filename = root + '\\' + \
                date_taken(old_file) + ' id' + str(i + 1) + \
                file_extension.lower()
            message = 'Date Taken: ' + filename + ' / ' + str(i) + ' of ' + str(len(files))
        except:
            filename = root + '\\' + time.strftime("%Y-%m-%d h%Hm%Ms%S", time.gmtime(
                os.path.getmtime(old_file))) + ' id' + str(i + 1) + file_extension.lower()
            message = 'Date Modified: ' + filename + ' / ' + str(i) + ' of ' + str(len(files))
        log.write(message + '\n')
        print(message)
        os.rename(old_file, filename)

log.write('\n\n')
log.close()