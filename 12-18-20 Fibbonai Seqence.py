# Jeremiah Allu
# 12-18-20
# Pd.5
# Fibonacci Sequence

# Funtion 1 just printed a description. No Data was passed back and forth!
def fibbonaciDescription():
    print('This will show the number of Fibbonaci numbers you requested!')
    print('First you will be asked how many numbers you want to see!')
    print('Then the list will print vertically!')
    print()


# Function 2 -- This will send back the number of Fibbonaci term I want to print
def getData():
    print()
    print('How many numbers of the Fibbonaci Sequence do you wish to see? \n')
    num=int(input())
    print()
    return(num)

# Function 3 -- This is the heart and soul of the program. It will generate the sequence!
def fibbonaci(sequence):
    if sequence>2:
        print("*******************")
        a=1
        b=1
        print(a)
        print(b)
        for x in range(sequence-2):
            c=a+b
            a=b
            b=c
            print(c)
        print("*******************")
    else:
        print('The first two numbers of the Fibonnaci Sequence are 1,1')
        print("However, you must ask to see at least 3 terms for this program")
        print("to give you more of the sequence")
        print()

# Function 4 -- will return whether the user wants to do the program again or not
def goAgain():
    print()
    print('Would you like to generate a new list?')
    again=str(input("Enter yes to see a new list or no to quit! "))
    print()
    return(again)

    

# Main Processing Module
again='yes'
while again.lower()=='yes' or again.lower()=='y':
    fibbonaciDescription()
    numSequence=getData()
    fibbonaci(numSequence)
    again=goAgain()

print()
print("Thanks for using this program!")
print()
