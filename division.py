def hash(k,s):
    
    return k % s

if __name__ == "__main__":
    s = int(input("enter size:"))
    k = int(input("enter key:"))
    print(hash(k,s))