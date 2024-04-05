########################
# from extra_utils.settings_var.settings_widget import global_var, get_global_var
########################
# global_var(data_global={'name_var':'global_var'})
######################## get from dict var
# get_global_var(get_var='var_to_get')
########################

selectWidgetBox= {
                    'selectWidgetBox':"None",
                    'numClick':1,
                    'numWidget':1,
                    'listWidgetUpdate':list(),
                    'text_widget_selected':'widget Text',
                    # 'page': 'is_defined'
                    # 'Icon_Browser': 'is_defined'
                    }

def global_var(data_global):
    global selectWidgetBox
    selectWidgetBox.update(data_global)
    # print('hello')
    return selectWidgetBox

def get_global_var(get_var=False):
    # print('hello')
    if get_var:
        tmp_selectWidgetBox  = selectWidgetBox.get(get_var)
        return tmp_selectWidgetBox
    else:
        return selectWidgetBox