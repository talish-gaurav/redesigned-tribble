
yn = input('''Tell us if you have been absent due to medical conditions, only use capital letters Y(for yes) and N(for no)''')

if yn == "Y":

    print("You can take the exam")

elif yn == "N":

    att = input("Has your attendance been over 75% ? Again type capital Y(for yes) and N(for no)")
    
    if att =="Y":

        print("You can take the test. ")

    elif att =="N":

        print("You can not take the test")  

    else:

        print("Invalid input! Try again with a capital Y(for yes) and N(for no)")

else:

    print("Invalid input! Try again with a capital Y(for yes) and N(for no)")  
    