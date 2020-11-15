import os
from unittest import TestCase

from decrypt import Decrypt
from encrypt import Encrypt


class Encryption(TestCase):

    def test_encryption_create_file(self):
        msg = b'hello there are some bytes over here'
        key = 'This is sample key'
        filename = 'test_create_file.txt'
        file = open(filename, 'wb')
        file.write(msg)
        e = Encrypt(filename, key)
        encrypt_filename = e.generate_encrypted_file()
        os.remove(filename)
        os.remove(encrypt_filename)
        self.assertTrue(1)


class Decryption(TestCase):
    def test_decryption(self):
        msg = b'This is a text'
        filename = 'test_decryption.txt'
        key = 'ThisIsMyKey'
        file = open(filename, 'wb')
        file.write(msg)
        file.close()
        e = Encrypt(filename, key)
        encrypted_filename = e.generate_encrypted_file()
        d = Decrypt(encrypted_filename, key)
        decrypted_filename = d.generate_decrypted_file()
        file = open(decrypted_filename, 'rb')
        decrypted_content = file.read()
        self.assertEqual(msg, decrypted_content)
