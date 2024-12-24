import sqlite3
import os

class sqlite_db:
    """
    # lite module in python to make easy work with sqlite3

    sqlite_db = sqlite_db(path_db="./exemple.db")

    # CREATE DATABASE
    sqlite_db.create_table(table_name="register", column=data_write,)

    # FIND NAME
    # fetch=5,all                               #by tabl+column
    data_returned = sqlite_db.find_name(
        table_name='register', column='user_name', name='javier')
    data_returned = sqlite_db.find_name(table_name='register', column='user_name', name='javier', match=[
                                        'user_password', 'elanimal'])  # fetch=5,all  #by tbl+column+match(column,name)

    # FIND ALL
    data_returned = sqlite_db.find_all(table_name='register')

    # WRITE DATA
    data_returned = sqlite_db.write_data(table_name='register',
                                         column=('javier53348', 'kuko', 'elanimal123'))

    # UPDATE DATA
    data_returned = sqlite_db.update_data(table_name='register',
                                          change_data=('user_name', 'javier53348'),
                                          by_data=('user_name', 'xavier53348')
                                          )
    data_returned = sqlite_db.update_data(table_name='register',
                                          change_data=('user_name', 'javier53348'),
                                          by_data=('user_name', 'xavier53348'),
                                          match=['user_email', 'email']
                                          )

    # CLEAN ALL
    data_returned = sqlite_db.remove_all(table_name='register')

    # REMOVE DATA
    data_returned = sqlite_db.remove_data(
                                    table_name='register',
                                    column_name='user_name',
                                    name='javier53348'
                    )
    data_returned = sqlite_db.remove_data(
                                    table_name='register',
                                    column_name='user_name',
                                    name='javier53348',
                                    match=['user_email', 'kuko']
                    )

    >>> print(data_returned)

    """
    real_pat='flet_box/extra_utils/external_library/flet_box_database.db'
    current_path = os.getcwd()
    full_current_path=os.path.join(current_path,real_pat)

    def __init__(self, path_db: str = 'Erase this test'):
        super().__init__()
        self.path_db=self.full_current_path

    def create_table(self, table_name: str = '', column: dict = {}):
        """
        Will return a new database

        EXEMPLE:

        sqlite_db = sqlite_db(path_db="./exemple.db")
        sqlite_db.create_table(table_name="register",column=data_write,)

        """
        body_str: str = ''
        self.conn = sqlite3.connect(self.path_db)

        for _ in zip(column.keys(), column.values()):
            body_str += f"""{_[0]} {_[1]},"""

        self.payload = f"""{body_str}"""
        self.payload = self.payload[:-1]

        self.command = f"""CREATE TABLE {table_name}( {self.payload} )"""

        try:
            cursor = self.conn.cursor()
            cursor.execute(self.command)
            print('DATABASE WAS CREATED')

        except Exception as e:
            print('PLESASE REMOVE OLD DATABASE TO CREATE NEW DATABASE', e)

    def find_name(self, table_name: str = '', column: str = '', name: str = '', fetch: str = 'all', match: list = []):
        """
        Find by name if exist

        EXEMPLE:
            connection_db = Instance_mysqlite_db.sqlite_connection(namedatabase=".book_orders.db")

            data_returned = sqlite_db.find_name(table_name='register',column='user_name',name='javier') #fetch=5,all                               #by tabl+column
            data_returned = sqlite_db.find_name(table_name='register',column='user_name',name='javier',match=['user_password','elanimal']) #fetch=5,all  #by tbl+column+match(column,name)
        """
        self.conn = sqlite3.connect(self.path_db)
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'SELECT * FROM {table_name} WHERE {column}="{name}" AND {match[0]}="{match[1]}"') if match else cursor.execute(f"SELECT * FROM {table_name} WHERE {column}='{name}'")
        except Exception as e:
            print(f"ERROR: {e}")
            return False

        if fetch == 'all':
            data_finded = cursor.fetchall()
        elif fetch == 'one':
            data_finded = cursor.fetchone()

        self.conn.commit(), cursor.close(), self.conn.close()

        if data_finded:
            return data_finded
        else:
            return False

    def find_all(self, table_name: str = 'noExist'):
        """
        Return all datatable name in database

        EXEMPLE:

        data_returned = sqlite_db.find_all(table_name='register')
        """
        self.conn = sqlite3.connect(self.path_db)
        cursor = self.conn.cursor()
        # sql=f"SHOW FULL TABLES "
        # sql=f"SHOW TABLES "
        try:
            payload = f"SELECT * FROM {table_name} "
            cursor.execute(payload)

        except Exception as e:
            print(f"ERROR: {e}")
            return False

        data_finded = cursor.fetchall()
        self.conn.commit(), cursor.close(), self.conn.close()

        if data_finded:
            return data_finded
        else:
            return False

    def write_data(self, table_name: str = '', column: tuple = ()):
        """
        Return BOL True or False if not error writing data.

        EXEMPLE:

        sqlite_db.write_data(table_name='register',column=('javier53348','kuko','elanimal123'))
        """
        self.conn = sqlite3.connect(self.path_db)
        cursor = self.conn.cursor()
        try:
            payload = f"INSERT INTO {table_name} VALUES{column}"
            wrote_data = cursor.execute(payload)

        except Exception as e:
            print(f"ERROR: {e}")
            return False

        self.conn.commit(), cursor.close(), self.conn.close()

        if wrote_data:
            return True
        else:
            return False

    def update_data(self, table_name: str = '', by_data: str = '', change_data: str = '', match=[]):
        """
        how work inside:

        1. find and Update data if data exist
        2. If no exist data return false
        3. if data exist and match exist return true else false

        EXEMPLE:

        data_returned = sqlite_db.update_data(table_name='register',
                                              change_data=('user_name', 'javier53348'),
                                              by_data=('user_name', 'xavier53348')
                        )
        data_returned = sqlite_db.update_data(table_name='register',
                                            change_data=('user_name', 'javier53348'),
                                            by_data=('user_name', 'xavier53348'),
                                            match=['user_email', 'email']
                        )
        """
        # (modifica SET) (donde WHERE) y (AND condicional)
        self.conn = sqlite3.connect(self.path_db)
        crusor = self.conn.cursor()

        try:
            """
            find exist name to be changed

            find_name = crusor.execute(f'SELECT * FROM {table_name} WHERE {change_data[0]}="{change_data[1]}"')
            equal_name = crusor.fetchone()

            """
            crusor.execute(f'SELECT * FROM {table_name} WHERE {change_data[0]}="{change_data[1]}"')

            equal_name = crusor.fetchone()

            if equal_name:

                if match:
                    '''if match is writed'''
                    try:
                        """
                        find exist name tin match o be changed

                        find_match = crusor.execute(f'SELECT * FROM {table_name} WHERE {match[0]}="{match[1]}"')
                        equal_match = crusor.fetchone()

                        """

                        crusor.execute(f'SELECT * FROM {table_name} WHERE {match[0]}="{match[1]}"')
                        equal_match = crusor.fetchone()

                        if equal_match:
                            '''if equal_match appear'''
                            payload = f"UPDATE {table_name} SET {by_data[0]}='{by_data[1]}' WHERE {change_data[0]}='{change_data[1]}' AND {match[0]}='{match[1]}' "
                        else:
                            return False

                    except Exception as e:
                        print(f"ERROR: {e}")
                        return False
                else:
                    payload = f"UPDATE {table_name} SET {by_data[0]}='{by_data[1]}' WHERE {change_data[0]}='{change_data[1]}' "
                try:
                    update_data = crusor.execute(payload)

                except Exception as e:
                    print(f"ERROR: {e}")
                    return False

                self.conn.commit(), crusor.close(), self.conn.close()

                if update_data:
                    return True
                else:
                    return False
            else:
                print('No exist')
                return False

        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def remove_all(self, table_name=''):
        """
        EXEMPLE:

        data_returned = sqlite_db.remove_all(table_name='register')
        """
        self.conn = sqlite3.connect(self.path_db)
        try:
            crusor = self.conn.cursor()
            crusor.execute(f'DELETE from {table_name}').fetchall()
            self.conn.commit(), crusor.close(), self.conn.close()

        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def remove_data(self, table_name: str = '', column_name: str = '', name: str = '', match: list = []):
        """
        EXEMPLE:

        data_returned = sqlite_db.remove_data(
                                        table_name='register',
                                        column_name='user_name',
                                        name='javier53348'
                        )
        data_returned = sqlite_db.remove_data(
                                        table_name='register',
                                        column_name='user_name',
                                        name='javier53348',
                                        match=['user_email', 'kuko']
                        )
        """

        self.conn = sqlite3.connect(self.path_db)
        crusor = self.conn.cursor()
        sql = ''

        if match:
            '''
            if match is writed

            find_name = crusor.execute(f'SELECT * FROM {table_name} WHERE {column_name}="{name}"')
            equal_name = crusor.fetchone()

            '''
            data = True
            try:
                find_name = crusor.execute(f'SELECT * FROM {table_name} WHERE {column_name}="{name}"')
                equal_name = crusor.fetchone()
                find_match = crusor.execute(f'SELECT * FROM {table_name} WHERE {match[0]}="{match[1]}"')
                equal_match = crusor.fetchone()

                if find_name and equal_match:
                    sql = f"DELETE from {table_name} WHERE {column_name}='{name}' AND {match[0]}='{match[1]}' "
                else:
                    sql = f"DELETE from {table_name} WHERE {column_name}='{name}' AND {match[0]}='{match[1]}' "
                    data = 'no exist match user'
                    return data

            except Exception as e:
                print(f"ERROR: {e}")
                return False
        else:
            try:
                """
                find exist name to be erase

                find_name = crusor.execute(f'SELECT * FROM {table_name} WHERE {column_name}="{name}"')
                equal_name = crusor.fetchone()
                """
                data = True

                find_name = crusor.execute(f'SELECT * FROM {table_name} WHERE {column_name}="{name}"')
                equal_name = crusor.fetchone()
                if equal_name:
                    sql = f"DELETE from {table_name} WHERE {column_name}='{name}'"
                else:
                    print('No exist')
                    data = 'no exist match user'
            except Exception as e:
                print(f"ERROR: {e}")
                return False
        try:
            """Always will be executed"""
            crusor.execute(sql)
            self.conn.commit(), crusor.close(), self.conn.close()
            return data

        except Exception as e:
            print(f"ERROR: {e}")
            return False


