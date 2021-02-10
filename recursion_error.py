def main():
    print('this is the main function!')
    main()   # main calls itself - this is known as recursion
    print('this never prints because main never returns')

if __name__ == '__main__':
    main()