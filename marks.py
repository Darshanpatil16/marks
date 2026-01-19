import sys
import math
def avg_marks(marks):
    
    avg=sum(marks)/len(marks)
    return avg
if  __name__ == "__main__":
    if len(sys.argv)>1:
        marks=[
            float(sys.argv[1])
            float(sys.argv[2])
            float(sys.argv[3])
        ]
        
    else:
        marks=[90,80,98,76,69]
        result=avg_marks(marks)
        print("Average Marks is:",result)
        if result>=80:
            print("A")
        else:
            print("B")
