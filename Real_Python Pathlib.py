#Real_Python Pathlib
from pathlib import Path

print(f"you can see me here: {Path(__file__).parent}")

for file_path in Path.cwd().glob("*.txt"):
    new_path = Path("archive") / file_path.name
    file_path.rename(new_path)
    print(new_path)
