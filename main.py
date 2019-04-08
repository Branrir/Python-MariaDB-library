from MariaDBintegration import *

class RunGUI(object):
    """main class"""

    def main():
        id = 45
        name = 'test'
        MariaDBintegration.Insert_games('name', '1111', 'jrpg', 'ps4')
        MariaDBintegration.Return_games()

    if __name__ == '__main__':
        main()
