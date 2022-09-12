
import matplotlib.pyplot as plt


def graphPloting(option,rows):
    songList=[]
    weeklist=[]
    for row in rows:
        if row[0]==option:
            if len(songList)<10:
                if row[2] not in songList:
                    songList.append(row[2])
                    weeklist.append(int(row[6]))
            else:
                break
    try:
        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        songList = [label.replace(' ', '\n') for label in songList]
        plt.bar(songList, weeklist, color='maroon',
                width=0.6)

        plt.xlabel(f"Top 10 Songs in {option}")
        plt.ylabel(f"Number of weeks on board untill {option}")
        plt.title(f"Top 10 Songs vs Number of weeks on the board untill {option}")
        plt.show()
    except:
        print("something weny wrong in graph")