# -*- coding: utf-8 -*-
def repetition(letters,numberBeforeSwitch,numRepetitions):
    for i in range(numRepetitions):
        for j in range(numberBeforeSwitch):
            print letters[i]
        
    return

def main():
    repetition(['1', '2'], 2, 2)
    
if __name__ == "__main__":
    main()