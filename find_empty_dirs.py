import os
from pathlib import Path

def find_empty_dirs(root_dir):
    empty_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Check if the directory contains any files or non-ignorable subdirectories
        has_content = False
        # Check for visible files
        if any(f for f in filenames if not f.startswith('.')):
            has_content = True

        # Check for non-ignorable subdirectories (dirnames in os.walk are names in this level)
        # This check needs to be careful with how os.walk works. A simpler way:
        # Check if after visiting subdirs (topdown=False), a dir has no remaining entries other than ignorable ones.

        # Re-list directory contents after os.walk has visited subdirectories
        try:
            items = os.listdir(dirpath)
            ignorable_items = {'__pycache__', '.DS_Store', '.gitkeep'} # Add other common ignored files/dirs here
            
            # Check if all items are ignorable
            all_ignorable = True
            for item in items:
                if item not in ignorable_items:
                    all_ignorable = False
                    break
                    
            if all_ignorable:
                 # Check if it's a directory and it's truly empty or only contains ignorable items
                 # The earlier check 'if any(f for f in filenames if not f.startswith('.'))' handles visible files.
                 # We also need to ensure there are no non-empty subdirectories left.
                 # Since topdown=False, we visit subdirs first. If we are at a dir_path and its listed content
                 # is all ignorable, and it wasn't marked as having content from subdirs (which happens automatically
                 # in os.walk's dirnames/filenames), then it's effectively empty for our purpose.
                 # A simpler check: if the directory contains *only* directories (which would have been visited and potentially removed from dirnames by os.walk if empty) or ignorable files.
                 if not has_content and not any(d in dirnames for d in os.listdir(dirpath) if (Path(dirpath) / d).is_dir() and d not in ignorable_items):
                      empty_dirs.append(str(Path(dirpath).relative_to(root_dir)))

        except OSError:
            # Handle permission errors or other issues reading directory
            continue # Skip this directory if we can't list its contents

    return empty_dirs

if __name__ == "__main__":
    # Assuming the script is run from the project root
    root_directory = Path.cwd()
    print(f"Checking for empty directories in: {root_directory}")
    empty_directories = find_empty_dirs(root_directory)

    if empty_directories:
        print("\nEmpty directories found:")
        for empty_dir in empty_directories:
            print(f"- {empty_dir}")
    else:
        print("\nNo empty directories found (excluding common ignored folders like __pycache__).")

    input("\nPress Enter to exit...") 