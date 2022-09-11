from tqdm import tqdm

def getTopRankSong(date,rows):
    top100songs=[]
    for row in tqdm(rows):
        if len(top100songs)<10:
            if row[0]==date:
                top100songs.append(row)
        else:
            break
    return  top100songs[0]

def getArtistDetails(option,rows):
    allArtist=[]
    allArtist_with_duplicate=[]
    artist_count=[]

    for row in tqdm(rows):
        if row[1]==option:
            allArtist_with_duplicate.append(row[3])
            if row[3] not in allArtist:
                allArtist.append(row[3])
    for artist in tqdm(allArtist):
        count=allArtist_with_duplicate.count(artist)
        artist_count.append(count)

    arstist_with_count=list(zip(allArtist,artist_count))
    sortedList=sorted(arstist_with_count, key=lambda t: t[1],reverse=True)
    return  sortedList[0:10]

def getTop10SongsInWeeks(rows):
    all_number_of_weeks=[]
    for row in tqdm(rows):
        if row[6] not in all_number_of_weeks:
            all_number_of_weeks.append(row[6])
    all_number_of_weeks=sorted(all_number_of_weeks,key=lambda t: int(t),reverse=True)

    songlist=[]
    weeklist=[]
    for week in tqdm(all_number_of_weeks):
        for row in rows:
            if len(songlist)<10:
                if row[6]==week:
                    if row[2] not in songlist:
                        songlist.append(row[2])
                        weeklist.append(row[6])
            else:
                break
    combined_list=list(zip(songlist,weeklist))
    combined_list = sorted(combined_list, key=lambda t:int(t[1]), reverse=True)

    return combined_list
