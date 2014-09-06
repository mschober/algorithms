wrd = '123'
wrd = '1234'
wrd = '12'
#wrd = '1'
wrd = 'a' * 99
wrd = 'a' * 20
#print wrd
wrd = 'a' * 100
wrd = 'banana'*5

def sub_words(wrd, split_size):
    while len(wrd) >= split_size:
        yield wrd[:split_size] #yield syntax is a lazy initialization, it generates the output when asked for next instead of pre-building the list
        wrd = wrd[1:]

#print list(sub_words(wrd, 2))

wrds = set([]) #use a set since under the covers it uses a hash (whereas a list iterates when looking O(n))
def update_set(wrd, wrds):
    if wrd in wrds:
        return True
    else:
        wrds.add(wrd)
        return False


def split_words_and_count(wrd, wrds, split_size=2):
    iterations = 0
    for sub in sub_words(wrd, split_size):
        iterations += 1
        if update_set(sub, wrds):
            repeated_sub = sub
        #    break #stop looking for this size once we get any old match
    wrd_len = iterations + 1
    return wrd_len, repeated_sub

wrd_len, repeated_sub = split_words_and_count(wrd, wrds) #get the length by parsing the 2 splits (cannot have repeated substring with string less than 4)
half_split_size = wrd_len /2 #due to symmetry there is no need to look at splits < 1/2 the length of the string

while half_split_size > 2:
    wrd_len, repeated_sub = split_words_and_count(wrd, wrds, half_split_size)
    if repeated_sub:
        break #found biggest, be done
    half_split_size -= 1

print wrds
print repeated_sub, len(repeated_sub) #could probably get the length of the word with more output parameters or something

#this is now a correct implementation with several great optimizations for speed, but the code is pretty heinous in terms of readability, might due for more refactoring
#another point is there was care taken to skip iterating for single characters, however edge cases were ignored
#IE. what to do with an empty string? what to do with a string that is all repeating? length < 4?

