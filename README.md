## Description

This script sorts files into subfolders based on their extensions. The script is asynchronous, allowing for efficient file operations.

## Requirements

- `aiopath` library
- `aioshutil` library

## Installation

Install the required libraries using pip:

```sh
pip install aiopath aioshutil
```

## Usage

Run the script with the following command:

```sh
python main.py <source_folder> <output_folder>
```

- `<source_folder>`: The folder containing the files to be sorted.
- `<output_folder>`: The folder where the sorted files will be placed.
- The script will create subfolders in the output folder based on the file extensions.

## Example

```sh
python main.py ./source_folder ./output_folder
```

This will sort the files in the `source_folder` into subfolders in the `output_folder` based on their extensions.