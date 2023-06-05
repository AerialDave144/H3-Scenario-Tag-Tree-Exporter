import os
import shutil

# Prompt the user to enter the name of the custom directory
def get_custom_dir_path():
    custom_dir = input('Enter the name of the custom directory: ')
    custom_dir_path = os.path.join(os.getcwd(), custom_dir, 'tags')
    try:
        os.makedirs(custom_dir_path)
    except FileExistsError:
        print(f'Error: The directory "{custom_dir_path}" already exists')
        return get_custom_dir_path()
    return custom_dir_path

custom_dir_path = get_custom_dir_path()

# Read the location of the tags folder from 'tags folder location.txt'
print('Reading tags folder location...')
with open('tags folder location.txt', 'r') as f:
    tags_folder_location = f.read().strip()

# Define a list of tags to exclude from 'scenario_tags.txt'
excluded_tags = [
    ".rasterizer_cache_file_globals",
    ".cache_file_resource_layout_table",
    "i've got a lovely bunch of coconuts.sound_cache_file_gestalt",
    "there they are all standing in a row.cache_file_resource_gestalt"
]

# Read the scenario tags from 'scenario_tags.txt'
print('Reading scenario tags...')
with open('scenario_tags.txt', 'r') as f:
    scenario_tags = []
    for line in f:
        tag = line.strip().split('\t')[1]
        if tag not in excluded_tags:
            scenario_tags.append(tag)
        else:
            print(f'Excluding tag: {tag}')

# Read the common tags from 'common_tags.txt'
print('Reading common tags...')
with open('common_tags.txt', 'r') as f:
    common_tags = [line.strip() for line in f.readlines()]

# Compute the list of tags to export
print('Computing tags to export...')
tags_to_export = [tag for tag in scenario_tags if tag not in common_tags]

# Save the list of tags to be exported to 'tags_to_be_exported.txt'
print('Saving tags to be exported...')
with open('tags_to_be_exported.txt', 'w') as f:
    for tag in tags_to_export:
        f.write(tag + '\n')

# Copy the files corresponding to the tags to be exported
print('Copying files...')
missing_tags = []
for tag in tags_to_export:
    src_path = os.path.join(tags_folder_location, tag)
    dst_path = os.path.join(custom_dir_path, tag)
    try:
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy2(src_path, dst_path)
        print(f'Copied file: {tag}')
    except FileNotFoundError:
        print(f'Error: Missing file or directory: {src_path}')
        missing_tags.append(tag)

# Save the list of missing tags to 'debug_missing tags.txt'
if missing_tags:
    print('Saving list of missing tags...')
    with open('debug_missing tags.txt', 'w') as f:
        for tag in missing_tags:
            f.write(tag + '\n')

# Wait for user input before exiting
input('Press Enter to exit...')
