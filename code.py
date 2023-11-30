def create_f(filename): #This function will create a empty file on desktop,   mode of file-r=read,w=write,a=append
    file=open(f'{filename}.txt','a')
    file.close()
    print('File is created on desktop...')

def addf (text,filename):# This function will add a text in file without overriding 
    file=open(f'{filename}.txt','a')
    char=file.write(f'\n{text}')
    print('you have successfully written in file')
    file.close()
    
def readf(filename): 
    file=open(f'{filename}.txt','r')
    content=file.read()
    file.close()
    print(content)


def writef(text,filename): #this will override data in file
    file=open(f'{filename}.txt','w')
    char=file.write(text) #this will give the total length of characters in file
    print(f'You have successfully reaplaced text in file.')
    file.close()
    
def dataf(data,filename): #if we have to save data in table like structure with columns ID,NAME,AGE,PLACE 
    file=open(f'{filename}.txt','a')
    for i,n,a,p in data:
        file.write(f'\n{i:5} {n:10} {a:3} {p:20}\n')
        print(f'{i:^5} {n:^10} {a:^3} {p:^20}')
    file.close()


while True:
    print('\n=====Welcome in system=====\n')
    print('Select a work:\n1.Create text file. \n2.Read file.\n3.Add text in text file.\n4.Replace data in text file.\n5.Structural record file.\n6.Exit')
    s=int(input('Enter your selection: '))
    if s==1:
        fn=input('Enter name of file: ')
        create_f(fn)
    elif s==2:
        fn=input('Enter file name: ')
        readf(fn)

    elif s==3:
        fn=input('Enter file name in which you want to add text: ')
        txtdata=input('Enter text to be added in file: ')
        addf(txtdata,fn)
        
    elif s==4: 
        fn=input('Enter file name in which you want to replace text: ')
        txtdata=input('Enter text to be replaced in file: ')
        writef(txtdata,fn)
        

    elif s==5:
        fn=input('Enter file name: ')
        ids=input('Enter ID: ')
        na=input('Enter Name: ')
        age=input('Enter age: ')
        place=input('Enter Place: ')
        data=[[ids,na,age,place]]
        dataf(data,fn)
    else:
        break
        
            
        
