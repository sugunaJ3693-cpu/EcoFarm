def get_moisture_limit(crop_type):
    if crop_type.lower() == "rice":
        return 40
    elif crop_type.lower() == "tomato":
        return 35
    elif crop_type.lower() == "cotton":
        return 30
    else:
        return 30


def validate_input(soil_moisture, temperature, last_water):
    if soil_moisture < 0 or soil_moisture > 100:
        return False, "Soil moisture must be between 0% and 100%."

    if temperature < -20 or temperature > 60:
        return False, "Temperature value is outside the supported range."

    if last_water < 0:
        return False, "Water amount cannot be negative."

    return True, ""


def calculate_water(soil_moisture, moisture_limit, temperature):
    moisture_gap = moisture_limit - soil_moisture
    water_amount = moisture_gap * 10

    if temperature >= 35:
        water_amount = water_amount * 1.2

    return water_amount


def make_decision(crop_type, soil_moisture, rain_expected,
                  temperature, last_water):

    moisture_limit = get_moisture_limit(crop_type)

    if soil_moisture < moisture_limit and rain_expected:
        return "IRRIGATION POSTPONED", \
               "Soil moisture is low, but rain is expected.", 0

    if soil_moisture < moisture_limit and last_water >= 100:
        return "IRRIGATION DELAYED", \
               "Significant water was applied recently.", 0

    if soil_moisture < moisture_limit:
        water_amount = calculate_water(
            soil_moisture,
            moisture_limit,
            temperature
        )

        return "IRRIGATION RECOMMENDED", \
               "Soil moisture is below the required level.", water_amount

    return "IRRIGATION NOT REQUIRED", \
           "Soil moisture is sufficient.", 0


# ---------------- MAIN PROGRAM ----------------

crop_type = input("Enter crop type (rice/tomato/cotton): ")
soil_moisture = float(input("Enter soil moisture (%): "))
rain_input = input("Is rain expected? (yes/no): ")
temperature = float(input("Enter temperature (°C): "))
last_water = float(input("Water applied recently (liters): "))

rain_expected = rain_input.lower() == "yes"

valid, error_message = validate_input(
    soil_moisture,
    temperature,
    last_water
)

if not valid:

    print("\n⚠️ INVALID INPUT")
    print(error_message)

else:

    decision, reason, water_amount = make_decision(
        crop_type,
        soil_moisture,
        rain_expected,
        temperature,
        last_water
    )

    print(f"\n🌱 {decision}")
    print(f"Reason: {reason}")

    if water_amount > 0:
        print(f"Estimated water required: {water_amount:.1f} liters")
