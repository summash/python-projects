import re

pattern= r"[A-Z]etaphysics"
pattern2= r"is"
text='''Metaphysics is the branch of philosophy that examines the basic structure of reality. Some philosophers designate it as first philosophy to suggest that it is more fundamental than other forms of philosophical inquiry. It is traditionally seen as the study of mind-independent features of the world, but some theorists view it as an inquiry into the conceptual framework of human understanding. Metaphysics investigates the nature of existence, the features all entities have in common, and their division into categories of being. An influential division is between particulars and universals. Modal metaphysics examines what it means for something to be possible or necessary. Metaphysicians also explore the concepts of space, time, and change, and their connection to causality and the laws of nature. Other topics include how mind and matter are related, whether everything in the world is predetermined, and whether there is free will. The roots of metaphysics lie in antiquity with speculations about the nature and origin of the universe. (Full article...)
Recently featured: Stanley GreenNihilism (Alexander McQueen collection)Dominik Hašek'''

#match= re.search(pattern, text)
#match2= re.search(pattern2, text)

matches=re.finditer(pattern2,text)
for match in matches:
    #print(match)
    print(match.span())
    
matches=re.finditer(pattern,text)
for match in matches:
    #print(match)
    print(text[match.span()[0]:match.span()[1]])


#print(match)
#print(match2)