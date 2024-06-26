import os
import argparse

def find_files_by_partial_names(root_dir, partial_names):
    matching_files = []
    for partial_name in partial_names:
        [print(i,end='\r') for i in ['>>','>>>','>>>>']]
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if partial_name in filename:
                    full_path = os.path.join(dirpath, filename)
                    matching_files.append(full_path)
    return matching_files

def read_partial_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def write_matching_paths(file_path, matching_paths):
    with open(file_path, 'w') as file:
        for path in matching_paths:
            file.write(path + '\n')

def main():
    parser = argparse.ArgumentParser(description='Find files by partial names and output their paths.')
    parser.add_argument('input_file', help='The input file containing partial filenames.')
    parser.add_argument('--root_directory', default=os.getcwd(), help='The root directory to start searching from. Default is the current working directory.')
    parser.add_argument('--output_file', default='output.txt', help='The output file to write matching file paths to. Default is output.txt.')

    args = parser.parse_args()

    root_directory = args.root_directory
    input_file = args.input_file
    output_file = args.output_file

    partial_names = read_partial_names(input_file)
    matching_file_paths = find_files_by_partial_names(root_directory, partial_names)
    write_matching_paths(output_file, matching_file_paths)

    print(f'Matching file paths have been written to {output_file}')

if __name__ == '__main__':
    main()
