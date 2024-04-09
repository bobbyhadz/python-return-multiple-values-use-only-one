# Return multiple values and only use One in Python

def my_func():
    return ['a', 'b', 'c', 'd']


# ✅ by unpacking values

_, _, c, _ = my_func()
print(c)  # 👉️ 'c'

_, b, *_ = my_func()
print(b)  # 👉️ 'b'