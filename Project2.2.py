def most_frequent(s):
    set1=set(s)
    dic={}
    for i in set1:
        if i==" ":
            continue
        else:
            dic[i]=s.count(i)
    print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
s=input("Please enter a string:")
most_frequent(s)