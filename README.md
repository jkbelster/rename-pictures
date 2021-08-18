# rename pictures
Python script that names all images in the specified folder in a uniform format by their creation date.

## How to use
This script is using the Image module of the Python Imaging Library (PIL). You have to install it first:
```
pip install pillow
```
By calling the method *rename_pictures* and passing the path to your folder you can use the script.
```
rename_pictures(path_folder)
```
This function returns a list of files that could not be renamed due to an incorrect file type, for example.

## To do
At the moment this script only supports .jpg files.
Support for .png and .nef files (Nikon raw image file).

## License
[MIT](https://github.com/jkbelster/rename-pictures/blob/main/LICENSE)

