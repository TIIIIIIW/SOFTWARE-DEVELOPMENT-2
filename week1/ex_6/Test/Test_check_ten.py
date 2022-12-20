import unittest
from unittest.mock import patch,mock_open

class AdditionTestCase(unittest.TestCase):

    def test_set_up_data_colum_main(self):

        result = set_up_data_colum(1,[['1']])

        assert result == [[1]]

    def test_set_up_data_colum_main2(self):

        result = set_up_data_colum(4,[['1', '3', '5', '7\n'], ['2', '4', '6', '8\n'], ['2', '2', '2', '2\n'], ['2', '2', '2', '2\n']])

        assert result == [[1, 2, 2, 2], [3, 4, 2, 2], [5, 6, 2, 2], [7, 8, 2, 2]]

    def test_set_up_data_colum_zero(self):

        result = set_up_data_colum(0,[])

        assert result == []

    def test_output_cal_total_main1(self):

        result = check_ten(2,['5','5\n'])

        assert result == 1

    def test_output_cal_total_main2(self):

        result = check_ten(4,['1','2','3','4'])

        assert result == 1

    def test_output_cal_total_main3(self):

        result = check_ten(5,['1','2','8','4','6'])

        assert result == 2
        
    def test_output_cal_total_zero(self):

        result = check_ten(0,[])

        assert result == 0

def cal_total(data):
    
    if len(data) == 1 :
        
        return int(data[0])
    
    return int(data[0]) + cal_total(data[1:])

def check_ten(size,data):
    c = 0
    for start in range(size-1):
        length = start+2
        for l in range(size-start-1) :
            total = cal_total(data[start:length])

            if total >= 10 :
                if total == 10 :
                    c += 1
                break
            length += 1
    return c

def set_up_data_colum(size,data):
    
    new_data = []
    for col in range(size):
        
        new_one = []
        
        for row in range(size):
            new_one.append(int(data[row][col]))
            
        new_data.append(new_one)
            
    return new_data

if __name__ == '__main__':
    unittest.main()