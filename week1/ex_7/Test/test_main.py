import unittest
from unittest.mock import patch,mock_open

class AdditionTestCase(unittest.TestCase):

    #Input    
    @patch('builtins.open',new=mock_open(read_data="16 200 -10\n12\n70\n1\n999\n50\n20\n1000\n150\n300\n200\n90\n900\n40\n140\n130\n30"))
    def test_input_main(self):

        result = read_file("null")
        assert result == (['16', '200', '-10\n'],[1, 12, 20, 30, 40, 50, 70, 90, 130, 140, 150, 200, 300, 900, 999, 1000])
  
    @patch('builtins.open',new=mock_open(read_data=""))
    def test_input_null(self):

        result = read_file("null")

        assert result == ("Please fill in this format. Number of members in the set c1 c2 ex 16 200 -10",[])

    @patch('builtins.open',new=mock_open(read_data="16 200 -10\n12\n70\n1\n999\n50\n20\n1000\n150"))
    def test_input_zero1(self):

        result = read_file("null")

        assert result == ("The specified number of answer sets does not match the actual number of data. :16 But get 8",[])

    @patch('builtins.open',new=mock_open(read_data="16 200 -10\n12\n70\n1\n999\n50\n20\n"))
    def test_input_zero2(self):

        result = read_file("null")

        assert result == ("The number of answers in the set must be more than 8 characters",[])
    
    @patch('builtins.open',new=mock_open(read_data="16 200 -10\n12\nฟ\n1\n999\n50\n20\n1000\n150"))
    def test_input_zero3(self):

        result = read_file("null")

        assert result == ("Set members must be numbers.",[])

    # Solution 

    def test_find_x_1_2_main(self):

        result = find_x_1_2([1, 12, 20, 30, 40, 50, 70, 90, 130, 140, 150, 200, 300, 900, 999, 1000],200)
 
        assert result == [[5, 10], [6, 8], [8, 6], [10, 5]]

    def test_find_x_1_2_main2(self):

        result = find_x_1_2([1, 2, 3, 4, 5, 6, 7, 8, 9],200)
 
        assert result == []

    def test_find_x_1_2_zero(self):

        result = find_x_1_2([],0)
 
        assert result == []

    #-------------------------------
    def test_find_x1_to_4_main(self):

        result = find_x1_to_4([[5, 10], [6, 8], [8, 6], [10, 5]],[1, 12, 20, 30, 40, 50, 70, 90, 130, 140, 150, 200, 300, 900, 999, 1000])

        assert result == [[5, 10, 2, 6], [5, 10, 4, 7], [5, 10, 7, 9], [6, 8, 2, 7], [8, 6, 2, 10]]

    def test_find_x1_to_4_main2(self):

        result = find_x1_to_4([],[1, 12, 20, 30, 40, 50, 70, 90, 130])

        assert result == []

    def test_find_x1_to_4_zero(self):

        result = find_x1_to_4([],[])

        assert result == []
    #-------------------------------

    def test_find_x_6_8_main(self):

        result = find_x_6_8([1, 12, 20, 30, 40, 50, 70, 90, 130, 140, 150, 200, 300, 900, 999, 1000],-10)
    
        assert result == [[3, 2], [4, 3], [5, 4], [9, 8], [10, 9]]

    def test_find_x_6_8_main2(self):

        result = find_x_6_8([1, 2, 3, 4, 5, 6, 7, 8, 9],200)
 
        assert result == []

    def test_find_x_6_8_zero(self):

        result = find_x_6_8([],0)
 
        assert result == []

    #-------------------------------

    def test_find_x5_to_8_main(self):

        result = find_x5_to_8([[3, 2], [4, 3], [5, 4], [9, 8], [10, 9]],[1, 12, 20, 30, 40, 50, 70, 90, 130, 140, 150, 200, 300, 900, 999, 1000])

        assert result == [[4, 3, 6, 2], [5, 4, 7, 3], [7, 4, 8, 3], [2, 5, 6, 4], [7, 5, 9, 4], [10, 5, 11, 4], [5, 10, 11, 9]]

    def test_find_x5_to_8_main2(self):

        result = find_x5_to_8([],[1, 12, 20, 30, 40, 50, 70, 90, 130])

        assert result == []

    def test_find_x5_to_8_zero(self):

        result = find_x5_to_8([],[])

        assert result == []

    #-------------------------------

    def test_combine_setA_setB_main(self):

        result = combine_setA_setB([[5, 10, 2, 6], [5, 10, 4, 7], [5, 10, 7, 9], [6, 8, 2, 7], [8, 6, 2, 10]],[[4, 3, 6, 2], [5, 4, 7, 3], [7, 4, 8, 3], [2, 5, 6, 4], [7, 5, 9, 4], [10, 5, 11, 4], [5, 10, 11, 9]])

        assert result == [5, 10, 2, 6, 7, 4, 8, 3]

    def test_combine_setA_setB_main2(self):

        result = combine_setA_setB([[6, 8, 2, 7], [8, 6, 2, 10]],[[5, 10, 2, 6], [5, 10, 4, 7],])

        assert result == []

    def test_combine_setA_setB_zero(self):

        result = combine_setA_setB([],[])

        assert result == []

    #-------------------------------

    def test_display_Ans_main(self):

        result = display_Ans([5, 10, 2, 6, 7, 4, 8, 3],[1, 12, 20, 30, 40, 50, 70, 90, 130, 140, 150, 200, 300, 900, 999, 1000])

        assert result == "50\n150\n20\n70\n90\n40\n130\n30\n"

    def test_display_Ans_main2(self):

        result = display_Ans([],[1, 12, 20, 30, 40, 50, 70, 90, 130])

        assert result == "There is no answer that satisfies the equation."

    def test_display_Ans_zero(self):

        result = display_Ans([],[])

        assert result == "There is no answer that satisfies the equation."

