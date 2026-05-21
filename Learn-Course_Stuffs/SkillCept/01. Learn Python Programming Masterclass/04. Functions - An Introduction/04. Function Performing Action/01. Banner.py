def banner(text):
    screen_width = 80

    if len(text) > screen_width - 4:
        txt = "The TEXT is too long to fit in the specified width."
        print("**{}**".format(txt.center(screen_width-4)))

    if text == "*":
        print("*" * screen_width)

    if len(text) < screen_width-4 and text != "*":
        centered_text = text.center(screen_width-4)
        print("**{}**".format(centered_text))



banner("*")
banner("Kumar Naman")
banner("Python 3")
banner("God is great")
banner("Data is the new fuel")
banner(" ")
banner("AI is new work resource")
banner("Robotics are new labours")
banner("Laptop is very good")
banner("asdfghjklqwertyuiopzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmpasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm")
banner("*")