from datetime import datetime

iso_stuff = datetime.now().isocalendar()

iso_dict = dict()
iso_dict["year"] = iso_stuff.year
iso_dict["week"] = iso_stuff.week
iso_dict["week_day"] = iso_stuff.weekday

print(f"{iso_dict}")

