# AES-EAX Cryptography Lab

This is a small Python lab I kept because it helped me understand authenticated encryption in a more practical way.

The folder contains two related exercises. They are not meant to represent a production login system or a complete cryptography project.

## AES-EAX Login Demo

In this exercise I generated a random password, encrypted it with AES-EAX and then verified it through the same key, nonce and authentication tag.

I practiced:

- secure random password generation with `secrets`
- AES-128
- AES-EAX
- nonce handling
- authentication tags
- basic integrity verification

## AES-EAX CTF Challenge

This second exercise uses the same AES-EAX concepts in a small CTF-style flow where a message is encrypted and later recovered.

I practiced:

- UTF-8 encoding
- random key generation
- encryption and decryption
- nonce handling
- `decrypt_and_verify`
- basic exception handling

## What I learned

The main thing I took from these exercises was the difference between confidentiality and integrity. AES-EAX helped me see how both can be handled in the same encryption process.

One important limitation of the login exercise is that real password storage should normally use secure password hashing rather than reversible encryption. I keep the example here as a learning exercise, not as a recommended authentication design.
