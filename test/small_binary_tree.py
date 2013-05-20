

# "_1" = [

#         '_2',= ['_4']
#         '_3' = ['_7','_8']
#         ]

# '_5' = ['_6']

# ==========================

# "_1" = ['_2','_3']
#         |     | = ['_7','_8']
#         |
#         '_2' = ['_4']

# '_5' = ['_6']
# ==========================
# 1 control  = 2,3
# 3 controls = 7,8
# 2 content  = 4
# 5 content  = 6



# "_1" = ['_2','_3']
# '_3' = ['_7','_8']
# '_2' = ['_4']
# '_5' = ['_6']

binary_data = {
                '_1':{
                        '_2':{},
                        '_3':{},
                     },
                '_3':{
                        '_7':{},
                        '_8':{},
                    },
                '_2':{
                        '_4':{},
                    },
                '_5':{
                        '_6':{},
                    },
                }


# 1-2-4
# 1-3-8
# 5-6
# LAYER_1
layer_1_keys = binary_data.keys()
# print(layer_1_keys)


# print(binary_data)
print(layer_1_keys)


def check_data(data):

    if binary_data.get(data):
        return True
    else:
        return False

print(check_data(data='_1',))

