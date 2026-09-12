""" Must be interactive, either in the command line with print() and input() or with Tkinter
Check guests in and out
Charge guests for their room(s)
Multiple room check in
Multiple Night Check in
Add 1 new feature of your choice
Ex. Upgrade room, room service, spa package, etc. """

roomTypeToRoomNum = {"1": [100,101,102,103,104],
                     "2": [200,201,202,203,204],
                     "3": [300,301,302,303,304],
                     "4": [400,401,402,403,404]
                     }
roomNumtoAvail = {100 : True,
                  101 : True,
                  102 : True,
                  103 : True,
                  104 : True,
                  200 : True,
                  201 : True,
                  202 : True,
                  203 : True,
                  204 : True,
                  300 : True,
                  301 : True,
                  302 : True,
                  303 : True,
                  304 : True,
                  400 : True,
                  401 : True,
                  402 : True,
                  403 : True,
                  404 : True
                  }

roomNumToRes = {}

        
        
        
        
        
def checkIn():
    print("We are so glad you will be staying at L'Hotel de Poosh!")
    name = input("What is your name for this reservation?")
    room = input("Which room would you like?\nPress one for Standard Room.\nPress 2 for Deluxe Room.\nPress 3 for Executive Suite.\nPress 4 for our world class Presidential suite!\nPress 5 if you want to book multiple rooms.")
    nights = int(input("How many nights will you be staying here for?"))
    if(room == "1"):
        print("We are delighted to have you with us! Your Standard Room is all ready for you, featuring a comfortable queen-size bed, a modern private bathroom, and high-speed Wi-Fi to keep you connected.")
        money = 100000*nights
    if(room == "2"):
        print("Welcome to the hotel! We have you all set up in one of our beautiful Deluxe Rooms. You'll love the extra space and the upgraded view. We've also included premium bath amenities and a fully stocked Nespresso machine for your stay.")
        money = 1000000*nights
    if(room == "3"):
        print("Welcome! It is an absolute pleasure to have you with us. We have you checked into one of our Executive Suites, which features your separate living area and a dedicated workspace. Your stay also includes complimentary access to our Executive Lounge for breakfast and evening cocktails.")
        money = 10000000*nights
    if(room == "4"):
        print("Welcome to the hotel, Mr./Ms. " + name + ". It is an absolute honor to have you with us. We have your Presidential Suite completely prepared. As our premier guest, your private butler is available 24/7 to handle everything from unpacking to securing exclusive dining reservations.")
        money = 100000000*nights
    roomNumToRes.put()

def getAvailRoomNumandSetUnavail(roomType):
    nums = roomTypeToRoomNum.get(roomType)
    for num in nums:
        isAvail = roomNumtoAvail.get(num)
        if(isAvail == True):

            roomNumtoAvail.put(num,False)
            return num
        


while(True):
    print("Welcome to L'Hotel de Poosh a resort where everything is overpriced, but all the money goes to a good cause: CoCO!")
    choice = input("What would you like to do today?\nPress 1 for checking in.\nPress 2 for checking out and payment.\nPress 3 for room service.\nPress 4 for our in-room spa package!\nPress 5 to leave the hotel.")
    if choice == "5":
        break
    elif choice == "1":
        checkIn()
        
        
        
        
        