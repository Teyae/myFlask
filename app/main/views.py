from . import self


@self.route('/')
def hello_world():
    return 'Hello World!'


@self.route('/map_ex')
def map_ex():
    return
