group=[
    {
        "id":11,
        "name":"Mohamed",
        "group":1,
        "birthday":"12/11/2004",
        "address":"2 flower street",
        "mark":14.37,
    },

     {
    "id":12,
    "name":"Bochra",
    "group":2,
    "birthday":"12/11/2002",
    "address":"7 dress street",
    "mark":9.5,
},
       {
    "id":13,
    "name":"salah",
    "group":2,
    "birthday":"12/11/2002",
    "address":"13 dress street",
    "mark":13.75,
},
       {
     "id":14,
    "name":"Asma",
    "group":1,
    "birthday":"12/11/2002",
    "address":"13 dress street",
    "mark":10.3,
}
]

def find_student(id):
    i=0
    while i<len(group) and group[i]["id"]!=id:
        i+=1
    if i<len(group):
        return group[i]
    return None

std1=find_student(1)
if std1 is None:
    print('The student is not found')
else:
    print(std1)
#print d1 keys
"""for key in d1.keys():
    print(key)
print(d1.keys())
#print the d1 values
for key in d1.keys():
    print(d1[key])
"""
#loop through the dictionary using (key,value)
for key,value in group[0].items():
    print(key,' : ',value)
#returns the average mark of the given group (gr)
def mark_average_by_group(gr:int)->float:
    s=0
    nb_st_gr=0
    for st in group:
        if st["group"]==gr:
            s+=st["mark"]
            nb_st_gr+=1
    return s/nb_st_gr

#find the student with the highest mark
def get_major_student()->dict:
    major:dict=group[0]
    for i in range(1,len(group)):
        if group[i]["mark"]>major["mark"]:
            major=group[i]
    return major
#test mark_average and get_major functions:
gr=int(input('Enter the group number :'))
avg=mark_average_by_group(gr)
print(f'The mark average of the group {gr} is {avg}')

major=get_major_student()
print(f'The major student is : \n{major}')

#or
print("The major student is :\n" + "\n".join(f"{key}: {value}" for key, value in major.items()))
#or
print(f'The major student is :')
for key, value in major.items():
    print(f'{key}: {value}')