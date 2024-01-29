import pathlib


def path_parts(path):
    print(f"{path}\n")

    print(f"Drive: {path.drive}")
    print(f"Root: {path.root}")
    print(f"Anchor: {path.anchor}")

    print(f"Parent: {path.parent}\n")
    for i, parent in enumerate(path.parents):
        print(f"Parents [{i}]: {parent}")

    print(f"Name: {path.name}")
    print(f"Suffix: {path.suffix}")
    for i, suffix in enumerate(path.suffixes):
       print(f"Suffixes [{i}]: {suffix}")
       print(f"Stem: {path.stem}\n")

#D3EASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/*+\99999999999999999---------------------+++++++++++++++++++++++++++++++++++++-
path_parts(pathlib.PureWindowsPath("D:/PythonTestSamples/listings.txt"))
path_parts(pathlib.PureWindowsPath('C:/Windows/System/python37.dll'))
path_parts(pathlib.PurePosixPath('/usr/lib/x86_64-linux-gnu/libpython3.7m.so.1'))