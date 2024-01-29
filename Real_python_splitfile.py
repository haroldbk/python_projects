from pathlib import Path
path = Path("C:\\Users\\haroldk\\Downloads\\techcrunch.csv")
#"C:\\Users\\haroldk\\Downloads\\techcrunch.csv"
with open(path) as f:
    for l in f:
        sp=l.split()
        print (sp)
          