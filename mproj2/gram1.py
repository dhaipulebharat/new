import json
from gingerit import GingerIt
def resp(msg):
    co= GingerIt().parse(msg)
    print(co)
    res=""
    res+=co['result']
    print(res)
    return res


def resp1(msg1):
    co= GingerIt().parse(msg1)
    print(co)
    res=""
    for i in co['corrections']:
        res+=(i['text']+"\t\t------->\t"+i['correct']+"\n")
        print(i['text'],"\t------->\t",i['correct'])
    return res