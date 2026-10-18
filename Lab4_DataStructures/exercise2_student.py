# EXERCISE 2: STUDENT PERFORMANCE DATA ANALYZER

LAST_NAME = "TABARDILLA"
SEED_NUM = 8
FAVORITE_ARTIST = "ARTHUR NERY"

students = [f"{LAST_NAME}_S{i}" for i in range(1, 6)]

subjects = [
    "PROGRAMMING",
    "MATHEMATICS",
    "ELECTRONICS",
    "PHYSICS",
    "ENGLISH"
]

artist_letters = [ord(ch) for ch in FAVORITE_ARTIST if ch.isalpha()]

def performance_category(score):
    if score is None:
        return "MISSING"
    elif score >= 90:
        return "Excellent"
    elif score >= 85:
        return "Very Good"
    elif score >= 80:
        return "Good"
    elif score >= 75:
        return "Fair"
    else:
        return "Needs Improvement"

records = []

# Generate a score for each student and subject.
for student_index, student in enumerate(students):
    for subject_index, subject in enumerate(subjects):
        artist_value = artist_letters[
            (student_index + subject_index) % len(artist_letters)
        ]

        score = 50 + (
            SEED_NUM
            + artist_value
            + student_index * 13
            + subject_index * 17
        ) % 51

        records.append({
            "student": student,
            "subject": subject,
            "score": score,
            "category": performance_category(score)
        })

# Add a repeated student/subject record.
records.append(records[0].copy())

# Add one incomplete record with a missing score.
records.append({
    "student": students[4],
    "subject": subjects[4],
    "score": None,
    "category": "MISSING"
})

# Organize records by student and subject.
organized = sorted(
    records,
    key=lambda record: (record["student"], record["subject"])
)

# Find repeated student/subject records.
seen = set()
repeated = []

for record in organized:
    key = (record["student"], record["subject"])

    if key in seen:
        repeated.append(record)
    else:
        seen.add(key)

print("\n=== REPEATED STUDENT-SUBJECT RECORDS ===")

for record in repeated:
    print(
        record["student"],
        "|",
        record["subject"],
        "| Score:",
        record["score"]
    )

print("Repeated records:", len(repeated))

print("\nDetails of repeated records:")
for record in repeated:
    print(record["student"], record["subject"], record["score"])

incomplete = [
    record for record in records
    if record["score"] is None
]

# Assessment Data 1: Generated Performance Records
print("\n=== ASSESSMENT DATA 1: GENERATED PERFORMANCE RECORDS ===")
for record in records:
    print(record)

# Assessment Data 2: Organized Student/Subject Data
print("\n=== ASSESSMENT DATA 2: ORGANIZED DATA ===")
for record in organized:
    print(record)

# Assessment Data 3: Repeated/Incomplete Records
print("\n=== ASSESSMENT DATA 3: REPEATED/INCOMPLETE ===")
print("Repeated records:", repeated)
print("Incomplete records:", incomplete)

# Assessment Data 4: Performance Categories
print("\n=== ASSESSMENT DATA 4: PERFORMANCE CATEGORIES ===")
for record in records:
    print(
        record["student"],
        "|", record["subject"],
        "| Score:", record["score"],
        "| Category:", record["category"]
    )

# Assessment Data 5: Student and Subject Summaries
print("\n=== ASSESSMENT DATA 5: STUDENT SUMMARIES ===")

for student in students:
    scores = [
        record["score"]
        for record in records
        if record["student"] == student and record["score"] is not None
    ]

    if scores:
        print(
            student,
            "| Valid scores:", len(scores),
            "| Average:", round(sum(scores) / len(scores), 2)
        )
    else:
        print(student, "| No valid scores")

print("\nSubject summaries:")
for subject in subjects:
    scores = [
        record["score"]
        for record in records
        if record["subject"] == subject and record["score"] is not None
    ]

    print(
        subject,
        "| Valid scores:", len(scores),
        "| Average:", round(sum(scores) / len(scores), 2)
    )

# Assessment Data 6: Ordered Results
print("\n=== ASSESSMENT DATA 6: ORDERED RESULTS ===")
valid_records = [
    record for record in records
    if record["score"] is not None
]

for record in sorted(valid_records, key=lambda r: r["score"], reverse=True):
    print(record)

# Final Output
print("\n=== FINAL OUTPUT: STUDENT PERFORMANCE REPORT ===")
print("Total records:", len(records))
print("Valid scores:", len(valid_records))
print("Incomplete records:", len(incomplete))
print("Repeated records:", len(repeated))
print("Students:", len(students))
print("Subjects:", len(subjects))
print("Student and subject summaries completed.")