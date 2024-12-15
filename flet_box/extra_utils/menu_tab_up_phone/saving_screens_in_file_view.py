import os

# from write_file_proyect import file_saved
# from ..screen_manager.write_file_proyect import file_saved

class saving_screens_in_file:
    """
    THIS MODULE WRITE ALL SCREENS AVIABLES IN APP

    PATH: 'test/proyect_name/proyect_name/controls/app_screen_manager.py'

    #: THIS MODULE LET YOU MANAGE ALL SCREENS IN APP
    #: YOU MAY CHANGE BETWEEN SCREENS TO EASY

    import saving_screens_in_file

    saving_screens_in_file(
        screens_list_name=['hello','world'],
        path_to_write=['/hello/hello/'],
        )

    RETURN:

    from .views.main_screen import main_screen
    # from .views.main_screen_events import *

    screens: dict={
        'main_screen': main_screen(),
        }

    """
    all_dict_imports = list()
    all_data = "#: THIS MODULE LET YOU MANAGE ALL SCREENS IN APP\n#: YOU MAY CHANGE BETWEEN SCREENS TO EASY\n\n"
    tabulation = "\t"

    def __init__(   self,
                    screens_list_name: list = [],
                    path_to_write: str = "",
                    ):

        super().__init__()
        self.list_screens = screens_list_name

        self.make_all_imports()
        self.make_screen_dict()

        self.full_screen_path = os.path.join(path_to_write, "app_screen_manager.py")

        # ==============================================
        # WRITE DATA OF ALL SCREENS
        self.file_saved(
            full_path=self.full_screen_path,
            data_code=self.all_data,
        )
        # ==============================================

        # IS NECESSARY CLEAR DICT THAT HAVE ALL SCREEN TO AVOID DUPLICATES FILES
        self.all_dict_imports.clear()

        # RUN ONLY IN PRODUCTION
        # print(self.all_data)
        # print(self.full_screen_path)

    def file_saved(
                    self,
                    full_path: str = "",
                    data_code: str = ""
                    ):

        with open(full_path, "w") as f:
            f.write(data_code)

    def make_all_imports(self):
        """
        WILL RETURN:

        #: THIS MODULE LET YOU MANAGE ALL SCREENS IN APP
        #: YOU MAY CHANGE BETWEEN SCREENS TO EASY

        from .views.hello import hello
        # from .views.hello_events import *

        from .views.world import world
        # from .views.world_events import *

        """
        for _ in self.list_screens:
            #: SAVE ALL IMPORT PATH
            self.tmp_screen_data = f"from .views.{_} import {_}\n"
            self.tmp_events_data = f"# from .views.{_}_events import *\n\n"

            #: ADD STR TO MIX DATA
            self.all_data += self.tmp_screen_data + self.tmp_events_data

            #: SAVE ALL IMPORT SCREENS
            if len(self.list_screens) == 1:
                self.tmp_data = f"'main_screen': {_}(),\n"
            else:
                self.tmp_data = f"'{_}': {_}(),\n"


            self.all_dict_imports.append(self.tmp_data)

    def make_screen_dict(self):
        """
        WILL RETURN:

        screens: dict={
                'main_screen': main_screen(),
                'second_screen': second_screen(),
                }
        """
        #: ADD STR TO MIX DATA

        self.all_data += "screens: dict={\n"

        for _ in self.all_dict_imports:
            self.all_data += f"{self.tabulation}{_}"

        self.all_data += self.tabulation + "}"

if __name__ == '__main__':
    saving_screens_in_file(
        screens_list_name=['hello','world'],
        path_to_write=['/hello/hello/'],
        )