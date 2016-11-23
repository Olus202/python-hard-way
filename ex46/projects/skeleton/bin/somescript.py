def create_list():
    some_list = ['a', 'b', 'c']
    return some_list

def join_list():
    sl = create_list()
    together = "-".join(sl)
    print together

if __name__ == "__main__":
    join_list()
