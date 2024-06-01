def city_country(city, country):
    """display a city and it's country"""
    city = city.title() + ", " + country.title()
    return city


city_1 = city_country("lagos", "nigeria")
city_2 = city_country("Toronto", "canada")
city_3 = city_country("new york", "united states of america")
print(city_1)
print(city_2)
print(city_3)


def make_album(name, album, tracks=""):
    """Returns artist name and album as an object."""
    album = {"name": name.title(), "album": album.capitalize()}
    if tracks:
        album["tracks"] = int(tracks)
    return album


album_1 = make_album("kendrick", "how to pimp a butterfly")
album_2 = make_album("j.cole", "kod")
album_3 = make_album("lil wayne", "carter v")
album_4 = make_album("moses bliss", "too faithful")

print(album_1)
print(album_2)
print(album_3)
print(album_4)

while True:
    print("Enter artist name:")
    print("\n(enter 'q' to quit)")

    a_name = input("Artist name: ")
    if a_name == "q":
        break
    album = input("album name: ")
    if album == "q":
        break
    album_tracks = input("Number of tracks: ")
    if album_tracks == "q":
        break
    obj_album = make_album(a_name, album, album_tracks)
    print(obj_album)
