# EXERCISE 3: TRANSACTION HISTORY ANALYZER

LAST_NAME = "TABARDILLA"
SEED_NUM = 8
FAVORITE_ARTIST = "NEW JEANS"

# 1. Generate five customers and five products.
customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

products = [
    "NOTEBOOK",
    "PEN",
    "USB",
    "HEADPHONES",
    "CALCULATOR"
]

# Assign fixed prices (in pesos).
prices = {
    "NOTEBOOK": 35.00,
    "PEN": 15.00,
    "USB": 250.00,
    "HEADPHONES": 450.00,
    "CALCULATOR": 300.00
}

# Get character positions from the favorite artist.
artist_letters = [
    ord(char) for char in FAVORITE_ARTIST if char.isalpha()
]

transactions = []

# Generate three transactions for each customer.
for customer_index, customer in enumerate(customers):

    for purchase_index in range(3):

        # Select a product using customer and purchase positions.
        product_index = (
            customer_index + purchase_index
        ) % len(products)

        product = products[product_index]

        # Generate quantity using SEED_NUM and artist characters.
        artist_value = artist_letters[
            (customer_index + purchase_index) % len(artist_letters)
        ]

        quantity = 1 + (
            SEED_NUM + artist_value + customer_index + purchase_index
        ) % 5

        transaction_value = quantity * prices[product]

        transactions.append({
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "price": prices[product],
            "total": transaction_value
        })

# Add one repeated customer-product purchase.
transactions.append(transactions[0].copy())


# 2. Organize transactions by customer and product.
organized = sorted(
    transactions,
    key=lambda record: (record["customer"], record["product"])
)


# 3. Identify repeated customer-product purchases.
seen = set()
repeated = []

for record in organized:
    key = (record["customer"], record["product"])

    if key in seen:
        repeated.append(record)
    else:
        seen.add(key)

distinct_products = set(record["product"] for record in transactions)
distinct_customers = set(record["customer"] for record in transactions)


# 4. Display Assessment Data 1: Generated Transaction Records.
print("\n=== ASSESSMENT DATA 1: GENERATED TRANSACTION RECORDS ===")

for record in transactions:
    print(record)


# 5. Display Assessment Data 2: Organized Transaction Data.
print("\n=== ASSESSMENT DATA 2: ORGANIZED TRANSACTION DATA ===")

for record in organized:
    print(record)


# 6. Display Assessment Data 3: Repeated/Distinct Transactions.
print("\n=== ASSESSMENT DATA 3: REPEATED/DISTINCT TRANSACTIONS ===")

print("Repeated customer-product purchases:")

for record in repeated:
    print(record)

print("Distinct customer-product combinations:", len(seen))
print("Distinct customers:", len(distinct_customers))
print("Distinct products:", len(distinct_products))


# 7. Display Assessment Data 4: Transaction Values.
print("\n=== ASSESSMENT DATA 4: TRANSACTION VALUES ===")

for record in transactions:
    print(
        record["customer"],
        "|", record["product"],
        "| Quantity:", record["quantity"],
        "| Price:", record["price"],
        "| Total:", record["total"]
    )

overall_total = sum(record["total"] for record in transactions)

print("Overall transaction value: PHP", round(overall_total, 2))


# 8. Display Assessment Data 5: Customer Summaries.
print("\n=== ASSESSMENT DATA 5: CUSTOMER SUMMARIES ===")

for customer in customers:

    customer_records = [
        record for record in transactions
        if record["customer"] == customer
    ]

    customer_total = sum(
        record["total"] for record in customer_records
    )

    total_items = sum(
        record["quantity"] for record in customer_records
    )

    print(
        customer,
        "| Transactions:", len(customer_records),
        "| Items purchased:", total_items,
        "| Total spending: PHP", round(customer_total, 2)
    )


# 9. Display Assessment Data 6: Product Summaries.
print("\n=== ASSESSMENT DATA 6: PRODUCT SUMMARIES ===")

for product in products:

    product_records = [
        record for record in transactions
        if record["product"] == product
    ]

    total_quantity = sum(
        record["quantity"] for record in product_records
    )

    product_total = sum(
        record["total"] for record in product_records
    )

    print(
        product,
        "| Transactions:", len(product_records),
        "| Quantity sold:", total_quantity,
        "| Sales: PHP", round(product_total, 2)
    )


# 10. Display Assessment Data 7: Ordered Results.
print("\n=== ASSESSMENT DATA 7: ORDERED RESULTS ===")

# Sort transactions by total value, highest first.
ordered_results = sorted(
    transactions,
    key=lambda record: record["total"],
    reverse=True
)

for record in ordered_results:
    print(record)


# 11. Display Assessment Data 8: Overall Transaction Summary.
print("\n=== ASSESSMENT DATA 8: OVERALL TRANSACTION SUMMARY ===")

print("Total transaction records:", len(transactions))
print("Distinct customer-product combinations:", len(seen))
print("Repeated purchases:", len(repeated))
print("Number of customers:", len(customers))
print("Number of products:", len(products))
print("Overall transaction value: PHP", round(overall_total, 2))


# 12. Final Output.
print("\n=== FINAL OUTPUT: CONSOLIDATED TRANSACTION REPORT ===")

print("Customer names:", customers)
print("Products:", products)
print("Total records:", len(transactions))
print("Total sales: PHP", round(overall_total, 2))
print("Repeated customer-product purchases:", len(repeated))

print("\nTransaction report completed.")