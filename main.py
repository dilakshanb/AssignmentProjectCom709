import csv
from tqdm import tqdm
import menu
import validate as val
import visualize as vs
import getsolution as sol


def run():
    #load data and save
    rows = []
    print("Start Data Extracting...............")
    with open('charts.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headings = next(csvreader)
        for row in tqdm(csvreader):
            rows.append(row[:])
    print("completed...............")

    menu.menu()
    option = int(input("Enter Your Option: "))

    #checking user Options
    while option != 5:
        if option == 1:
            option = input("Enter Date(YY-MM-DD): ")

            while not val.dateValidate(option,rows):
                option = input("Enter Date(YY-MM-DD): ")


            top100songs=sol.getTopRankSong(option,rows)
            print()
            print(f"---------top ranked song for a {option}---------")
            print()
            print(f"Date is             : {top100songs[0]}")
            print(f"Rank is             : {top100songs[1]}")
            print(f"Song Name is        : {top100songs[2]}")
            print(f"Artist is           : {top100songs[3]}")
            print(f"Last Week Rank is   : {top100songs[4]}")
            print(f"Weeks on Board      : {top100songs[6]}")
            print()
            exitCode = int(input("Enter 0 to return main menu: "))
            while exitCode != 0:
                print("Invalid Number")
                exitCode = int(input("Enter 0 to return main menu: "))
            print("exit code correct")
            menu.menu()
            option = int(input("Enter Your Option: "))

        elif option == 2:
            combined_list=sol.getTop10SongsInWeeks(rows)

            print("----------Top 10 songs with the longest number of weeks on the board ----------")
            print("______________________________________________________________")
            print()

            print("{0:50} {1:15}".format('Song Name', 'Number of weeks on the board'))

            print()
            for item in combined_list:

                name = item[0]
                qty = item[1]
                print("{0:50} {1:15}".format(name, qty))



            exitCode = int(input("Enter 0 to return main menu: "))
            while exitCode != 0:
                print("Invalid Number")
                exitCode = int(input("Enter 0 to return main menu: "))
            menu.menu()
            option = int(input("Enter Your Option: "))


        elif option == 3:
            option = input("Enter Song Rank: ")
            sortedList=sol.getArtistDetails(option,rows)

            print("----------top 10 details of the artist ,how many weeks on the board in certain rank----------")
            print("______________________________________________________________")
            print()

            print("{0:50} {1:15}".format('Artist Name','Number of weeks on the board'))

            print()
            for item in sortedList:
                name = item[0]
                qty=item[1]
                print("{0:50} {1:15}".format(name, qty))



            print()
            exitCode = int(input("Enter 0 to return main menu: "))
            while exitCode != 0:
                print("Invalid Number")
                exitCode = int(input("Enter 0 to return main menu: "))
            menu.menu()
            option = int(input("Enter Your Option: "))

        elif option == 4:
            option = input("Enter Date for Ploting graph(YY-MM-DD): ")

            while not val.dateValidate(option,rows):
                option = input("Enter Date(YY-MM-DD): ")

            vs.graphPloting(option,rows)
            exitCode = int(input("Enter 0 to return main menu: "))
            while exitCode != 0:
                print("Invalid Number")
                exitCode = int(input("Enter 0 to return main menu: "))
            menu.menu()
            option = int(input("Enter Your Option: "))

        else:
            print("invalid Number")

    print("Thanks for using this programme , GOOD BYE!")

if __name__ == '__main__':
    run()