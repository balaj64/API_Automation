from Data_Driven import Test_Library
import requests

obj = Test_Library.DataFile("C:/Users/HP/PycharmProjects/API_Automation/Data_Driven/studentDetails.xlsx")


def test_add_multiple_student():
    url = "https://thetestingworldapi.com/api/studentsDetails"

    row = obj.fetch_row_count()
    col = obj.fetch_column_count()
    keylist = obj.fetch_keylist()
    print(row)
    print(keylist)

    for i in range(2, row + 1):
        jsondata = obj.update_request_with_data(i, keylist)
        response = requests.post(url, json=jsondata)
        print(response)
