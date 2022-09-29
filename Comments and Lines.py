file = open("/home/niit/Desktop/Test",'r')
data = file.readlines()
count=0
comment_count=0
bool = False
prev = 0
for line in data:
    count+=1
    for i in range(len(line)):
        if line[i]=="/" and line[i+1]=="/":
            # print("Comment at line ",count)
            print("Single Line Comment ",comment_count," at line ",count)
            comment_count+=1

        if line[i]=="/" and line[i+1]=="*":
            # print("Comment from line ",count)
            bool = True
            prev = count
            comment_count+=1

        if line[i]=="*" and line[i+1]=="/" and bool==True:
            print("Multiline Comment starts at line ",prev," ends at ",count)

print("Total lines:",count)
print("Total comments:",comment_count)