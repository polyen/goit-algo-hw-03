import argparse
import os
import shutil


def copy_file(name, path, destination):
    ext = str.split(name, '.').pop()

    dst_path = os.path.join(destination, ext)
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    try:
        shutil.copyfile(path, os.path.join(dst_path, name))
    except shutil.SameFileError:
        print(f'File {name} was not copied due it is in the same place')
    except OSError:
        print(f'Cannot copy {name} file due to OS limitation')
    except:
        print(f'Unknown error occurs while copying file {name}')


def copy_folder(folder, destination='dist'):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path):
            copy_file(item, item_path, destination)
        else:
            copy_folder(item_path, destination)


def parse_input():
    parser = argparse.ArgumentParser(description="Copy script")

    parser.add_argument("-s", "--source", dest="source", help='Folder from which to copy', required=True)
    parser.add_argument("-d", "--destination", dest="destination", help='Folder where to copy. Default is "dist"')
    args = parser.parse_args()

    output = args.source[1:] if args.source.startswith('/') else args.source
    dest = 'dist'

    if args.destination:
        dest = args.destination[1:] if args.destination.startswith('/') else args.destination

    return output, dest


def create_destination_folder(dest):
    if not os.path.exists(dest):
        os.mkdir(dest)


def main():
    try:
        output, dest = parse_input()
    except TypeError:
        print('Incorrect input, please check for arguments')
        return

    out = os.path.join(os.getcwd(), str(output))
    dest = os.path.join(os.getcwd(), dest)

    try:
        create_destination_folder(dest)
    except FileNotFoundError:
        print(f'Output directory {dest} cannot be created')
        return

    copy_folder(out, dest)


if __name__ == "__main__":
    main()
