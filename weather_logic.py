def weather_decision(rain_probability, temperature):

    if rain_probability >= 70:
        return True, "High probability of rainfall."

    elif rain_probability >= 40:
        return True, "Moderate probability of rainfall."

    else:
        return False, "Low probability of rainfall."


# ---------------- TEST PROGRAM ----------------

if __name__ == "__main__":

    rain_probability = float(
        input("Enter rain probability (%): ")
    )

    temperature = float(
        input("Enter temperature (°C): ")
    )

    if rain_probability < 0 or rain_probability > 100:
        print("\n⚠️ INVALID INPUT")
        print("Rain probability must be between 0% and 100%.")

    else:
        rain_expected, reason = weather_decision(
            rain_probability,
            temperature
        )

        print("\n🌦️ WEATHER ANALYSIS")

        if rain_expected:
            print("Rain expected: YES")
        else:
            print("Rain expected: NO")

        print(f"Reason: {reason}")
        print(f"Temperature: {temperature:.1f}°C")
