import os
# from ..settings_var.settings_widget import GLOBAL_VAR

class work_with_app():
    # globalVar='Erase this test'
    screens_db: dict = {
                "screens":{},
                # "events":[],
                # "styles":[],
    }

    def __init__(self,path_dir):
        super().__init__()
        self.list_dir = path_dir

    def list_data(self):

        self.list_elements = os.listdir(self.list_dir)
        self.screens_elements: list = [ _.strip('.py') for _ in self.list_elements
                                                                if _.endswith('.py')
                                                                and not _.endswith('_events.py')
                                                                and not _.endswith('_styles.py')
                                                                and not _.endswith('db.py')
                                                                and not _.endswith('__.py')
                                    ]

        self.styles_elements: list = [ _.strip('.py') for _ in self.list_elements if _.endswith('_styles.py')]
        self.events_elements: list = [ _.strip('.py') for _ in self.list_elements if _.endswith('_events.py')]

        self.screens_db['screens']=self.screens_elements
        print(self.screens_db)

        return self.screens_db