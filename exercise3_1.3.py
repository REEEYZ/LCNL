###############################################################################
import random


def main():
    
    test = []
    mask = ["masked", "nonmasked", "masked"]
    direction = ["left", "right"]
    for i in range(5):
        for j in range(6):
            num = i + 1
            maskChoice = random.choice(mask)
            direc = random.choice(direction)
            test.append([num, maskChoice, direc])
            
    
    random.shuffle(test)
    for i in range(len(test)):
        for j in range(len(test[i])):
            print(test[i][j]),
        print ""
        
        
        

    
if __name__ == "__main__":
    main()
    
    
    
###############################################################################

