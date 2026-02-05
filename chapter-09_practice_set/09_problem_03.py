'''Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
'''

def table(n,name:str):
    for i in range(1,11):
        m = n*i
        data = str(n)+" x "+str(i)+" = "+str(m)+"\n"
        with open(name,"a") as f:
            f.write(data)


for i in range(2,21):
    name = "table\multi"+str(i)+".txt"
    table(i,name)



                                