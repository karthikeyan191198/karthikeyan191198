import time
string='my name is karthi'
wordcount=len(string.split())
print(string)
while True:
    t0=time.time()
    inputtext=str(input('enter the sentence:'))
    t1=time.time()
    accuracy=len(set(inputtext.split())&set(string.split()))
    accuracy=accuracy/wordcount
    timetaken=t1-t0
    wpm=wordcount/timetaken
    print("wpm",wpm,"Accuracy",accuracy,"Timetaken",timetaken)