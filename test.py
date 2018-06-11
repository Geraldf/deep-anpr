import ast

file_list = dict()
s = open('plates.txt', 'r').read()
file_list = ast.literal_eval(s)