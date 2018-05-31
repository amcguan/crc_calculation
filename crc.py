import time

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
  
    for i in range(pick-1):
        abz += "0"
        arrows += "|"
    
    arrows += "|"
    
    # Slicing the divident to appropriate
    # length for particular step
    tmp = divident[0 : pick]

    while pick < len(divident):
  
        time.sleep(1)
        spaces += " "
        underscores = underscores + "-"
        
        if tmp[0] == '1':
            if pick == len(divisor):
                print(" " + tmp + divident[pick : len(divident)] + abz)
            else:
                print(shift[iter_back:] + afz + tmp + divident[pick : len(divident)] + abz)
            iter_back = 0
            print(spaces + divisor)
            print(underscores)
            time.sleep(1)
            print(spaces + arrows)
            afz = "0"
  
            # replace the divident by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + divident[pick]
  
        else:   # If leftmost bit is '0'
 
            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            afz += "0"
            #shift = shift[:-1]
            iter_back += 1
            tmp = xor('0'*pick, tmp) + divident[pick]
  
        # increment pick to move further
        pick += 1
        shift += " "
  
    # For the last n bits, we have to carry it out
    # normally as increased value of pick will cause
    # Index Out of Bounds.
    
    spaces += " "
    #shift = shift[:-1]
    underscores = underscores + "-"
    
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
        afz = "0"
    else:
        tmp = xor('0'*pick, tmp)
        afz += "0"
  
    checkword = tmp
    
    print(shift[iter_back:] + afz + tmp + divident[pick : len(divident)] + abz)
    print("Remainder: " + checkword)
    return checkword
  
# Function used at the sender side to encode
# data by appending remainder of modular divison
# at the end of data.
def encodeData(data, key):
  
    l_key = len(key)
  
    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
  
    # Append remainder in the original data
    codeword = data + remainder
    return codeword    

input_string = input("Enter data you want to send-> ")
key = input("Enter key you want to use-> ")

data =(''.join(format(ord(x), 'b') for x in input_string))
print("Data: " + data)
print("Key: " + key + "\n")
 
ans = encodeData(data,key)
print(ans)
