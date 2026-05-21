albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984)
]

print("Horizontal View: ")
for album in albums:
    print("Album: {}, Artist: {}, Year: {}\n"
      .format(album[0], album[1], album[2]))
    
print("\n\nVertical View: ")
for album in albums:
    print("Album: {}\nArtist: {}\nYear: {}\n"
      .format(album[0], album[1], album[2]))
    