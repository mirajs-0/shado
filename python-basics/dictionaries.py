# LESSON 3 - Dictionaries

# Behavioral profile of the phone owner

user_profile = {
    "name": "Miraj",
    "most_used_app": "WhatsApp",
    "avg_daily_unlocks": 47,
    "typical_first_unlock": "07:30",
    "nigh_usage": False
}

# Accessing values by key
print(user_profile["name"])
print(user_profile["avg_daily_unlocks"])
print(user_profile["typical_first_unlock"])

# ADDING AND UPDATING
user_profile["device"] = "Android"
print(user_profile)

# Updating
user_profile["avg_daily_unlocks"] = 52
print(f"Updated unlocks: {user_profile['avg_daily_unlocks']}")

user_profile["most_used_app"] = "Wolt"
print(f"New Most Used App: {user_profile['most_used_app']}")

# CHECKING IF KEY EXISTS
if "name" in user_profile:
    print(f"Profile Owner: {user_profile['name']}")

if "location" not in user_profile:
    print(f"Location data not collected.")

# LOOPING THROUGH A DICTIONARY
print("\nFull Behavioral Profile:")
for key, value in user_profile.items():
    print(f"{key}: {value}")

# NESTED DICTIONARY

shado_data = {
    "authorized_user": {
        "name": "Miraj",
        "avg_daily_unlocks": 47,
        "top_apps": ["WhatsApp", "Chrome", "Instagram", "Maps"]
    },
    "current_session": {
        "unlocks": 12,
        "apps_opened": ["Chrome", "Maps", "Settings"]
    }
}

# Accessing nested data
print(shado_data["authorized_user"]["name"])
print(shado_data["current_session"]["apps_opened"])

# Comparing Two Profiles
authorized_apps = shado_data["authorized_user"]["top_apps"]
current_apps = shado_data["current_session"]["apps_opened"]

matches = 0
for application in current_apps:
    if application in authorized_apps:
        matches +=1
print(f"\n App Matches: {matches} out of {len(current_apps)}")

if matches == 0:
    print ("Warning: Behavior does not match owner profile")
else:
    print("Behavior partially matches owner profile")