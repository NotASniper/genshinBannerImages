import os

# Directory with your files (use "." for current directory)
folder = "C:/Users/Semmy/Downloads/CharcterPortraits/characters"

for fname in os.listdir(folder):
    # Only process files that start with "Portraits "
    if fname.startswith("Portraits "):
        new_name = fname.replace("Portraits ", "", 1)  # remove only the first occurrence
        old_path = os.path.join(folder, fname)
        new_path = os.path.join(folder, new_name)
        
        # Rename
        os.rename(old_path, new_path)
        print(f'Renamed: {fname} -> {new_name}')
