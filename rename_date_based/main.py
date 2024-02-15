import os

directory_path = os.getcwd()

def rename_files(directory_path, old_name, new_name):
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory_path):
        # Check if the file name contains the specified substring
        if old_name in filename:
            # Construct the new file name by replacing the old substring
            new_filename = filename.replace(old_name, new_name)

            # Create the full file paths for the old and new names
            old_filepath = os.path.join(directory_path, filename)
            new_filepath = os.path.join(directory_path, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {filename} to {new_filename}')

# Example usage:
old_name = 'weee.txt'
new_name = 'new'

rename_files(directory_path, old_name, new_name)