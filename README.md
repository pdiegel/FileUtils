# File Baseclass

This Python module provides the `File` class, which represents a generic Windows file. It includes methods for retrieving information about the file, such as its type, name, size, and creation and modification dates.

## Usage

To use this module, simply create an instance of the `File` class, passing in the path to the file as a string argument:

pythonCopy code

`from file import File  file = File("C:\\path\\to\\file.txt")`

You can then use the following methods and properties to retrieve information about the file:

### `file_type`

Returns the file type of the file.

pythonCopy code

`print(file.file_type)  # "txt"`

### `file_name`

Returns the file name of the file.

pythonCopy code

`print(file.file_name)  # "file"`

### `exists`

Returns `True` if the file exists, `False` otherwise.

pythonCopy code

`print(file.exists)  # True`

### `file_size`

Returns the file size in bytes. Raises a `FileNotFoundError` if the file does not exist.

pythonCopy code

`print(file.file_size)  # 12345`

### `creation_date`

Returns the creation date of the file as a string. Raises a `FileNotFoundError` if the file does not exist.

pythonCopy code

`print(file.creation_date)  # "05/05/2023 10:30:15"`

### `modification_date`

Returns the modification date of the file as a string. Raises a `FileNotFoundError` if the file does not exist.

pythonCopy code

`print(file.modification_date)  # "05/05/2023 10:30:15"`

### `__repr__()`

Returns a string representation of the file.

pythonCopy code

`print(repr(file))  # "File(C:\\path\\to\\file.txt)"`

### `__str__()`

Returns a string representation of the file.

pythonCopy code

`print(str(file))  # "C:\\path\\to\\file.txt"`

### `__len__()`

Returns the file size in bytes. Raises a `FileNotFoundError` if the file does not exist.

pythonCopy code

`print(len(file))  # 12345`

# RedStakeFile Class

This Python module provides the `RedStakeFile` class, which represents a Red Stake Surveyors file. It is a subclass of the `File` class and provides additional methods and properties for working with Red Stake files.

## Usage

To use this module, simply create an instance of the `RedStakeFile` class, passing in the path to the file as a string argument:

pythonCopy code

`from redstakefile import RedStakeFile  file = RedStakeFile("C:\\path\\to\\file.dwg")`

You can then use the following methods and properties to retrieve information about the file:

### `file_number`

Returns the 8-digit file number of the Red Stake file. Reformats the number if necessary.

pythonCopy code

`print(file.file_number)  # "23040186"`

### `file_year`

Returns the year of the Red Stake file.

pythonCopy code

`print(file.file_year)  # "23"`

### `file_month`

Returns the month of the Red Stake file.

pythonCopy code

`print(file.file_month)  # "04"`

### `file_destination_dir`

Returns the destination directory of the Red Stake file. This is the directory to which the file should be moved based on its file type and file number.

pythonCopy code

`print(file.file_destination_dir)  # "\\server\dwg\23dwg\04"`

### `relocate_files()`

This function relocates all Red Stake files in the specified source directory to their destination directories on the server.

pythonCopy code

`from redstakefile import relocate_files  relocate_files("C:\\path\\to\\source\\directory")`

## Requirements

This module requires Python 3.x and the `os` and `shutil` modules, which are included in the Python standard library. It also requires the `File` class from the `file` module in the same repository.

## License

This module is released under the MIT license. See LICENSE for more details.