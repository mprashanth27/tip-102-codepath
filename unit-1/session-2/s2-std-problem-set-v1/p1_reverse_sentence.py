'''
U-nderstand:
i/p = sentence: str
o/p = rev_sentence: str

Edge cases:
""
" "

P-lan:
list[s.split()]
rev_sen.join(list[-1::])

I-mplement:
'''
def reverse_sentence(sentence):
    word_list = sentence.split()
    reversed_words = reversed(word_list) # or word_list[::-1]
    rev_sen = " ".join(reversed_words)
    return rev_sen

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))

sentence = ""
print(reverse_sentence(sentence))

sentence = " "
print(reverse_sentence(sentence))