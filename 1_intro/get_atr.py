class Login:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        """ получение доступа к атрибуту  перехватывается методом __getatribute__ """
        if item == 'secret_field' and self.password == '9ae)c':
            return 'secret value'
        else:
            return object.__getattribute__(self, item)

l = Login()
# l.secret_field --> AttributeError
#l.password = '9ae)c'
#l.secret_field --> 'secret value'

