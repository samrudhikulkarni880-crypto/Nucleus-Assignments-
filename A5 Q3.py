def main():
    #write a function to return multiple values(ex.sum and average)
    def sum_and_average(numbers):
        total = sum(numbers)
        average = total 
        return total, average

    num_list = [10, 20, 30, 40, 50]
    sum_result, avg_result = sum_and_average(num_list)
    print("Sum:", sum_result)
    print("Average:", avg_result)

if __name__ == "__main__":
    main()