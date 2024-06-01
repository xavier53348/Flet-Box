

def create_nested_dict(data_1:str="",data_2:str="",value: str="",nested_dict: dict={}):
    """
    HOW TO USE NESTED DICT ONLY 2 DIMENTION DICT:

    from path_module import create_nested_dict

    #: INSERT FIRST DATA
    create_nested_dict(
                       data_1      = 'screen_1',
                       data_2      = 'widget_1',
                       value       = "Container",
                       nested_dict = personal_dict,
                       )
    #: UPDATE FIRST DATA
    create_nested_dict(
                       data_1      = 'screen_1',
                       data_2      = 'widget_2',
                       value       = "Text",
                       nested_dict = personal_dict,

                       )
    #: CREATE NEW DATA IN FIRST DATA
    create_nested_dict(
                       data_1      = 'screen_2',
                       data_2      = 'widget_3',
                       value       = "Row",
                       nested_dict = personal_dict,
                       )
    """
    if not data_2:
        nested_dict.update({data_1:value})
    else:
        # print(nested_dict.get(data_1))

        if nested_dict.get(data_1) == None:
            #: IF NO EXIST KEY IN DICT CREATE A EMPTY DICT AND INSERT FIRST VALUE
            nested_dict[data_1]={}
            nested_dict[data_1].update({data_2:value})

            #: RUN ONLY IN PRODUCTION
            # print(nested_dict)

        else:
            #: IF EXIST KEY IN DICT UPDATE REST OF VALUES
            new_dict = nested_dict.get(data_1)
            # new_dict = nested_dict.get(data_1)
            new_dict.update({data_2:value})

            #: RUN ONLY IN PRODUCTION
            # print(new_dict,'he')




if __name__ == '__main__':
    personal_dict: dict={}

    #: INSERT FIRST DATA
    create_nested_dict(
                       data_1      = 'screen_1',
                       data_2      = 'widget_1',
                       value       = "Container",
                       nested_dict = personal_dict,
                       )
    #: UPDATE FIRST DATA
    create_nested_dict(
                       data_1      = 'screen_1',
                       data_2      = 'widget_2',
                       value       = "Text",
                       nested_dict = personal_dict,

                       )
    #: CREATE NEW DATA IN FIRST DATA
    create_nested_dict(
                       data_1      = 'screen_2',
                       data_2      = 'widget_3',
                       value       = "Row",
                       nested_dict = personal_dict,
                       )

    print(f"current_dict = {personal_dict}")