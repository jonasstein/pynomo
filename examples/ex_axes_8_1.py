# ex_axes_8_1.py

import sys
from pynomo.nomo_wrapper import *
from pynomo.nomographer import *

N_params = {'u_min': 0.0,
            'u_max': 300.0,
            'function_x': lambda u: 3 * sin(u / 180.0 * pi),
            'function_y': lambda u: 3 * cos(u / 180.0 * pi),
            'title': 'u',
            'tick_levels': 3,
            'tick_text_levels': 1,
            'title_x_shift': -0.5,
            'grid_length_0': 0.8/4,
            'grid_length_1': 0.6/4,
            'grid_length_2': 0.5/4,
            'grid_length_3': 0.4/4,
            'grid_length_4': 0.3/4,
            'text_size_0': text.size.tiny,
            'text_size_1': text.size.tiny,
            'text_size_2': text.size.tiny,
            'text_size_3': text.size.tiny,
            'text_size_4': text.size.tiny,
            'text_distance_0': 1.2/4,
            'text_distance_1': 1.1/4,
            'text_distance_2': 1.0/4,
            'text_distance_3': 1.0/4,
            'text_distance_4': 1.0/4,
            'title_distance_center': 0.7,
            'title_opposite_tick': True,
            'title_draw_center': True,
            'text_format': "$%3.1f$",
            'full_angle': True,
            'extra_angle': 90.0,
            'text_horizontal_align_center': True,
            'text_format': r"$%2.0f$",
            'text_color': color.cmyk.Sepia,
            }
block_params = {'block_type': 'type_8',
                'f_params': N_params,
                'width': 5.0,
                'height': 15.0,
                }
main_params = {'filename': 'ex_axes_8_1.pdf',
               'paper_height': 10.0,
               'paper_width': 10.0,
               'block_params': [block_params],
               'transformations': [('scale paper',)]
               }
Nomographer(main_params)
