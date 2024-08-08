from flet import Container ,ElevatedButton ,Page


def create_index_page(module_path='./test/data_in_module.py',widget_screen = 'screen'):
    """
    CREATE DATABASE OF ALL WIDGET

    >>> from views.building_code_traslator import create_index_page
    >>> create_index_page(module_path ='./test/views/SCREENS_DB.py',widget_screen=self.data_share)

    """


    with open(module_path,'w') as f:

        delete = widget_screen.__dict__.get('_Control__page').index
        # DELETE SPECIFICS WIDGETS NAME
        # delete = .pop('page')
        # delete = delete.pop('View')

        del delete['page']
        # del delete['Container_exemple()']
        code_to_traslate = f"{delete}"

        f.write(code_to_traslate)

    with open(module_path,'r') as f:
        data_change = f.read().replace(", '_", ",\n'_")
        with open(module_path,'w') as f:
            f.write(data_change)



def tralating_index_page(
                            read_module_path  = './test/data_in_module.py',
                            write_module_path = './test/views/FLET_TRASLATED_SCREEN_DB.py',
                            code_to_traslate  = 'EXEMPLE ft.Container()' ,
                            show              = True,
                            write_lines       = False,
                            ):
    """
    TRASLATOR MODULE IS DON TO TRASLATE ANY WIDGET TO STR() BUT CAHNGING SOME CHARACTES ('{
    TO EXPORT AND SAVE PROYECT

    from building_code_traslator import tralator_flet_code_to_py
    tralator_flet_code_to_py(
                        module_path      ='./test/data_in_module.py',
                        code_to_traslate = self.data_share,
                        )
    original Container(height=30, bgcolor='#44CCCC00', onclick=True, padding='{"l":8,"t":8,"r":8,"b":8}')
    returned Container(height=30, bgcolor='#44CCCC00', onclick=True, padding={"l":8,"t":8,"r":8,"b":8})
    """
    # with open(module_path,'w') as f:
    #     code_to_traslate = f"{code_to_traslate.__repr__()}"
    #     f.write(code_to_traslate)

    import_module = 'from flet import *'
    data =  """
def read_database_dict(index_widget):
    global SCREEN_APP
    return SCREEN_APP.get(index_widget)
    """
    with open(read_module_path,'r') as f:
        tmp_new_code = f.read()
        tmp_new_code = tmp_new_code.replace("'{", "{").replace("}'", "}")
        tmp_new_code = tmp_new_code.replace('Container_exemple', 'Container').replace('imagefit', 'image_fit').replace('imageopacity', 'image_opacity')
        tmp_new_code = tmp_new_code.replace('borderradius', 'border_radius').replace('imagesrc','image_src').replace('runspacing', 'run_spacing')
        tmp_new_code = tmp_new_code.replace('horizontalalignment', 'horizontal_alignment').replace('verticalalignment','vertical_alignment')
        tmp_new_code = tmp_new_code.replace("n='content'", '').replace('onclick','on_click').replace('Offstage()','None')


        if write_lines:
            with open(write_module_path,'w') as f:
                f.write(f"{import_module}\n\nSCREEN_APP = {tmp_new_code}\n\n{data}")

        if show:
            print(tmp_new_code)
            return tmp_new_code

def read_index_page_db(index=''):
    """ MOST BE TRASLATED TO INTEGRATE ALL SCREENS IN APP"""
    from .FLET_TRASLATED_SCREEN_DB import read_database_dict
    data_recived = read_database_dict(index_widget=index)
    return data_recived
