import numpy as np

def main():
    evaluate_data()

def evaluate_data():
    A=[[4/19,2/11,1/2],[7/19,7/11,1/14],[8/19,2/11,3/7]]
    x0=np.random.rand(3,1)
    print('Inizializzo lo stato casuale x0=',x0)
    print()
    x0=x0/np.sum(x0)
    print('Ho reso x0 stocastico', x0)
    print()
    for i in range(50):
        if(i%10==0 or i==49):
            print('x0=',x0)
            print()

if __name__== "__main__":
    main()
