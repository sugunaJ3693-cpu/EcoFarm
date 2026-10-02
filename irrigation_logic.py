from crop_logic import get_crop_info
from weather_logic import weather_decision


def validate_input(soil_moisture, temperature, last_water, rain_probability):
    if soil_moisture < 0 or soil_moisture > 100:
        return False, "Soil moisture must be between 0% and 100%."

    if temperature < -20 or temperature > 60:
        return False, "Temperature value is outside the supported range."

    if last_water < 0:
        return False, "Water amount cannot be negative."

    if rain_probability < 0 or rain_probability > 100:
        return False, "Rain probability must be between 0% and 100%."

    return True, ""


def calculate_water(soil_moisture, moisture_limit, temperature):
    moisture_gap = moisture_limit - soil_moisture
    water_amount = moisture_gap * 10

    if temperature >= 35:
        water_amount = water_amount * 1.2

    return water_amount


def make_decision(
    crop_type,
    soil_moisture,
    rain_expected,
    temperature,
    last_water
):
    crop_info = get_crop_info(crop_type)

    if crop_info is None:
        return (
            "INVALID CROP",
            "Crop is not available in the EcoFarm system.",
            0
        )

    moisture_limit = crop_info["moisture_limit"]

    if soil_moisture < moisture_limit and rain_expected:
        return (
            "IRRIGATION POSTPONED",
            "Soil moisture is low, but rain is expected.",
            0
        )

    if soil_moisture < moisture_limit and last_water >= 100:
        return (
            "IRRIGATION DELAYED",
            "Significant water was applied recently.",
            0
        )

    if soil_moisture < moisture_limit:
        water_amount = calculate_water(
            soil_moisture,
            moisture_limit,
            temperature
        )

        return (
            "IRRIGATION RECOMMENDED",
            "Soil moisture is below the required level.",
            water_amount
        )

    return (
        "IRRIGATION NOT REQUIRED",
        "Soil moisture is sufficient.",
        0
    )


# ---------------- MAIN PROGRAM ----------------

crop_type = input("Enter crop type (rice/tomato/cotton): ")
soil_moisture = float(input("Enter soil moisture (%): "))
rain_probability = float(input("Enter rain probability (%): "))
temperature = float(input("Enter temperature (°C): "))
last_water = float(input("Water applied recently (liters): "))


rain_expected, weather_reason = weather_decision(
    rain_probability,
    temperature
)


valid, error_message = validate_input(
    soil_moisture,
    temperature,
    last_water,
    rain_probability
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

    print("\n🌱 CROP INFORMATION")

    crop_info = get_crop_info(crop_type)

    if crop_info is not None:
        print(f"Crop: {crop_info['name']}")
        print(f"Moisture limit: {crop_info['moisture_limit']}%")
        print(f"Water requirement: {crop_info['water_need']}")

    print("\n🌦️ WEATHER ANALYSIS")
    print(f"Rain probability: {rain_probability:.1f}%")
    print(f"Weather reason: {weather_reason}")

    print(f"\n🌱 {decision}")
    print(f"Reason: {reason}")

    if water_amount > 0:
        print(f"Estimated water required: {water_amount:.1f} liters")
