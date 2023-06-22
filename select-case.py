# python >3.10
# https://youtube.com/shorts/-Xswnq39Q3M?feature=share
#
# PythonでもSelect case文が使えるようになっていた
#

def do_this():
    print('Doing this')
    
def do_that():
    print('Doing that')

def main():
    match input('Do this or that? '):
        case 'this':
            do_this()
        case 'that':
            do_that()
        case _:
            print('Invalid input!')


if __name__ == '__main__':
    main()