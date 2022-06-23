from time_def import time_def


def p_def():
    @time_def
    def my_def():
        return

    @time_def
    def my_def_args(*args):
        return args

    @time_def
    def my_def_kwargs(**kwargs):
        return kwargs

    @time_def
    def my_def_args_and_kwargs(*args, **kwargs):
        return args, kwargs

    assert my_def() is None
    assert my_def_args(1, "2", {1: 1}, (2, 2)) == (1, "2", {1: 1}, (2, 2))
    assert my_def_kwargs(a=1, b=2) == {"a": 1, "b": 2}
    assert my_def_args_and_kwargs(1, 2, 3, a=1, b=2) == ((1, 2, 3), {"a": 1, "b": 2})

if __name__ == '__main__':
    p_def()
