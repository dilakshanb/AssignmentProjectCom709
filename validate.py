
from tqdm import tqdm



def dateValidate(option,rows):
    date = option.split('-')
    if len(date) == 3:
        if len(date[0]) == 4 and int(date[0]) < 2022:
            if len(date[1]) == 2 and int(date[1]) < 13:
                if len(date[2]) == 2 and int(date[2]) < 32:
                    print("input date is valid.............")

                    dates = []
                    for row in tqdm(rows):
                        if row[0] not in dates:
                            dates.append(row[0])
                    try:
                        if option in dates:
                            print("date found in dataset..........")

                            return True
                        else:
                            print("date not found in dataset")
                            return False
                    except:
                        print("something wrong")
                        return  False

                    return True
                else:
                    print("invalid input.........")
                    return False

            else:
                print("invalid input............")
                return  False

        else:
            print("invalid input...............")
            return False

    else:
        print("please use '-' sign for separate year,month and day")
        return False