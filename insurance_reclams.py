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