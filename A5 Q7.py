def main():
    #write a function that sorts an array using a custom comarison function
    def sort(arr, comparison_func):
        return sorted(arr, key=comparison_func)
    arr = [8,4,2,6,1,5,3,7]
    sorted_arr = sort(arr, lambda x: x)
    print("Sorted array:", sorted_arr)
if __name__=="__main__":
    main()
