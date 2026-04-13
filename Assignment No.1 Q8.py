import inspect
import random
def main():
    a = random.randint(1, 50)
    print(inspect.getsource(random.randint))
    print(a)


if __name__ == "__main__":
    main()