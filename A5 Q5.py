def main():
    #write a higher-order function that takes another function as input
    def higher_order(function):
        print("This is a higher-order function.")
        function()
    def main():
        print("Hello, samrudhi!")
    higher_order(main)
if __name__=="__main__":
    main()