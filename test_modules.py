import unittest
import getsolution
import  validate
import csv


class TestSolutions(unittest.TestCase):

    def setUp(self):
        self.rows = []
        with open('charts.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            headings = next(csvreader)
            for row in csvreader:
                self.rows.append(row[:])

    def tearDown(self):
        pass

    def test_getTopRankSong(self):
        answer=['2021-08-21', '1', 'Stay', 'The Kid LAROI & Justin Bieber', '1', '1', '5']

        self.assertEqual(getsolution.getTopRankSong("2021-08-21",self.rows),answer)

    def test_getArtistDetails(self):

        answer2=[('Mariah Carey', 65), ('The Beatles', 54), ('Boyz II Men', 34), ('Madonna', 32), ('Drake', 31), ('Whitney Houston', 31), ('Michael Jackson', 30), ('The Black Eyed Peas', 28), ('Bee Gees', 27), ('Adele', 26)]
        self.assertEqual(getsolution.getArtistDetails("1",self.rows),answer2)

    def test_getTop10SongsInWeeks(self):
        answer3=[('Blinding Lights', '90'), ('Radioactive', '87'), ('Sail', '79'), ("I'm Yours", '76'), ('How Do I Live', '69'), ('Counting Stars', '68'), ('Party Rock Anthem', '68'), ('Rolling In The Deep', '65'), ('Foolish Games/You Were Meant For Me', '65'), ('Before He Cheats', '64')]


        self.assertEqual(getsolution.getTop10SongsInWeeks(self.rows), answer3)

    def test_dateValidate(self):
        self.assertEqual(validate.dateValidate("2021-08-21",self.rows), True)
        self.assertEqual(validate.dateValidate("2021-08-22",self.rows), False)
        self.assertEqual(validate.dateValidate("2021:08:22",self.rows), False)





if __name__ == '__main__':
    unittest.main()