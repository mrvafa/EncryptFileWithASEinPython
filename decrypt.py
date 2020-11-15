#! /usr/bin/python3.6

# Author: MohammadReza Vafazadeh
# Site: mrvafa.ir
# date: 2020-11-15

"""
This is decryption base on AES in Python.
AES algorithms is one of the most secure encryption algorithms.
"""
import hashlib
import os

from Crypto.Cipher import AES


class Decrypt:

    def __init__(self, filename, key):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.mode = AES.MODE_CBC
        self.iv = '''=FC*#4YpLWvtDxLQ'''
        self.filename = filename

    def generate_decrypted_file(self):
        cipher = AES.new(key=self.key, mode=self.mode, IV=self.iv)
        file = open(self.filename, 'rb')
        encrypt_content = file.read()
        decryption_content = cipher.decrypt(encrypt_content).rstrip(b'0')
        decryption_file_filename = self.filename if '.' in self.filename else self.filename + '.'
        filename_split_with_dot = decryption_file_filename.split('.')
        decryption_file_filename = '.'.join(filename_split_with_dot[:-1]) + '.decrypted'
        filename_counter = 1
        while os.path.isfile(decryption_file_filename):
            decryption_file_filename = '.'.join(filename_split_with_dot[:-1]) + f'_{filename_counter}.encrypted'
            filename_counter += 1
        file = open(decryption_file_filename, 'wb')
        file.write(decryption_content)
        file.close()
        return decryption_file_filename
