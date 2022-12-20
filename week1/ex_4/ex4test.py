import unittest

class TestCase(unittest.TestCase):
    def test_1element(self):
        result = checkDuplicate([1], 1)
        assert result == 'This array has no duplicate elements.'

    def test_duplicate(self):
        result = checkDuplicate([1,1], 1)
        assert result == 'This array has duplicate elements.'

    def test_noDuplicate(self):
        result = checkDuplicate([1,2,3], 1)
        assert result == 'This array has no duplicate elements.'

    def test_wrongType(self):
        result = checkDuplicate('a',1)
        assert result == 'The condition is invalid.'
    

def checkDuplicate(alist, counter) :
    if (type(alist) != type([])) or (type(counter) != type(1)) or (counter < 1) or (counter > len(alist)) :
        return 'The condition is invalid.'

    if len(alist) <= 1 :
        return 'This array has no duplicate elements.'

    if counter < len(alist) :
        if alist[0] == alist[counter] :
            return 'This array has duplicate elements.'

        if alist[0] != alist[counter] :
            return checkDuplicate(alist, counter+1)

    return checkDuplicate(alist[1:], 1)


if __name__ == '__main__':
    unittest.main()