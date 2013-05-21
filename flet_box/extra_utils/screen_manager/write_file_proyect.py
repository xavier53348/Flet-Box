import os


def file_saved(full_path: str = '', data_code: str=''):
    with open(full_path , 'w') as f:
        f.write(data_code)

def dump_data_file(
                     file_name:str = "",
                  screen_dump: str = "",
                   style_dump: str = "",
                   event_dump: str = "",
                 path_to_dump: str = "",
                   ):

    #: CREATE STYLE AND SCREN APTH
    full_screen_path = os.path.join(path_to_dump,f"{file_name}.py")
    full_styles_path = os.path.join(path_to_dump,f"{file_name}_styles.py")
    full_events_path = os.path.join(path_to_dump,f"{file_name}_events.py")

    #: SCREEN_NAME
    file_saved(
               full_path = full_screen_path,
               data_code = screen_dump,
               )

    #: STYLE_NAME
    file_saved(
               full_path = full_styles_path,
               data_code = style_dump,
               )

    #: PATH_NAME
    file_saved(
               full_path = full_events_path,
               data_code = event_dump,
               )

def write_file(
               path_name:  str="",
               file_name:  str="",

               main_code:  str="",
               style_code: str="",
               event_code: str="",
               ):

    """
    THIS LITE MODULE LET YOU DUMP ALL DATA IN CORRECT WAY

    write_file(file_path= "file_path", data_to_write= "data_to_writeL")
    """
    #: CREATE PATH
    path_screens_styles_events    = os.path.join(path_name,'views')
    path_event_and_screen_manager = path_name

    #: CODES TO WRITE
    main_code  = main_code.replace('CustomPage', file_name).replace('SYTLE_RENAME', file_name).replace('EVENT_RENAME', file_name)
    style_code = style_code
    event_code = event_code.replace(': #', f": # ID: {file_name},")

    #: WRITE DATA
    dump_data_file(
                    file_name    = file_name,
                    screen_dump  = main_code,
                    style_dump   = style_code,
                    event_dump   = event_code,

                    path_to_dump = path_screens_styles_events,
                    )



