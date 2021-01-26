class DBIntegrityException(Exception):
    pass


class DBDataException(Exception):
    pass


class DBUserExistsException(Exception):
    pass


class DBUserNotExistsException(Exception):
    pass

class DBMessageCreateException(Exception):
    pass

class DBMessageNotExistsException(Exception):
    pass
