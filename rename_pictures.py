"""
This script names all images in the specified folder in a uniform format by their creation date.
It only supports .jpg files.

Example:
    path_folder = input('Enter the path of your folder: ')
    print(rename_folder(path_folder))

Todo:
    * add support for more file types (.nef, .png)
"""


import os
import errno
from PIL import Image

def rename_pictures(path_folder):
    '''Rename pictures by their creation date.

    Args:
        path_folder (str): Path of the folder

    Raises:
        FileNotFoundError: Folder not exists
        
    Return:
        list_unprocessed: Return list of all files that could not be renamed 
    '''
    
    dic_name_index = {}
    list_unprocessed = []
    
    # check folder path
    if not os.path.exists(path_folder):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path_folder)
    
    # iterate through the folder for rename the pictures
    for file in os.listdir(path_folder):
    
        file_path = path_folder + '\\' + file
        
        # check file type
        if os.path.splitext(file)[1].lower() == '.jpg':
            
            # get creation date 
            creation_date = (Image.open(file_path).getexif()[36867])
            parsed_date = creation_date[:10].replace(':','')
            
            # check if creation date exists in dictionary
            index = 1
            if parsed_date in dic_name_index:
                index = dic_name_index.get(parsed_date)
                index = index + 1  
            dic_name_index[parsed_date] = index

            # rename file (format: yyyymmdd_00x)
            newfilename = path_folder + '\\' + parsed_date + '_' + (('0')*(3-len(str(index)))) + str(index) + os.path.splitext(file)[1]
            os.rename(file_path, newfilename)             
        else:
            list_unprocessed.append(file_path)
    
    return list_unprocessed