def banner(text, screen_width):

    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than the screen width = {}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)

    if len(text) < screen_width-4 and text != "*":
        centered_text = text.center(screen_width-4)
        print("**{}**".format(centered_text))



banner("*", 66)
banner("Kumar Naman", 66)
banner("Python 3", 66)
banner("God is great", 66)
banner("Data is the new fuel", 66)
banner(" ", 66)
banner("AI is new work resource", 66)
banner("Robotics are new labours", 66)
banner("Laptop is very good", 66)
banner("asdfghjklqwertyuiopzxcvbnmqwerzxtyuiopasdfghjklzxcvbnm", 66)
banner("*", 66)