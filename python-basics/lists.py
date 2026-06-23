# LESSON 3 - Lists
# Shado Project

apps_opened =["Instagram", "WhatsApp", "Chrome", "Camera", "WhatsApp"]

# Accessing items by position
print(apps_opened[0]) #first item
print(apps_opened[1])
print(apps_opened[-1]) #last item

# Length of List
print(len(apps_opened))

# Add to end of list
apps_opened.append("Maps")
print(apps_opened)

# Remove specific item
apps_opened.remove("Instagram")
print(apps_opened)

# LOOPING THROUGH A LIST
print("Apps opened this session:")
for app in apps_opened:
    print("-- " + app)

# Checking if Item Exists
if "Whatsapp" in apps_opened:
    print("Whatsapp was opened")

if "Tiktok" not in apps_opened:
    print("Tiktok was never opened")

# SLICING - getting part of a list
# First 3 apps opened
first_three = apps_opened[0:3]
print(f"First three apps: {first_three}")

# Last 2 apps opened
last_two = apps_opened[-2:]
print(f"Last two apps: {last_two}")