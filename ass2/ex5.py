import json
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)
new_batter = {"id": "b03", "type": "Tea"}
for donut in ex5:
    if donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append(new_batter)
with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=4)

print("File Updated")
