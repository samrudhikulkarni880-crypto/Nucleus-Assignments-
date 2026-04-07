def main():
    #write a function that acceps a variable number of arguments
    
    def variable_args(*args):
        for arg in args:
            print(arg)
    
    variable_args(7, "Hello", "Samrudhi")

if __name__=="__main__":    
    main()