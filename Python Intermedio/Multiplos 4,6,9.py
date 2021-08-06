def run():
    mutiplo=[x for x in range(1,10000) if x%4==0 and x%6==0 and x%9==0]
    print(mutiplo)
    
if __name__=='__main__':
    run()