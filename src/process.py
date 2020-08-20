import os
from PIL import Image, UnidentifiedImageError


def change_DPI(input_dir, output_dir, dpi=(300, 300)):
    if not (os.path.exists(input_dir) and os.path.isdir(input_dir)):
        print(f'No such folder "{input_dir}"!')
        return 1

    if not (os.path.exists(output_dir) and os.path.isdir(output_dir)):
        os.makedirs(output_dir)

    print(f'Watching in folder "{input_dir}":')

    file_count = 0
    success_file_count = 0
    for filename in os.listdir(input_dir):
        file_count += 1
        filepath = os.path.join(input_dir, filename)
        print(f'Trying to open "{filename}"... ', end='')

        if not os.path.isfile(filepath):
            print("Not a file.")
            continue

        try:
            image = Image.open(filepath)
        except UnidentifiedImageError as err:
            print(f"Failed to open {filepath}!")
            continue

        print("Saving... ", end='')
        image.save(os.path.join(output_dir, filename), dpi=dpi)
        print("Done!")
        success_file_count += 1

    print("="*40)

    if file_count:
        print(f"Finished {success_file_count} / {file_count} files!")
        return 0

    print("No files found!")
    return 1
