#!/usr/bin/python

key = input("Enter API key from free.currencyconverterapi.com: ")
f = open("converter_key.txt", 'w')
f.write(key)
f.close()


