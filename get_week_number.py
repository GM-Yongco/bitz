import json
from datetime import datetime


iso_stuff = datetime.now().isocalendar()

iso_dict = dict()
iso_dict["year"] = iso_stuff.year
iso_dict["week"] = iso_stuff.week
iso_dict["week_day"] = iso_stuff.weekday

json_string = json.dumps(iso_dict, indent=4)
print(json_string)

print(f"{iso_stuff}")

