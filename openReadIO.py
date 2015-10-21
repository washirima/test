__author__ = 'Ingrid Marie'
import io
import os

testfile = open('will.html','wb')


testfile.write(bytes('this is me trying to /n'
                     'on a file with python',
                     encoding='utf8',
                     errors= 'strict'))

testfile.close()

testfile = open('will.html', 'r+')
read = testfile.read()
print(read)
