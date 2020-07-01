class A(object):

    def __init__(self):
        self._user_id = 0

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if value == 10:
            self._user_id = value

    @user_id.deleter
    def user_id(self):
        del self._user_id


class B(object):
    def __init__(self):
        self._user_id = 0

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        if value == 10:
            self._user_id = value

    def del_user_id(self):
        del self._user_id

    user_id = property(get_user_id, set_user_id, del_user_id, "用户id")


if __name__ == '__main__':
    a = A()
    a.user_id = 100
    print(a.user_id)
    del a.user_id

    b = B()
    b.user_id = 100
    print(b.user_id)
    del b.user_id
