s = input()

answers = []
characters = [0] * 26

for c in s:
    characters[ord(c)-97] += 1

def gen(chars, string):
    chars = chars[::]
   
    if len(string) == len(s):
        
        answers.append(string)
        return

    for i in range(26):
        
        if chars[i] > 0:
    
            tempstr = string + chr(97+i)
            chars[i] -= 1
            gen(chars, tempstr)
            chars[i] += 1

gen(characters, "")

print(len(answers))
for a in answers:
    print(a)

            
            
    
