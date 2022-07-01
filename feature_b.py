def pyramid(n):
    for i in range(n):
        print(" "*(n-i)+"*"*i+"*"*(i-1))

if __name__ == '__main__':
    pyramid(int(input("Pyramid Level :")))