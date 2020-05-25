def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        f(*args, **kwargs)
        print("Ended!")
    
    return wrapper

@func
def func2(name, ):
    print(f"I am funciton 2 {name}")

@func
def func3(age):
    print(f" I am {age} years old!")

func2("Mridul")
func3(27)




#Hi from context managers#hello from context managers