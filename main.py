import os
import sys
import subprocess
import platform

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(path):
        with open(path, 'w') as f:
            pass  # Create an empty file
        print(f"Created file: {path}")

def parse_structure(structure_file):
    structure = []
    path_stack = []

    with open(structure_file, 'r') as f:
        for line in f:
            depth = line.count('│') + line.count('    ')
            item = line.strip().strip('│├└─ ')

            # Adjust the path stack based on the current depth
            path_stack = path_stack[:depth]

            if item.endswith('/'):
                # It's a directory
                path_stack.append(item[:-1])
            else:
                # It's a file
                full_path = os.path.join(*path_stack, item)
                structure.append(full_path)

    return structure

def process_structure(structure, root_dir):
    for path in structure:
        full_path = os.path.join(root_dir, path)
        if path.endswith('/'):
            create_directory(full_path)
        else:
            create_file(full_path)

def open_file_explorer(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", path])
    else:  # Linux and other Unix-like
        subprocess.Popen(["xdg-open", path])

def find_file(root_dir):
    while True:
        filename = input("Enter the name of the file you want to open (or 'q' to quit): ")
        if filename.lower() == 'q':
            break
        
        for root, dirs, files in os.walk(root_dir):
            if filename in files:
                file_path = os.path.join(root, filename)
                print(f"File found: {file_path}")
                open_file = input("Do you want to open this file? (y/n): ")
                if open_file.lower() == 'y':
                    open_file_explorer(file_path)
                return
        
        print(f"File '{filename}' not found in the project directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <structure_file.txt>")
        sys.exit(1)

    structure_file = sys.argv[1]
    
    project_name = input("Enter the project name: ")
    project_location = input("Enter the directory where you want to create the project: ")
    
    output_directory = os.path.join(project_location, project_name)
    
    structure = parse_structure(structure_file)
    process_structure(structure, output_directory)
    print(f"Project structure generated in {output_directory}")
    
    
    print("Project generation completed.")