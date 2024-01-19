import string


class EncryptUtil:

    def encrypt(self, message):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypt_message: str = "".join(
            [abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in
             enumerate(message)])
        # print(encrypt_message)
        return encrypt_message


if __name__ == '__main__':
    encryptUtil = EncryptUtil()
    encrypt_message_1 = encryptUtil.encrypt("abcdefghijklmnopqrstuvwxyz") # bcdefghijklmnopqrstuvwxyzA
    print('"'+encrypt_message_1+'"')
    encrypt_message_2 = encryptUtil.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # BCDEFGHIJKLMNOPQRSTUVWXYZ!
    print('"'+encrypt_message_2+'"')
