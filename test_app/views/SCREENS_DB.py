from flet import *


SCREEN_APP = {'_1': View(scroll='auto', vertical_alignment='center', horizontal_alignment='center', spacing=8, padding='8'),
'_2': Container(bgcolor='#44CCCC00', ink=True, margin={"l":8,"t":8,"r":8,"b":8}, padding={"l":8,"t":8,"r":8,"b":8}, alignment={"x":0,"y":0}),
'_3': Container(),
'_4': Container(expand=1, tooltip='Container', width=320, height=320, bgcolor='#3f449a', image_src='/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg', image_fit='COVER', image_opacity=0.1, ink=False, border_radius={"bl":30,"br":30,"tl":30,"tr":30}, border={"l":{"w":2,"c":"black"},"t":{"w":2,"c":"black"},"r":{"w":2,"c":"black"},"b":{"w":2,"c":"black"}}, margin={"l":8,"t":8,"r":8,"b":8}, padding={"l":8,"t":8,"r":8,"b":8}, alignment={"x":0,"y":0}, gradient={"colors":["blue","yellow"],"tile_mode":"clamp","begin":{"x":0,"y":-1},"end":{"x":0,"y":1},"type":"linear"}),
'_5': Column(scroll='auto', horizontal_alignment='center', alignment='spaceAround', spacing=8, tight=True, wrap=True, run_spacing=8, ),
'_6': Container(tooltip='Container', width=150, height=70, bgcolor='red', image_src='/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg', image_fit='COVER', image_opacity=0.1, ink=False, on_click=True, border_radius={"bl":30,"br":30,"tl":30,"tr":30}, border={"l":{"w":2,"c":"black"},"t":{"w":2,"c":"black"},"r":{"w":2,"c":"black"},"b":{"w":2,"c":"black"}}, margin={"l":8,"t":8,"r":8,"b":8}, padding={"l":8,"t":8,"r":8,"b":8}, alignment={"x":0,"y":0}, gradient={"colors":["blue","yellow"],"tile_mode":"clamp","begin":{"x":0,"y":-1},"end":{"x":0,"y":1},"type":"linear"}),
'_7': ElevatedButton(tooltip='buttom', text='press container', ),
'_8': Container(tooltip='Container', width=150, height=30, bgcolor='#44CCCC00', image_src='/icons/icon-512.png', ink=False, on_click=True, border_radius={"bl":30,"br":30,"tl":30,"tr":30}, border={"l":{"w":2,"c":"black"},"t":{"w":2,"c":"black"},"r":{"w":2,"c":"black"},"b":{"w":2,"c":"black"}}, margin={"l":8,"t":8,"r":8,"b":8}, padding={"l":8,"t":8,"r":8,"b":8}, alignment={"x":0,"y":0}, gradient={"colors":["yellow","blue"],"tile_mode":"clamp","center":{"x":0,"y":0},"radius":0.5,"focal_radius":0.0,"type":"radial"}),
'_9': ElevatedButton(tooltip='buttom', text='press container', ),
'_10': ElevatedButton(tooltip='buttom', text='WRITE'),
'_11': ElevatedButton(tooltip='buttom', text='DELETE'),
'_12': None}