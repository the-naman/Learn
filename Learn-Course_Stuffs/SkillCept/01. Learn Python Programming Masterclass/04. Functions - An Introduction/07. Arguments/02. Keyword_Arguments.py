def banner(text= " ", screen_width = 80):

    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than the screen width = {}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)

    if len(text) < screen_width-4 and text != "*":
        centered_text = text.center(screen_width-4)
        print("**{}**".format(centered_text))



banner("*", 80)
banner("Kumar Naman", 80)
banner("Python 3", 80)
banner("God is great", 80)
banner("Data is the new fuel", 80)
banner(screen_width=151)                        # data is not given but it taken data as default " "
banner("AI is new work resource", 100)
banner("Robotics are new labours", 100)
banner("Laptop is very good", 100)
banner("asdfghjklqwertyuiopzxcvbnmqwerzxtyuiopasdfghjklzxcvbnm", 100)
banner("*", 100)


# Here arguments directed to the keyword parameters
# for more plz check python documentation