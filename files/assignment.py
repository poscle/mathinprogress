gym = [
    [  #first week
        ["8 - Pilates"],
        ["18 - Boxfit"],
        ["13 - Attack"],
        ["9 - Pilates", "19 - Boxfit"],
        ["14 - Attack"],
        ["8 - Pilates"],
        ["8 - Pilates", "10 - Boxfit"]
    ],
    [  #second week
        ["10 - Boxfit"],
        ["9 - Pilates", "17 - Attack"],
        ["19 - Boxfit"],
        ["9 - Pilates"],
        ["9 - Baby Yoga"],
        ["8 - Pilates"],
        ["8 - Pilates"]
    ],
    [  #third week
        ["8 - Pilates"],
        ["11 - Boxfit", "17 - Yoga"],
        ["18 - Pilates"],
        ["12 - Boxfit"],
        ["18 - Pilates", "19 - Attack"],
        ["8 - Pilates", "10 - Boxfit"],
        ["8 - Pilates"]
    ],
    [  #fourth week
        ["18 - Pilates"],
        ["18 - Boxfit"],
        ["19 - Pilates"],
        ["19 - Boxfit"],
        ["19 - Pilates"],
        ["8 - Pilates"],
        ["8 - Pilates"]
    ]
]

count_pilates = 0

for week in gym:
    for day in week:
        for session in day:
            if "Pilates" in session:
                count_pilates += 1

print(count_pilates)

count_classes = 0

for week in gym:
    for day in week:
        for session in day:
            if session.startswith("18") or session.startswith("19"):
                count_classes += 1

print(count_classes)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

boxfit_list = []

for week_index in range(len(gym)):
    for day_index in range(len(gym[week_index])):
        for session in gym[week_index][day_index]:
            if "Boxfit" in session:
                boxfit_list.append(
                    f"Week {week_index + 1}, {days[day_index]}: {session}"
                )

print(boxfit_list)
