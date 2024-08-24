# Project Structure Generator

This Python script automatically generates a project directory structure based on a provided text file. It's designed to quickly set up the skeleton of a new project, saving time and ensuring consistency in project organization.

## Features

- Automatically reads a project structure from a text file (`example-project-structure.txt`)
- Generates directories and files based on the specified structure
- Supports nested directory structures
- Handles both files and directories
- Simple command-line interface for specifying project name and location

## Requirements

- Python 3.6 or higher

## Usage

1. Ensure that `main.py` and `example-project-structure.txt` are in the same directory.

2. Run the script:
   ```
   python main.py
   ```

3. When prompted, enter:
   - The name for your new project
   - The directory where you want to create the project

4. The script will generate the project structure based on the contents of `example-project-structure.txt`.

## Project Structure File Format

The `example-project-structure.txt` file should use the following format to define the project structure:

- Use `│`, `├`, `└`, and `─` characters to indicate the hierarchy
- End directory names with a `/`
- File names should include their extension

Example:
```
project_root/
├── src/
│   ├── main.go
│   └── utils/
│       └── helper.go
├── tests/
│   └── main_test.go
└── README.md
```

## Notes

- The script will create empty files for all specified files in the structure.
- If a directory in the specified output location already exists, the script will add new files and directories to it without overwriting existing ones.
- Make sure you have write permissions in the directory where you're creating the project.

## Customization

To use a different project structure, simply modify the contents of `example-project-structure.txt` to match your desired project layout.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to submit issues or pull requests.

## License

[Specify your license here, e.g., MIT, GPL, etc.]

