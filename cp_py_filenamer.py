'''Takes problem heading and generates a .py file name'''

s = input("Enter problem name:") # i/p = Problem 1: Reverse Sentence
s = s.lower()
s_list = s.split() # ['problem', '1:', 'reverse', 'sentence']
#print(s_list)
p_num = s_list[1][0]
p_name = "_".join(s_list[2:])
file_name = "p" + p_num + "_" + p_name + ".py"
print(file_name) # o/p = p1_reverse_sentence.py
