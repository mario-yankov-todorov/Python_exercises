
def remove_duplicates(func):
    def inside(a):
        a = list(dict.fromkeys(a))
        return func(a)
    return inside

@remove_duplicates
def sum_elements(a):
    x = sum(a)
    return x

if __name__ == "__main__":

    a = [5, 6, 5]
    
    x = sum_elements(a)

    print(x)