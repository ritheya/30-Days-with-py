# Exercises: Level 1
# What is the most frequent word in the following paragraph?
#     paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
#     [
#     (6, 'love'),
#     (5, 'you'),
#     (3, 'can'),
#     (2, 'what'),
#     (2, 'teaching'),
#     (2, 'not'),
#     (2, 'else'),
#     (2, 'do'),
#     (2, 'I'),
#     (1, 'which'),
#     (1, 'to'),
#     (1, 'the'),
#     (1, 'something'),
#     (1, 'if'),
#     (1, 'give'),
#     (1, 'develop'),
#     (1, 'capabilities'),
#     (1, 'application'),
#     (1, 'an'),
#     (1, 'all'),
#     (1, 'Python'),
#     (1, 'If')
#     ]
import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words=re.findall(r'\b\w+\b',paragraph)
catch={}
for word in words:
    if word in catch:
        catch[word]+=1
    else:
        catch[word]=1
sorted_words=sorted(catch.items(),key=lambda x:x[1],reverse=True)
print(sorted_words)
# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) # 20
txt='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
reg_ex=r'-?\d+'
match=re.findall(reg_ex,txt)
print("points:",match)
srt_match=list(map(int,match))
print("sorted_points:",srt_match)
distance=max(srt_match)-min(srt_match)
print('distance:',distance)
# Exercises: Level 2
# Write a pattern which identifies if a string is a valid python variable
# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True
#1st
def names(args):
    return bool(re.match(r'^[a-zA-Z0-9_][a-zA-Z0-9_]*$',args))
print(names('first_name'))
print(names('first-name'))
print(names('1first_name'))
print(names('firstname'))



# Exercises: Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.
# print(clean_text(sentence));
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text=re.sub('[^a-zA-Z0-9 ]','',sentence)
print(clean_text)
sent=re.findall(r'\b\w+\b',(clean_text))
count={}
for senten in sent:
    if senten in count:
        count[senten]+=1
    else:
        count[senten]=1
final=sorted(count.items(),key=lambda x:x[1],reverse=True)
print (final[:3])
print(final)