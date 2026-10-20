def read_rows(lines):
    header = None
    rows = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        fields = [f.strip() for f in line.split(",")]
        if header is None:
            header = fields
        elif len(fields) == len(header):
            rows.append(dict(zip(header, fields)))
    return rows


def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row["тип"] == kind:
            try:
                total += float(row["минуты"].replace(",", "."))
            except ValueError:
                pass
    return round(total, 1)


def to_csv(counts):
    text = "тип,количество\n"
    for kind in sorted(counts):
        text += kind + "," + str(counts[kind]) + "\n"
    return text