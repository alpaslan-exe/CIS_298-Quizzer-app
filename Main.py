import csv

# ===== TEST COUNTRIES FILE =====
print("Testing countries_capitals.csv...\n")

try:
    with open("countries_capitals.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print("Country:", row["country"], "| Capital:", row["capital"])
            break  # only show first row

    print("✅ countries_capitals.csv works!\n")

except Exception as e:
    print("❌ Error with countries file:", e)

# ===== TEST STATES FILE =====
print("Testing state_capitals.csv...\n")

try:
    with open("state_capitals.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print("State:", row["state"], "| Capital:", row["capital"])
            break  # only show first row

    print("✅ state_capitals.csv works!\n")

except Exception as e:
    print("❌ Error with states file:", e)