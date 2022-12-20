import unittest
from unittest.mock import patch,mock_open

class AdditionTestCase(unittest.TestCase):
    
    @patch('builtins.open',new=mock_open(read_data="2\n2\n5 5\n5 5\n4\n1 3 5 7\n2 4 8 2\n6 3 1 1\n 2 3 5 6"))
    def test_input_main(self):

        result = find_Ten("null")
        assert result == (2, [2, 4], [['5', '5\n'], ['5', '5\n'], ['1', '3', '5', '7\n'], ['2', '4', '8', '2\n'], ['6', '3', '1', '1\n'], ['', '2', '3', '5', '6']])
  
    @patch('builtins.open',new=mock_open(read_data=""))
    def test_input_null(self):

        result = find_Ten("null")

        assert result == (0,[],[])

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
        
    def test_output_mixed_answer_ten_main_1(self):

        result = mixed_answer_ten(1,[2,],[['5','5\n'], ['5','5\n']])

        assert result == [4]

    def test_output_mixed_answer_ten_main_2(self):

        result = mixed_answer_ten(2,[2,4],[['5','5\n'], ['5','5\n'],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])

        assert result == [4,4]

    def test_output_mixed_answer_ten_zero(self):

        result = mixed_answer_ten(0,[],[])

        assert result == []

    def test_output_mixed_answer_ten_error1(self):

        result = mixed_answer_ten(2,[2,4],[['5','5\n'], ['5','5\n'],[1,2,3,4],[1,2,3,4],[1,2,3,4]])

        assert result == "Matrix size and matrix size are not the same."

    def test_output_mixed_answer_ten_error2(self):

        result = mixed_answer_ten(1,[2,4],[['5','5\n'], ['5','5\n'],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])

        assert result == "The number of data sets and the actual number of data do not match."

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

def mixed_answer_ten(total_number,All_size_of_metrix,data_set):
    
    index = 0
    Ans = 0
    All_Ans = []

    if total_number != len(All_size_of_metrix):
        
        return "The number of data sets and the actual number of data do not match."
    
    for section in range(total_number):

        size = All_size_of_metrix[section]
        data = data_set[index:index+size]

        if size != len(data):

            return "Matrix size and matrix size are not the same."

        data_convert_column_to_row = set_up_data_colum(size,data)
        
        for i in range(size):
            
            Ans += check_ten(size,data[i]) + check_ten(size,data_convert_column_to_row[i])
            
        index += size
        All_Ans.append(Ans)
        Ans = 0
        
    return All_Ans

def find_Ten(filename):
    
    All_size_of_metrix,data_set = [],[]
    stack,total_number = 0,0
    
    file = open(str(filename))
    
    try :
        
        for line in file:

            if str(line) != '\n' :

                if total_number == 0 :

                        total_number = int(line)

                else :

                    target = line.split(' ')

                    if stack == 0 :

                        All_size_of_metrix.append(int(target[0]))
                        stack = int(target[0])

                    else :

                        stack -= 1
                        data_set.append(target)
        file.close()

    except :
                    
        return "Invalid input"

    return total_number,All_size_of_metrix,data_set

if __name__ == '__main__':
    unittest.main()