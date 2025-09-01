import csv, glob
out = open("merged.csv", "w", newline="", encoding="utf-8")
writer = None
for path in glob.glob("*.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        if writer is None:
            writer = csv.DictWriter(out, fieldnames=r.fieldnames)
            writer.writeheader()
        for row in r:
            writer.writerow(row)
out.close()
print("OK -> merged.csv")
