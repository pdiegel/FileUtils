"""This module contains the DWGFile class. It is a subclass of the File
class."""
import os
import re
import shutil

from file import File


class RedStakeFile(File):
    """This class represents a RedStake file."""

    dwg_dir = r"\\server\dwg"
    asc_dir = r"\\server\ascii"
    cogo_dir = r"\\server\cogo\COGO"
    pdf_dir = r"\\server\access\Scans\Survey Scans"
    file_directories = {
        "dwg": (dwg_dir, "dwg"),
        "asc": (asc_dir, "ASCII"),
        "cgf": (cogo_dir, "COGO"),
        "pdf": pdf_dir,
    }

    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        if (
            file_path.split(".")[-1].lower()
            not in RedStakeFile.file_directories.keys()
        ):
            raise TypeError(f"{self.file_path} is not a valid Red Stake file")

        try:
            self.file_number
        except AttributeError as err:
            raise err

    @property
    def file_number(self) -> str:
        """Returns the 8-digit file number of the Red Stake file. Reformats
        the number if necessary."""
        file_number = re.search(r"^\d{6,8}[^0-9]*$", self.file_name)

        if not self.file_name[0].isnumeric():
            file_number = None

        if file_number:
            file_number = file_number.group(0)
        else:
            raise AttributeError

        valid_months = ("10", "11", "12")
        while len(file_number) < 8:
            month = file_number[2:4]
            if month not in valid_months and month[0] != "0":
                file_number = file_number[:2] + "0" + file_number[2:]
            else:
                file_number = file_number[:4] + "0" + file_number[4:]

        return file_number

    @property
    def file_year(self) -> str:
        """Returns the year of the Red Stake file."""
        try:
            self.file_number
        except AttributeError:
            raise AttributeError(f"File {self.file_path} has no file number")
        else:
            return self.file_number[:2]

    @property
    def file_month(self) -> str:
        """Returns the month of the Red Stake file."""
        try:
            self.file_number
        except AttributeError:
            raise AttributeError(f"File {self.file_path} has no file number")
        else:
            return self.file_number[2:4]

    @property
    def file_type(self) -> str:
        """Returns the file type of the Red Stake file."""
        return self.file_path.split(".")[-1].lower()

    @property
    def file_destination_dir(self) -> os.path:
        """Returns the destination directory of the Red Stake file."""
        final_dir_prefix = self.file_directories[self.file_type]

        if isinstance(final_dir_prefix, tuple):
            final_dir = os.path.join(
                final_dir_prefix[0],
                f"{self.file_year}{final_dir_prefix[1]}",
                self.file_month,
            )
        else:
            final_dir = final_dir_prefix

        if os.path.exists(final_dir):
            return final_dir

        return None


def move_files(source_dir: os.path):
    """Transfers all Red Stake files from the source directory to the server"""
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)

        try:
            red_stake_file = RedStakeFile(filepath)
        except (TypeError, AttributeError):
            continue

        try:
            destination_path = os.path.join(
                red_stake_file.file_destination_dir,
                filename,
            )
        except AttributeError:
            continue
        except TypeError:
            print(
                f"File {filename} in {source_dir} has no destination directory"
            )
            continue
        else:
            if os.path.exists(destination_path):
                print(f"File {destination_path} already exists")
                # Insert logic to delete or rename file.
                continue
            shutil.move(filepath, destination_path)
            del red_stake_file


def main():
    directory_to_scan = r"\\server\ascii"
    for root, dirs, files in os.walk(top=directory_to_scan):
        for directory in dirs:
            current_dir = os.path.join(root, directory)
            print(f'Parsing directory "{current_dir}"')
            try:
                move_files(src_dir=current_dir)
            except PermissionError:
                print(f"Permission error at {current_dir}")
                continue


if __name__ == "__main__":
    main()
