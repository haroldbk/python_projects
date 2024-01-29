#Read_shopping_list
from pathlib import Path
"""
path = Path.cwd()/"shoppinglist.md"
with path.open(mode="r",encoding="utf-8")as md_file:
    content = md_file.read()
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print ("\n".join(groceries))
"""
"""
content = Path("shoppinglist.md").read_text(encoding="utf-8")
groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))

Path("plain_list.md").write_text("\n".join(groceries),encoding="utf-8")
"""
source = Path("shoppinglist.md")
destination = source.with_stem("shoppinglist_02")
destination.write_bytes(source.read_bytes())