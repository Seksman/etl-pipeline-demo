def extract_data(path = "data/input.csv"):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    # This changes are done to test Feature Extract branch.
    # This is second changes are done to test Feature Extract branch.

    return rows