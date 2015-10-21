__author__ = 'Ingrid Marie'
import copy
import keyword
import sys
import pickle

print(keyword.iskeyword('if'))

print(keyword.kwlist)


print(sys.version)
mySaveDOC = ['william','james','peter']

save_file = open('pickle.pdf' , 'wb')
pickle._dump(mySaveDOC, save_file)
save_file.close()