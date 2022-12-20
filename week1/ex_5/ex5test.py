import unittest

class TestCase(unittest.TestCase):
    def test_noElement(self):
        result = findSumZero([])
        assert result == 'Can not find answer'

    def test_notList(self):
        result = findSumZero(1)
        assert result == 'Can not find answer'

    def test_noAnswer(self):
        result = findSumZero([1,1,1])
        assert result == 'No answer'

    def test_problem(self):
        result = findSumZero([0,-1,2,-3,1,-2])
        assert result == [(-3, 1, 2), (-2, 0, 2), (-1, 0, 1)]

def findSumZero(alist) :
    result = []
    if type(alist) != type([]) or len(alist) < 3: return 'Can not find answer'
    alist.sort()
    for index in range(len(alist)):
        left_num = index + 1
        right_num = len(alist) - 1
        req_num = 0 - alist[index]
        last_append = [0]
        if index > 0 and alist[index] == alist[index-1]: break
        else :
            while left_num < right_num :
                sum_num = alist[left_num] + alist[right_num]
                if sum_num == req_num :
                    result_element = tuple((alist[index],alist[left_num],alist[right_num]))
                    if result_element == last_append[0] :
                        left_num += 1
                    else :
                        last_append[0] = result_element
                        result.append(result_element)
                        left_num += 1
                elif sum_num < req_num :
                    left_num += 1
                else :
                    right_num -= 1
    if len(result) == 0 : return 'No answer'
    else: return result

if __name__ == '__main__':
    unittest.main()