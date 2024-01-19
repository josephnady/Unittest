import unittest
from unittest import mock
from unittest.mock import Mock

from app.encrypt_util import EncryptUtil
# from mock import patch


# before writing code
# we have to break down all cases that makes unit test passed and fails
# for example
# 1- when input is "ABC" capital letters it should
# 2- ...
# 3- ...
# ...
class EncryptUtilTest(unittest.TestCase):

    # this function is called before each single test case
    def setUp(self):
        # we can use it to create a fresh objects
        # if I use some global variables under the test class
        self.__class_under_test = EncryptUtil()

    # this function is called after each single test case
    def tearDown(self):
        pass

    # success when input length == output length
    def test_encrypt_succeeded_when_inputLength_equals_outputLength(self):
        # inputs
        data: str = "abc"

        # expected result
        expected = len(data)

        # actual result
        encrypt_message: str = self.__class_under_test.encrypt(data)
        actual = len(encrypt_message)

        # assertion
        self.assertEqual(expected, actual, "should be 3")

    # failed when input length != output length
    def test_encrypt_failed_when_inputLength_notEquals_outputLength(self):

        # inputs
        data: str = "abc"

        # expected result
        expected = len(data)

        # actual result
        mocked_encrypt_message: str = f"{data} "
        self.__class_under_test.encrypt = Mock(return_value=mocked_encrypt_message)
        encrypt_message = self.__class_under_test.encrypt(data)
        actual = len(encrypt_message)

        # assertion
        self.assertNotEqual(expected, actual, "should be 3")

    # when input chars contains
    # * the first alphabetical
    # * small letters
    def test_encrypt_succeeded_when_smallLetter_and_firstAlphabeticalChars(self):
        # expected result
        expected: str = "bcd"

        # actual result
        args: str = "abc"  # inputs
        actual: str = self.__class_under_test.encrypt(args)

        # assertion
        self.assertEqual(expected, actual, "should be bcd")

    # when input chars contains
    # * the latest alphabetical
    # * small letters
    def test_encrypt_succeeded_when_smallLetter_and_latestAlphabeticalChars(self):
        # expected result
        expected: str = "yzA"

        # actual result
        args: str = "xyz"  # inputs
        actual: str = self.__class_under_test.encrypt(args)

        # assertion
        self.assertEqual(expected, actual, "should be yzA")

    # when input chars contains
    # * the first alphabetical
    # * capital letters
    def test_encrypt_succeeded_when_capitalLetter_and_firstAlphabeticalChars(self):
        # expected result
        expected: str = "BCD"

        # actual result
        args: str = "ABC"  # inputs
        actual: str = self.__class_under_test.encrypt(args)

        # assertion
        self.assertEqual(expected, actual, "should be BCD")

    # when input chars contains
    # * the latest alphabetical
    # * capital letters
    def test_encrypt_succeeded_when_capitalLetter_and_latestAlphabeticalChars(self):
        # expected result
        expected: str = "YZ!"

        # actual result
        data: str = "XYZ"  # inputs
        result: str = self.__class_under_test.encrypt(data)

        # assertion
        self.assertEqual(expected, result, "should be YZ!")


