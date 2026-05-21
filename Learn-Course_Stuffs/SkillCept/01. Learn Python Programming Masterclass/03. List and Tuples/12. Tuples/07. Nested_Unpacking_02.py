albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975, 
     [
        ("1." "Welcome to My Nightmare"),
        ("2." "Devil's Food"),
        ("3." "The Black Widow"),
        ("4." "Some Folks"),
        ("5." "Only Women Bleed")
     ]),
    ("Bad Company", "Bad Company", 1974, 
     [
        ("1." "Can't Get Enough"),
        ("2." "Rock Steady"),
        ("3." "Ready for Love"),
        ("4." "Don't Let Me Down")
     ]),
    ("Nightflight", "Budgie", 1981, 
     [
        ("1." "Night Flight"),
        ("2." "Maybe It's Just Love"),
        ("3." "Crazy Lovers"),
        ("4." "Penumbra Moon"),
        ("5." "Nearer to You")
     ]),
    ("More Mayhem", "Emilda May", 2011, 
     [
        ("1." "Pulling The Rug"),
        ("2." "psycho"),
        ("3." "Mayhem"),
        ("4." "Kentish Town Waltz"),
        ("5." "All For You"),
        ("6." "Eternity"),
        ("7." "Inside Out"),
        ("8." "Proud and Humble"),
        ("9." "Sneaky Freak"),
        ("10." "Bury My Troubles"),
        ("11." "Too Sad To Cry")
     ]),
    ("Ride the Lightning", "Metallica", 1984, 
    [
        ("1." "Fight Fire with Fire"),
        ("2." "Ride the Lightning"),
        ("3." "For Whom the Bell Tolls"),
        ("4." "Fade to Black")
    ])
]


# Code for list the songs in each album
# ---------------------------------------------------------

# choice = 1
# while choice > 0:
#     print("""
#     1. Welcome to my Nightmare
#     2. Bad Company
#     3. Nightflight
#     4. More Mayhem
#     5. Ride the Lightning
#     0. Exit""")
#     choice = int(input("Enter your choice: "))
#     while choice > 0:
        
#         for song in albums[choice-1][3]:
#             print(song)
#         break
# else:
#     print("Exit Successfull")






choice = 1
while choice > 0:
    print("""
    1. Welcome to my Nightmare
    2. Bad Company
    3. Nightflight
    4. More Mayhem
    5. Ride the Lightning
    0. Exit""")
    choice = int(input("Enter your choice: "))
    while choice > 0:
        for song in albums[choice-1][3]:
            print(song)
        song_choose= int(input("Choose song to play: "))
        print("{} playing... listen and enjoy...".format(albums[choice-1][3][song_choose-1]))
        break
else:
    print("Exit Successfull")
