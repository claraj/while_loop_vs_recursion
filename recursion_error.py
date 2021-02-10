def main():
    print('this is the main function!')
    main()   # main calls itself - this is known as recursion
    print('after the call to main')

if __name__ == '__main__':
    main()