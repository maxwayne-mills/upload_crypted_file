#!/usr/bin/env python3

import sys
import pyAesCrypt

buffersize = 64 * 1024
password = "foobar"

# encrypt Function
def encrypt(file):
    encrypted_file_name = file + ".aes"
    print("Encrypting file: " + file)
    pyAesCrypt.encryptFile(file,encrypted_file_name, password, buffersize)

# Decrypt function
def decrypt(file):
    print("Decrypting file:" + file)
    pyAesCrypt.decryptFile(file, "test_data.unc", password, buffersize)

# Start program
if int(len(sys.argv)) == 1:
    print(sys.argv[0] + " options: encrypt | decrypt")
elif sys.argv[1] == "encrypt":
    file = sys.argv[2]
    encrypt(file)
elif sys.argv[1] == "decrypt":
    file = sys.argv[2]
    decrypt(file)


