# phone to word

from sys import argv

w2n=[
    'O_O',
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz',
]

def find_letter(letter):
    try:
    	return str(w2n.index([x for x in w2n if letter in x][0])+1)
    except Exception:
        return ' '

try:
    raw_num=argv[1]
    processed_num=''.join([find_letter(i) if i.isalpha() else i for i in raw_num])
    print(processed_num)
except Exception:
    print('Sorry, there was an error!')

# Try: 1-833-magwrld
