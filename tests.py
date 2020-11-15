from unittest import TestCase
from encrypt import Encrypt

class Encryption(TestCase):

    def test_encryption_len(self):
        msg = b'hello there are some bytes over here'
        key = 'This is sample key'
        msg_lenght = len(msg)
        filename = 'test_len.txt'
        file = open(filename, 'wb')
        file.write(msg)
        e = Encrypt(filename, key)
        encrypted_file = open(e.generate_encrypted_file(), 'rb')
        encrypted_msg = encrypted_file.read()
        encrypted_msg_len = len(encrypted_msg)
        self.assertEqual(msg_lenght, encrypted_msg_len)
