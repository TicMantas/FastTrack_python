def my_function(a=1, b=2, c=3, **kwargs):


    age= kwargs.get('age')
    color = kwargs.get('eye_color')
    print(age, color)
    print(c)
    print(b,c)
    print(kwargs, type(kwargs))

my_function(b=5,a=10,aged=15, eyes_color='blue')