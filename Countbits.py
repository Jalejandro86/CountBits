def countBits(n):
    if n <= 1 or n <= 10 ** 9:
		setBits = [ones for ones in binary[2:] if ones=='1']
	else:
		raise SystemExit
    
    
    return "countBits(n) =" + setBits
	
if __name__ == "__main__":
	x = input("Input a number  ")
        if x.isdigit():
			n = bin(x)
		
    countBits(n) 