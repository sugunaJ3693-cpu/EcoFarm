def calculate_total_water(water_amounts):

    total_water = sum(water_amounts)

    return total_water


# ---------------- TEST PROGRAM ----------------

water_amounts = []

count = int(input("How many irrigation events? "))

for i in range(count):

    water = float(
        input(f"Enter water used for event {i + 1} (liters): ")
    )

    if water < 0:
        print("\n⚠️ INVALID INPUT")
        print("Water usage cannot be negative.")
        exit()

    water_amounts.append(water)


total = calculate_total_water(water_amounts)

print("\n💧 WATER USAGE")
print(f"Total water used: {total:.1f} liters")
