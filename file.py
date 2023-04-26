"""This module contains the File baseclass."""
import datetime
import os


class File:
    """This class represents a generic windows file."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        if not self.exists:
            raise FileNotFoundError(f"File {self.file_path} does not exist")

    @property
    def file_type(self) -> str:
        """Returns the file type of the file."""
        return os.path.splitext(self.file_path)[-1][1:]

    @property
    def file_name(self) -> str:
        """Returns the file name of the file."""
        return os.path.basename(os.path.splitext(self.file_path)[0])

    @property
    def exists(self) -> bool:
        """Returns True if the file exists, False otherwise."""
        return os.path.exists(self.file_path)

    @property
    def file_size(self) -> float:
        """Returns the file size in bytes. Raises FileNotFoundError if
        the file does not exist."""
        if self.exists:
            return os.path.getsize(self.file_path)
        else:
            raise FileNotFoundError(f"File {self.file_path} does not exist")

    @property
    def creation_date(self) -> str:
        """Returns the creation date of the file. Raises
        FileNotFoundError if the file does not exist."""
        if self.exists:
            creation_timestamp = os.path.getctime(self.file_path)
            return self.timestamp_to_date(creation_timestamp)
        else:
            raise FileNotFoundError(f"File {self.file_path} does not exist")

    @property
    def modification_date(self) -> str:
        """Returns the modification date of the file. Raises
        FileNotFoundError if the file does not exist."""
        if self.exists:
            modification_timestamp = os.path.getmtime(self.file_path)
            return self.timestamp_to_date(modification_timestamp)
        else:
            raise FileNotFoundError(f"File {self.file_path} does not exist")

    def timestamp_to_date(
        self,
        time: float,
        time_format: str = "%m/%d/%Y %H:%M:%S",
    ) -> str:
        """Returns a string representation of the date and time from
        a timestamp."""
        return datetime.datetime.fromtimestamp(time).strftime(time_format)

    def __repr__(self) -> str:
        """Returns a string representation of the file."""
        return f"File({self.file_path})"

    def __str__(self) -> str:
        """Returns a string representation of the file."""
        return self.file_path

    def __len__(self) -> int:
        """Returns the file size in bytes. Raises FileNotFoundError if
        the file does not exist."""
        return self.file_size


if __name__ == "__main__":
    file = File(r"C:\Users\redst\Documents\23040186-PROPOSED_PPD.pdf")
    print(f"File type: {file.file_type}")
    print(f"File name: {file.file_name}")
    print(f"File exists: {file.exists}")
    print(f"File size: {file.file_size/1000:.2f} KB")
    print(f"File creation date: {file.creation_date}")
    print(f"File modification date: {file.modification_date}")
    print(f"File: {file}")
    print(f"File: {repr(file)}")
    print(f"File size: {len(file)/1000:.2f} KB")
