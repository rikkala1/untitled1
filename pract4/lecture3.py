__author__ = 'jc446932'
num = 0
out_file = open('numbers.txt',"w")
while num>=0:
     num = int(input("Number:"))
     if num>=0:
        print(str(num),file = out_file)
out_file.close()
