"""Some helpful utility functions for working with csv files."""

from csv import DictReader
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r" , encoding="utf8")
    # read the file. 
    # open a handle to the data file

    csv_reader = DictReader(file_handle)
    # prepare to read data file as csv rather than string.

    for row in csv_reader:
        # read each row of csv line by line.
        result.append(row)



    file_handle.close()
    # close file when  done to free its resources. 
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single coloumn."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result

def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oirented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result 