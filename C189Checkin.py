import requests, time

def main():
    gonghao='{{ secrets.gh }}'
    shoujihao='{{ secrets.sjh }}'
    url="http://xg.sqxy.edu.cn/xgh5/openData"
    r = requests.Session()
    riqi=time.strftime('%Y-%m-%d',time.localtime(time.time())) #年-月-日   格式的当天日期
    #riqi="2020-08-06"
    payload={
        'command': 'XGXT',
        'param': {"cmd":"yqsbFormSave","xh":"004154","sbsj":riqi,"nl":"30","lxfs":"15736990255","jzdq":"410782","jzdq_xxdz":"南村镇南村北村","tw":"36.5","sflx":"0","jcbr":"0","zyzz":"1,","fbrq":"","zyzzms":"","bz":"","bz1":"","wcjtgj":"","wcjtgjxq":"","wcdq":"","wcdqxxdz":"","lkdate":"","fhdate":"","zszt":""}
    }
    #params="command=XGXT&param=%7B%22cmd%22%3A%22yqsbFormSave%22%2C%22xh%22%3A%22004154%22%2C%22sbsj%22%3A%22"+riqi+"%22%2C%22nl%22%3A%2230%22%2C%22lxfs%22%3A%2215736990255%22%2C%22jzdq%22%3A%22410782%22%2C%22jzdq_xxdz%22%3A%22%E5%8D%97%E6%9D%91%E9%95%87%E5%8D%97%E6%9D%91%E5%8C%97%E6%9D%91%22%2C%22tw%22%3A%2236.5%22%2C%22sflx%22%3A%220%22%2C%22jcbr%22%3A%220%22%2C%22zyzz%22%3A%221%2C%22%2C%22fbrq%22%3A%22%22%2C%22zyzzms%22%3A%22%22%2C%22bz%22%3A%22%22%2C%22bz1%22%3A%22%22%2C%22wcjtgj%22%3A%22%22%2C%22wcjtgjxq%22%3A%22%22%2C%22wcdq%22%3A%22%22%2C%22wcdqxxdz%22%3A%22%22%2C%22lkdate%22%3A%22%22%2C%22fhdate%22%3A%22%22%2C%22zszt%22%3A%22%22%7D"
    params="command=XGXT&param=%7B%22cmd%22%3A%22yqsbFormSave%22%2C%22xh%22%3A%22"+gonghao+"%22%2C%22sbsj%22%3A%22"+riqi+"%22%2C%22nl%22%3A%2230%22%2C%22lxfs%22%3A%22"+shoujihao+"%22%2C%22jzdq%22%3A%22410782%22%2C%22jzdq_xxdz%22%3A%22%E5%8D%97%E6%9D%91%E9%95%87%E5%8D%97%E6%9D%91%E5%8C%97%E6%9D%91%22%2C%22tw%22%3A%2236.5%22%2C%22sflx%22%3A%220%22%2C%22jcbr%22%3A%220%22%2C%22zyzz%22%3A%221%2C%22%2C%22fbrq%22%3A%22%22%2C%22zyzzms%22%3A%22%22%2C%22bz%22%3A%22%22%2C%22bz1%22%3A%22%22%2C%22wcjtgj%22%3A%22%22%2C%22wcjtgjxq%22%3A%22%22%2C%22wcdq%22%3A%22%22%2C%22wcdqxxdz%22%3A%22%22%2C%22lkdate%22%3A%22%22%2C%22fhdate%22%3A%22%22%2C%22zszt%22%3A%22%22%7D"
    xiangying=r.post(url, params = params)
    jieguo=xiangying.text #dict形式，但是是str格式
    jieguo=eval(jieguo) #字符串转字典类型，就可以使用dict方法操作
    print(jieguo["message"])
    return 1
    

if __name__ == "__main__":
    main()
