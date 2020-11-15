from unittest import TestCase
from encrypt import Encrypt
import os


class Encryption(TestCase):

    def test_encryption_len(self):
        msg = b'hello there are some bytes over here'
        key = 'This is sample key'
        msg_length = len(msg)
        filename = 'test_len.txt'
        file = open(filename, 'wb')
        file.write(msg)
        e = Encrypt(filename, key)
        encrypted_file = open(e.generate_encrypted_file(), 'rb')
        encrypted_msg = encrypted_file.read()
        encrypted_msg_len = len(encrypted_msg)
        os.remove(filename)
        self.assertEqual(msg_length, encrypted_msg_len)