if __name__ == '__main__':
    from create_skelenton import data_input

    data_write = {
        'user_name': 'TEXT',
        'user_email': 'TEXT',
        'user_password': 'TEXT',
        'time_created': 'TEXT',
    }
    screen_write = {
        'user_name': 'TEXT',
        'main_screen': 'TEXT',
        'screen_one': 'TEXT',
        'screen_two': 'TEXT',
        'screen_three': 'TEXT',
        'screen_four': 'TEXT',
        'screen_five': 'TEXT',
        'screen_six': 'TEXT',
        'screen_seven': 'TEXT',
        'screen_eigth': 'TEXT',
        'screen_nine': 'TEXT',
        'screen_ten': 'TEXT',
        'screen_eleven': 'TEXT',
        'screen_twelve': 'TEXT',
    }
    sqlite_db = sqlite_db(path_db="./flet_box_database.db")

    # BASIC C.R.U.D
    #:= CREATE DATABASE
    # sqlite_db.create_table(table_name="register", column=data_write,)
    # sqlite_db.create_table(table_name="user_screen", column=screen_write,)
    #
    #:= REMOVE ALL
    # data_returned = sqlite_db.remove_all(table_name='register')
    # #
    # REMOVE DATA
    # data_returned = sqlite_db.remove_data(
    #                                 table_name='register',
    #                                 column_name='user_name',
    #                                 name='javier53348'
    #                 )
    # data_returned = sqlite_db.remove_data(
    #                                 table_name='register',
    #                                 column_name='user_name',
    #                                 name='javier53348',
    #                                 match=['user_email', 'kuko']
    #                 )
    #:= WRITE DATA
    # data_returned = sqlite_db.write_data(table_name='register',
    #                                      column=('javier53348', 'kuko53348@gmail.com', 'elanimal123','5444656'))
    # data_returned = sqlite_db.write_data(table_name='register',
                                         # column=('juan', 'juan53348@gmail.com', 'juan123','54544656')
                                         # )
    # data_returned = sqlite_db.write_data(table_name='user_screen',
    #                                      column=(
    #                                             'user_demo',
    #                                             data_input,
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None',
    #                                             'None'
    #                                         )
    #                                      )
    print(data_input)
    # # UPDATE DATA
    # data_returned = sqlite_db.update_data(table_name='register',
    #                                       change_data=('user_name', 'javier53348'),
    #                                       by_data=('user_name', 'xavier53348')
    #                                       )

    # data_returned = sqlite_db.update_data(table_name='register',
    #                                       change_data=('user_name', 'javier53348'),
    #                                       by_data=('user_name', 'xavier53348'),
    #                                       match=['user_email', 'email']
    #                                       )
    data_returned = sqlite_db.update_data(table_name='user_screen',
                                          change_data=('user_name', 'user_demo'),
                                          by_data=('main_screen', data_input)
                                         )
    #:= FIND NAME
    # fetch=5,all                               #by tabl+column
    # data_returned = sqlite_db.find_name(
    #                                 table_name='register',
    #                                 column='user_name',
    #                                 name='javier'
    #                 )

    # FIND BY NAME
    # data_returned = sqlite_db.find_name(table_name='register',
    #                                       column='user_name',
    #                                       name='javier',
    #                                       match=[ 'user_password', 'elanimal']
    #                 )  # fetch=5,all  #by tbl+column+match(column,name)

    # FIND ALL
    # data_returned = sqlite_db.find_all(table_name='register')
    # print(data_returned)
