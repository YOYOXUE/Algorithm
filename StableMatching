import random
def ReadToDict(filename):
    preferred_dict={}
    try:
        file=open(filename)
    except:
        print('cannot find file:'),filename)

    for line in file:
        name=line.split(';')[0].strip()
        preferred_list=[]
        for preferred in line.replace(name+':','').strip().split(' '):
            preferred_list.append(preferred)
        preferred_dict[name]=preferred_list
    file.close()
    return preferred_dict
    
def FindABoy(boys_state):
    while True:
        index=random.randint(0,len(boys_state)-1)
        if boys_state[index]=='FREE':
            return 'B'+str(index)

def FindAGirl(preferred_list):
    for i in range(len(preferred_list)):
        if preferred_list[i][0]=='G':
            preferred_list[i]=preferred_list[i[.lower()
            return preferred_list[i].upper()
   
 def StableMatching(boys_dict,girls_dict):
     boys_state=['FREE' for i in boys_dict]
     girls_state=['FREE' for i in girls_dict]
     while True:
         if 'FREE' not in boys_state:
             return boys_state
         boy_name=FindABoy(boys_state)
         boy_index=int(boy_name.replace('B',''))
         girl_name=FindAGirl(boys_dict[boys_name])
         girl_index=int(girl_name.replace('G',''))
         if girls_state[int(girl_index)]=='FREE':
             girls_state[girl_index]=boy_name
             boys_state[boy_index]=girl_name
         elif girls_dict[girl_name].index(boy_name)<girls_dict[girl_name].index(girls_state[girl_index]):
             boys_state[int(girls_state[girl_index].replace('B',''))]='FREE'
             girls_state[girl_index]=boy_name
             boys_state[boy_index]=girl_name
         else:pass
     return 'Never be here'
     
if __name__='__main__':
    boys_dict=ReadToDict('boys_rankings.txt')
    girls_dict=ReadToDict('girls_rankings.txt')
    print(StableMatching(boys_dict,girls_dict))
