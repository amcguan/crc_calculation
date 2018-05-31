#Credit to: Shaurya Uppal from GeeksForGeeks Website
#https://www.geeksforgeeks.org/cyclic-redundancy-check-python/

import time
import sys

def xor(a, b):
  
    # initialize result
    result = []
  
    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
  
    return ''.join(result)
  
  
# Performs Modulo-2 division
def mod2div(divident, divisor):

    spaces = ""
    underscores = "----------------------"
    abz = ""
    afz = "0"
    arrows = ""
    shift = ""
    iter_back = 0
  
    # Number of bits to be XORed at a time.
    pick = len(divisor)
    len_div = len(divisor)
  
    for i in range(pick):
        arrows += "|"
    
    underscores = '-'*(len(divident)+7)
    # Slicing the divident to appropriate
    # length for particular step
    tmp = divident[0 : pick]

    while pick < len(divident):
  
        spaces += " "
        
        if tmp[0] == '1':
 
            if pick == len(divisor):
                print(" " + tmp + divident[pick : len(divident)])
            else:
                print(shift[iter_back:] + afz + tmp[:-1], end='', flush=True)
                #input()
                print(tmp[-1:] + divident[pick : len(divident)])
                
            iter_back = 0
            time.sleep(2)
            print(spaces + divisor)
            print(underscores)
            
            time.sleep(1)
            
            print(spaces + arrows + " XORED")
            afz = "0"
            time.sleep(2)
            # replace the divident by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + divident[pick]
  
        else:   # If leftmost bit is '0'
 
            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            afz += "0"
            iter_back += 1
            tmp = xor('0'*pick, tmp) + divident[pick]
  
        # increment pick to move further
        pick += 1
        shift += " "
  
    # For the last n bits, we have to carry it out
    # normally as increased value of pick will cause
    # Index Out of Bounds.
    
    spaces += " "
    underscores = underscores + "-"
    
    if tmp[0] == '1':
        print(shift[iter_back:] + afz + tmp + divident[pick : len(divident)])
        iter_back = 0
        time.sleep(2)
        print(spaces + divisor)
        print(underscores)
        
        time.sleep(1)
        
        print(spaces + arrows + " XORED")
        time.sleep(2)
        afz = "0"
        tmp = xor(divisor, tmp)
    else:
        iter_back += 1
        afz += "0"
        tmp = xor('0'*pick, tmp)
  
    checkword = tmp
    shift += " "
    
    print(shift[iter_back:] + afz + tmp + divident[pick : len(divident)] + " (remainder)\n")
    return checkword
  
# Function used at the sender side to encode
# data by appending remainder of modular divison
# at the end of data.
def encodeData(data, key):
    
    l_key = len(key)
  
    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    
    print("\nLength of Divisor = " + str(l_key))
    print("*Data Word will add " + str(l_key-1) + " 0's at the end")
    print("\nAlter Data: " + data + "|" + '0'*(l_key-1))
    print("Divisor:    " + key + "\n")
    remainder = mod2div(appended_data, key)
  
    # Append remainder in the original data
    codeword = data + remainder
    print("Data Word: " + appended_data)
    print("Remainder: " + str(' '*(len(data)) + remainder))
    print("Code Word: " + codeword)
    return    

input_string = input("Enter data you want to send-> ")
data =(''.join(format(ord(x), 'b') for x in input_string))
#data = "101101"
print("Input Data (in binary): " + data)

key = input("\nEnter the divisor you want to use-> ")
 
ans = encodeData(data,key)

