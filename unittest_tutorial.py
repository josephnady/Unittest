'''
this is a tutorial demo from Python Simplified in youtube 
https://www.youtube.com/watch?v=ibVSPVz2LAA

TDD -> Test Driven Development 
using unittest package

The Three laws of TDD
1) Write a failing test first
2) Make sure the test fails
3) Then write just enough code to
fail test -> fix code -> pass test -> fail new test -> ....
'''
'''testing'''
import unittest
import string

def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypt_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char)+1) else abc[0] for idx, char in enumerate(message)])
    # print(encrypt_message)
    return encrypt_message

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "I am Batman!!! 888"
    # test go here
    # the first part of func name must be test_
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    def test_funcReturnSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))
    
    def test_lenIO(self):
        self.assertEqual(len(self.my_message),len(encrypt(self.my_message)))
    
    def test_differentIO(self):
        self.assertNotIn(self.my_message,encrypt(self.my_message))

    def test_outputExists(self):
        self.assertIsInstance(encrypt(self.my_message),str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypt_message = "".join([abc[abc.find(char) + 1]  if len(abc) > (abc.find(char)+1) else abc[0]  for idx, char in enumerate(self.my_message)])
        print(encrypt_message)
        self.assertEqual(encrypt_message,encrypt(self.my_message))

if __name__ == "__main__":
    unittest.main()
