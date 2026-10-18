# EXERCISE 1: ENGINEERING TEST DATA ORGANIZER

LAST_NAME = "TABARDILLA"
SEED_NUM = 8
FAVORITE_ARTIST = "ARTHUR NERY"

sources = [f"{LAST_NAME}_T{i}" for i in range(1, 6)]

categories = [
    "TEMPERATURE",
    "VOLTAGE",
    "CURRENT",
    "PRESSURE",
    "SPEED"
]

# Use the artist's letters, excluding spaces.
artist_letters = [ord(ch) for ch in FAVORITE_ARTIST if ch.isalpha()]

# Each category has a starting value and a range.
measurement_rules = {
    "TEMPERATURE": (20, 81),
    "VOLTAGE": (1, 20),
    "CURRENT": (1, 10),
    "PRESSURE": (80, 71),
    "SPEED": (10, 111)
}

records = []

# Generate one measurement for every source/category combination.
for source_index, source in enumerate(sources):
    for category_index, category in enumerate(categories):
        artist_value = artist_letters[
            (source_index + category_index) % len(artist_letters)
        ]

        base, value_range = measurement_rules[category]

        value = base + (
            SEED_NUM
            + artist_value
            + source_index * 7
            + category_index * 11
        ) % value_range

        records.append({
            "source": source,
            "category": category,
            "value": value
        })

# Add one repeated source/category record.
records.append(records[0].copy())

# Organize records by source and category.
organized = sorted(
    records,
    key=lambda record: (record["source"], record["category"])
)

# Identify repeated source/category combinations.
seen = set()
repeated = []

for record in organized:
    key = (record["source"], record["category"])

    if key in seen:
        repeated.append(record)
    else:
        seen.add(key)

# Assessment Data 1: Generated Test Data
print("\n=== ASSESSMENT DATA 1: GENERATED TEST DATA ===")
for record in records:
    print(record)

# Assessment Data 2: Organized Test Data
print("\n=== ASSESSMENT DATA 2: ORGANIZED TEST DATA ===")
for record in organized:
    print(record)

# Assessment Data 3: Repeated/Distinct Data
print("\n=== ASSESSMENT DATA 3: REPEATED/DISTINCT DATA ===")
print("Repeated records:", repeated)
print("Distinct source/category combinations:", len(seen))

# Assessment Data 4: Numerical and Categorical Summaries
print("\n=== ASSESSMENT DATA 4: SUMMARIES ===")

for category in categories:
    values = [
        record["value"]
        for record in records
        if record["category"] == category
    ]

    print(
        category,
        "| Count:", len(values),
        "| Minimum:", min(values),
        "| Maximum:", max(values),
        "| Average:", round(sum(values) / len(values), 2)
    )

print("\nRecords per source:")
for source in sources:
    count = sum(record["source"] == source for record in records)
    print(source, ":", count)

# Assessment Data 5: Ordered Results
print("\n=== ASSESSMENT DATA 5: ORDERED RESULTS ===")
for record in sorted(organized, key=lambda r: (r["category"], r["value"])):
    print(record)

# Assessment Data 6: Final Summary
print("\n=== FINAL OUTPUT: CONSOLIDATED TEST DATA SUMMARY ===")
print("Total records:", len(records))
print("Distinct source/category combinations:", len(seen))
print("Repeated records:", len(repeated))
print("Measurement categories:", len(categories))
print("Test sources:", len(sources))
print("All records have been generated, organized, and summarized.")