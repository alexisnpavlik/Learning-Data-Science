import time

class fiboIter():

    def __iter__(self):
        self.n1=0
        self.n2=1
        self.counter=0
        return self

    def __next__(self):
        if self.counter==0:
            self.counter+=1
            return self.n1
        elif self.counter==1:
            self.counter+=1
            return self.n2
        else:
            self.aux=self.n1+self.n2
            self.n1 , self.n2 = self.n2 , self.aux
            self.counter+=1
            return self.aux
        
    
def run():
    fibonachi=fiboIter()
  
    for i in fibonachi:
        print (i)
        time.sleep(0.05)
        if i >=1000000:
            raise StopIteration
            break

if __name__=="__main__":
    run()
        