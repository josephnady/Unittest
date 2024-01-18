import unittest

def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list


class TestUniqueFunc(unittest.TestCase):
    input_list = [1,2,3,1,3,4]
    expected = [1,2,3,4]
    @staticmethod
    def uniq_test(list):
        """ Returns unique values of a list """
        u_list = []
        for item in list:
            if item not in u_list:
                u_list.append(item)
        return u_list
    
    def test_input_is_not_none(self):
        self.assertIsNotNone(self.input_list)
    #scenario 1 - one element in the input_list
    def test_input_contain_one_element(self):
         self.assertTrue(len(self.uniq_test(self.input_list))<=len(self.expected))

if __name__=="__main__":
        unittest.main()