colour = input("Enter traffic light colour (red/yellow/green): ")

if colour == "red":
    print("STOP!")
elif colour == "yellow":
    print("Prepare to stop")
elif colour == "green":
    print("You can go")
else:
    print("Wrong input!")