def read_file(name) :
    
    data_A,c = [],[]
    
    file = open(name)

    for line in file:

        if str(line) != '\n' :

            if len(c) == 0 :

                c = line.split(' ')
                
            else :
                
                try :
                    
                    data_A.append(int(line))
                    
                except :
                    
                    return "Set members must be numbers.",[]

    file.close()

    if len(c) != 3 :
                    
        return "Please fill in this format. Number of members in the set c1 c2 ex 16 200 -10",[]

    if len(data_A) < 8 :
        
        return "The number of answers in the set must be more than 8 characters",[]

    if int(c[0]) != len(data_A):
        
        return "The specified number of answer sets does not match the actual number of data. :"+str(c[0])+" But get "+str(len(data_A)),[]
    
    data_A.sort()
    return c,data_A

def find_x_1_2(data,conditions):
    
    x_1_2_find_index = []

    for start in range(len(data)):

        for target in range(len(data)):

            if target == start :

                continue

            if conditions == data[start] + data[target]:

                x_1_2_find_index.append([start,target])

    return x_1_2_find_index

def find_x1_to_4(conditions,data_A):
    
    Ans_1 = []

    for condition in conditions :

        for start in range(len(data_A)):

            if start == condition[0] or  start == condition[1]:

                continue        

            for target in range(len(data_A)):

                if target == start or target == condition[0] or  target == condition[1] :

                    continue

                if data_A[target] == data_A[start] + data_A[condition[0]] :
                    
                    Ans_1.append([condition[0],condition[1],start,target])

    return Ans_1

def find_x_6_8(data,conditions):
    
    x_6_8_find_index = []
    
    for start in range(len(data)):

        for target in range(len(data)):

            if target == start :

                continue

            if data[target] == data[start] + conditions :

                x_6_8_find_index.append([start,target])

    return x_6_8_find_index

def find_x5_to_8(conditions,data_A):
    
    Ans_1 = []

    for condition in conditions :

        for start in range(len(data_A)):

            if start == condition[0] or  start == condition[1]:

                continue        

            for target in range(start+1,len(data_A)):

                if target == start or target == condition[0] or  target == condition[1] :

                    continue

                if data_A[target] == data_A[start] + data_A[condition[0]] :
                    
                    Ans_1.append([start,condition[0],target,condition[1]])

    return Ans_1

def combine_setA_setB(set_A,set_B):

    Ans = []
    for A_1 in set_A :

        for A_2 in set_B:

            A = 4

            for member_2 in A_2 :
        
                if member_2 in A_1 :

                    A-=1
                
            if A == 4 :
                
                return A_1+A_2

    return []    

def display_Ans(Ans,data_A):
    
    A = ''
    if Ans != [] :
        for i in range(len(Ans)) :
            A += str(data_A[Ans[i]])  +"\n"
        
        return A
    else : 
        return"There is no answer that satisfies the equation."

if __name__ == '__main__':
    unittest.main()