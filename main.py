#! /usr/bin/python3.6
import argparse
from getpass import getpass

from decrypt import Decrypt
from encrypt import Encrypt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', help='Enter D for decryption and E for Encryption.', required=True)
    parser.add_argument('-p', '--path', help='Path to file you want to decrypt/encrypt.', required=True)
    args = parser.parse_args()

    path = args.path
    function = args.function.lower()

    if function not in ('e', 'd'):
        raise TypeError('No function found! (You should use either D or E.)')

    key = getpass('Please Enter your Key: ')

    if function == 'e':
        e = Encrypt(filename=path, key=key)
        encrypted_file_path = e.generate_encrypted_file()
        print(f'Encryption was successfully finished. encrypted file path is {encrypted_file_path}.')
    else:
        e = Decrypt(filename=path, key=key)
        decrypted_file_path = e.generate_decrypted_file()
        print(f'Decryption was successfully finished. decrypted file path is {decrypted_file_path}.')
