print("how is it going?\n")

mood = input()

if mood.lower() == 'good':
    x = input("I'm so glad to hear that, would you like me to read you a happy poem?")
    if x.lower() == 'yes':
        print("Roses are red, violets are blue, you make life easy, I like you")
    else:
        print("Okay, have a great day!\n")
elif mood.lower() == 'bad':
    x = input("I'm so sorru, I can try to cheer you up with a powerful quote if you want?\n")
    if x.lower() == 'yes':
        print("Here is a quote that you should alwasy remember; 'You're never too old to enjoy a sunset.' - Sassy the Sasquatch")
    else:
        print("I'm sorru, hope you feel better soon!")
