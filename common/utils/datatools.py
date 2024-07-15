
class InstantiatingObjects():
    '''
    将请求数据对象化
    '''
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

