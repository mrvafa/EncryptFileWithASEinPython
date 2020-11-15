#! /usr/bin/python3.6

# Author: MohammadReza Vafazadeh
# Site: mrvafa.ir
# date: 2020-11-15

"""
This is encryption base on AES in Python.
AES algorithms is one of the most secure encryption algorithms.
"""
from Crypto.Cipher import AES
import hashlib
import os


class Encrypt:
    def __init__(self, filename, key):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.mode = AES.MODE_CBC
        self.iv = '''=FC*#4YpLWvtDxLQ'''
        self.filename = filename

    def _get_file_content(self):
        file = open(self.filename, 'rb')
        file_content = file.read()

        while len(file_content) % 16 != 0:
            file_content += b'\0'
        return file_content

    def generate_encrypted_file(self):
        cipher = AES.new(key=self.key, mode=self.mode, IV=self.iv)
        file_content = self._get_file_content()
        encrypt_content = cipher.encrypt(file_content)
        encryption_file_filename = self.filename if '.' in self.filename else self.filename + '.'
        filename_split_with_dot = encryption_file_filename.split('.')
        encryption_file_filename = '.'.join(filename_split_with_dot[:-1]) + '.encrypted'
        filename_counter = 1
        while os.path.isfile(encryption_file_filename):
            encryption_file_filename = '.'.join(filename_split_with_dot[:-1]) + f'_{filename_counter}.encrypted'
            filename_counter += 1
        file = open(encryption_file_filename, 'wb')
        file.write(encrypt_content)
        file.close()
        return encryption_file_filename
