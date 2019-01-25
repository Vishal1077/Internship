#Challenge 1st
text = 0
with open('james_joyce_ulysses.txt', 'r') as novel:
    for v in novel:
        test = v.split()
        text += len(test)
        #print test
print "Total words in james_joyce_ulysses novel:-",text



#or




# we don't care about case sensitivity and therefore use lower:
import re
ulysses = open("james_joyce_ulysses.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", ulysses)
print("Total words in james_joyce_ulysses novel:- " + str(len(words)))






#Challenge 2nd
#(a)
for word in ["the", "while", "good", "bad", "ireland", "irish"]:
    print(word + "=" + \
          str(words.count(word)))

#(b)
diff_words = set(words)
print("Total different words :- " + str(len(diff_words)))





#Challenge 3rd
novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis_kafka.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt', 
          'james_joyce_ulysses.txt', 
          'moby_dick_melville.txt']
for novel in novels:
    txt = open(novel).read().lower()
    words = re.findall(r"\b[\w-]+\b", txt)
    diff_words = set(words)
    n = len(diff_words)
    print("{name:38s}: {n:5d}".format(name=novel[:-4], n=n))





#Challenge 4th
words_in_novel = {}
for novel in novels:
    txt = open(novel).read().lower()
    words = re.findall(r"\b[\w-]+\b", txt)
    words_in_novel[novel] = words
    
words_only_in_ulysses =  set(words_in_novel['james_joyce_ulysses.txt'])
novels.remove('james_joyce_ulysses.txt')
for novel in novels:
    words_only_in_ulysses -= set(words_in_novel[novel])
    
with open("words_only_in_ulysses.txt", "w") as fh:
    txt = " ".join(words_only_in_ulysses)
    fh.write(txt)
    
print(len(words_only_in_ulysses))





#Challenge 5th
# we start with the words in ulysses
common_words = set(words_in_novel['james_joyce_ulysses.txt'])
for novel in novels:
    common_words &= set(words_in_novel[novel])
    
print(len(common_words))

