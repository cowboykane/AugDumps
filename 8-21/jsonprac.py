import os, json

albums = {
    "Elliott Smith": "Figure 8",
    "Failure": "Fantastic Planet",
    "Massive Attack": "Mezzanine"
}

with open("8-21/albums.json", "w") as f:
    json.dump(albums, f, indent=4)

with open("8-21/albums.json", "r") as f:
    print_file = json.load(f)

print(print_file)