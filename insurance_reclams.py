reclaims=[]
def get_reclaim()->dict:
    reclaim={}
    reclaim['id']=int(input('id ? = '))
    reclaim['amount']=float(input('amount ? = '))
    reclaim['type']=input('type ? = ')
    reclaim['status']=input('status ? = ')
    reclaim['date']=input('date ? = ')
    return reclaim

def create_reclaim():
    rc=get_reclaim()
    reclaims.append(rc)

def eval_approved_reclaims()->float:
    s=0
    for i in range(len(reclaims)):
        if reclaims[i]['status'] == 'approved':
            s+=reclaims[i]['amount']
    return s
def eval_approved_reclaims_v2()->float:
    s=0
    for reclaim in reclaims:
        if reclaim['status'] == 'approved':
            s+=reclaim['amount']
    return s

def extract_unique_types()->set:
    types=set() #empty set
    for reclaim in reclaims:
        types.add(reclaim['type'])
    return types
#returns the reclaim(dict) that have the id given as argument
def find_reclaim(id:int)->dict:
    i=0
    found=False
    while i<len(reclaims) and not found:
        if reclaims[i]['id']==id:
            found=True
        else:
            i+=1
    if not found:
        return {}
    return reclaims[i]