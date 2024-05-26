import os

def write_file(
               file_path:     str="",
               file_name:     str="",
               data_to_write: str=""
               ):
    """
    THIS LITE MODULE LET YOU DUMP ALL DATA IN CORRECT WAY

    write_file(file_path= "file_path", data_to_write= "data_to_writeL")
    """
    current_path: str = os.path.join(file_path,file_name) #: SET PATH AND FILE
    full_path = os.path.join(os.getcwd(),current_path)    #: SET ALL FULL PATH

    #: WRITE DATA IN TO APP
    with open(full_path,'w') as f:
       f.write(data_to_write)

    #: RUN ONLY IN PRODUCTION
    # print(current_path)
    # print(full_path)