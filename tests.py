import os
from unittest import TestCase

from encrypt import Encrypt


class Encryption(TestCase):

    def test_encryption_len(self):
        msg = b'hello there are some bytes over here'
        key = 'This is sample key'
        filename = 'test_len.txt'
        file = open(filename, 'wb')
        file.write(msg)
        e = Encrypt(filename, key)
        encrypt_filename = e.generate_encrypted_file()
        os.remove(filename)
        os.remove(encrypt_filename)
        self.assertTrue(1)
