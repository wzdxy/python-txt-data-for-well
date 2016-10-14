def task(filename):
    rightHeads=[]
    print ('正在处理: ['+filename+'] ...')
    patch_file_url="./old/"+filename
    patch_file=open(patch_file_url,'r')        #打开文档，逐行读取数据
    new_file_url="./new/"+filename
    new_file=open(new_file_url,'w')
    i=0
    for line in open(patch_file_url):
        line=patch_file.readline()
        line=line.replace('\n','')
        if i==0:
            heads=line.split("\t")
            # print (heads)
            for index in range (len(heads)):
                if heads[index]=='AC' or heads[index]=='GR' or heads[index]=='DEN' or heads[index]=='RT' or heads[index]=='RLLD' or heads[index]=='ac' or heads[index]=='gr' or heads[index]=='den' or heads[index]=='rt' or heads[index]=='rlld':
                    rightHeads.insert(len(rightHeads),index)            
            if 'RT' in heads and 'RLLD' in heads:
                rightHeads.remove(heads.index('RLLD'))
            if 'rt' in heads and 'rlld' in heads:
                rightHeads.remove(heads.index('rlld'))
            if 'rt' in heads and 'RLLD' in heads:
                rightHeads.remove(heads.index('RLLD'))
            if 'RT' in heads and 'rlld' in heads:
                rightHeads.remove(heads.index('rlld'))            
            if len(rightHeads)<4:
                print('['+filename+'] 项数不足：跳过')
                new_file.close()

                return -1;
            headStr=''
            for index in range (len(rightHeads)):
                headStr+=heads[rightHeads[index]]
                if index!=len(rightHeads)-1:
                    headStr+='\t'
                else:
                    headStr+='\n'
            new_file.write(headStr)      
        
        if i>0:
            datas=line.split("\t")
            newStr=''
            for index in range (len(rightHeads)):
                newStr+=datas[rightHeads[index]]
                if index!=len(rightHeads)-1:
                    newStr+='\t'
                else:
                    newStr+='\n'
            # print ('行：'+str(i))
            # print (newStr)
            new_file.write(newStr)
        i=i+1
    # print ('Write File...')
    new_file.close()
    print('['+filename+'] 处理完成')
    return 0

def main():
    import os 
    import time
    path='./old'
    for root,dirs,files in os.walk(path):
        startTime=time.time()
        print ('—— 开始处理 —— \n要处理的文件数量：'+str(len(files)))
        for item in files:
            r=task(item)
            if r==0:
                print ('已完成第'+str(files.index(item)+1)+'个文件, 还剩'+str(len(files)-files.index(item)-1)+'个')
            elif r==-1 and os.path.exists('./new/'+item):
                os.remove('./new/'+item)
    endTime=time.time()                            
    print ('ALL Done in '+str(int(endTime-startTime))+' seconds !')



# task()
main()
