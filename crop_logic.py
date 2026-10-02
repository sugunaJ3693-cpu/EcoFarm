def get_crop_info(crop_type):

    crop_type = crop_type.lower()

    if crop_type == "rice":
        return {
            "name": "Rice",
            "moisture_limit": 40,
            "water_need": "High"
        }

    elif crop_type == "tomato":
        return {
            "name": "Tomato",
            "moisture_limit": 35,
            "water_need": "Medium"
        }

    elif crop_type == "cotton":
        return {
            "name": "Cotton",
            "moisture_limit": 30,
            "water_need": "Medium"
        }

    else:
        return None


# ---------------- TEST PROGRAM ----------------

if __name__ == "__main__":

    crop = input("Enter crop type: ")

    crop_info = get_crop_info(crop)

    if crop_info is None:
        print("\n⚠️ UNKNOWN CROP")
        print("Crop is not available in the EcoFarm system.")

    else:
        print("\n🌱 CROP INFORMATION")
        print(f"Crop: {crop_info['name']}")
        print(f"Moisture limit: {crop_info['moisture_limit']}%")
        print(f"Water requirement: {crop_info['water_need']}")
