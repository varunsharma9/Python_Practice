# a = open('new123','w')
# a.write("dhfighduifhgiuadhfihuddffoijaoidfjfgoijadifjoaiij\nfdsfgsfhghsdfgfh")
# a.close
with open('new123', 'r') as file:
    for line in file:
        print(line, end='')  

