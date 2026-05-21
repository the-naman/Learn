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

id = 0
choice = int(input("""1. Album\n2. Artist\n3. Year\n4. Songs\n5. All in one\n0. Exit\nEnter your choice: """))
if choice > 0:
        if choice <= 5:
            for album, artist, year, songs in albums:
                id += 1
                if choice == 1:
                    print("{}. {}".format(id, album))
                    
                elif choice == 2:
                    print("{}. {}".format(id, artist))
                    
                elif choice == 3:
                    print("{}. {}".format(id, year))
                    
                elif choice == 4:
                    print("{}. {}\n".format(id, songs))
                    
                elif choice == 5:
                     print("Album: {}\nArtist: {}\nYear: {}\nSongs: {}\n"
                           .format(album, artist, year, songs))
              
                     
        else:
             print("Invalid Choice")
else:
    print("Exit")
