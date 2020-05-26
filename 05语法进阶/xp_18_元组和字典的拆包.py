def demo(*args, **kwargs):
    print(args)
    print(kwargs)
gl_args = (1, 2, 3)
gl_kwargs = {"name":"小明", "age":18}
demo(*gl_args, **gl_kwargs)