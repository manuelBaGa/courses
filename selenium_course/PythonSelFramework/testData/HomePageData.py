import csv


class HomePageData:

    test_HomePage_data = [{"name":"Rahul",
                             "email":"hello@gmail.com",
                             "gender":"Male"},
                            {"name": "Anshika",
                             "email": "hello@gmail.com",
                             "gender": "Female"}]

    @staticmethod
    def getTestData(test_case_name):
        rows = {}

        # reading csv file
        with open("..\\testData\\exceldemo_data.csv",
                  'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            next(csvreader)
            # extracting each data row one by one
            for row in csvreader:
                rows[row[0]]={"name":row[1],
                             "email":row[2],
                             "gender":row[3]}

        return [rows[test_case_name]]