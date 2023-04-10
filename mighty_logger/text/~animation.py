# ##########################   Qt_Colored-logger   ########################### #
# ---------------------------------------------------------------------------- #
#                                                                              #
# Copyright © 2023 Kalynovsky Valentin. All rights reserved.                   #
#                                                                              #
# Licensed under the Apache License, Version 2.0 (the "License");              #
# you may not use this file except in compliance with the License.             #
# You may obtain a copy of the License at                                      #
#                                                                              #
#     http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS,            #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.     #
# See the License for the specific language governing permissions and          #
# limitations under the License.                                               #
#                                                                              #
# ---------------------------------------------------------------------------- #
# ############################################################################ #

# ATTENTION! It's just a vision for the future. This is not yet used functionality.
# Source: https://github.com/kopensource/colored_logs/blob/develop/colored_logs/models/animation_type.py

class AnimationType:
    Dots = ['.  ', '.. ', '...']
    Wave = [
        '⸳·⸳․․․․․',
        '․⸳·⸳․․․․',
        '․․⸳·⸳․․․',
        '․․․⸳·⸳․․',
        '․․․․⸳·⸳․',
        '․․․․․⸳·⸳',
        '⸳․․․․․⸳·',
        '·⸳․․․․․⸳'
    ]
    WaveAutoReverse = [
        '⸳·⸳․․․․․',
        '․⸳·⸳․․․․',
        '․․⸳·⸳․․․',
        '․․․⸳·⸳․․',
        '․․․․⸳·⸳․',
        '․․․․․⸳·⸳',
        '․․․․⸳·⸳․',
        '․․․⸳·⸳․․',
        '․․⸳·⸳․․․',
        '․⸳·⸳․․․․'
    ]
    Clock1 = ['⌏', '⌎', '⌌', '⌍']
    Clock2 = ['◴', '◷', '◶', '◵']
    Clock3 = ['◴   ', ' ◷  ', '  ◶ ', '   ◵', '  ◶ ', ' ◷  ']
    Circle = ['◜ ', ' ◝', ' ◞', '◟ ']
    KnightRider = ['▪▪▫▫▫▫▫', '▪▪▪▫▫▫▫', '▫▪▪▪▫▫▫', '▫▫▪▪▪▫▫', '▫▫▫▪▪▪▫', '▫▫▫▫▪▪▪', '▫▫▫▫▫▪▪']
    KnightRiderAutoReverse = [
        '▪▫▫▫▫▫▫', '▪▪▫▫▫▫▫', '▪▪▪▫▫▫▫', '▫▪▪▪▫▫▫', '▫▫▪▪▪▫▫', '▫▫▫▪▪▪▫', '▫▫▫▫▪▪▪', '▫▫▫▫▫▪▪',
        '▫▫▫▫▫▫▪', '▫▫▫▫▫▪▪', '▫▫▫▫▪▪▪', '▫▫▫▪▪▪▫', '▫▫▪▪▪▫▫', '▫▪▪▪▫▫▫', '▪▪▪▫▫▫▫', '▪▪▫▫▫▫▫'
    ]
    Blocks1 = ['▖', '▗', '▝', '▘']
    Blocks2 = ['▚', '▞']
    Blocks3 = ['▟', '▙', '▛', '▜']
    Blocks4 = ['▖', '▗', '▝', '▘', '▚', '▞', '▟', '▙', '▛', '▜', '█']
    BlocksAutoReverse = ['▖', '▗', '▝', '▘', '▚', '▞', '▟', '▙', '▛', '▜', '█', '▜', '▛', '▙', '▟', '▞', '▚', '▘', '▝', '▗']
    Line = ['▓▓▒▒▒▒▒▒', '▓▓▓▒▒▒▒▒', '▒▓▓▓▒▒▒▒', '▒▒▓▓▓▒▒▒', '▒▒▒▓▓▓▒▒', '▒▒▒▒▓▓▓▒', '▒▒▒▒▒▓▓▓', '▒▒▒▒▒▒▓▓', '▓▒▒▒▒▒▒▓']
    LineAutoReverse = [
        '▓▒▒▒▒▒▒▒', '▓▓▒▒▒▒▒▒', '▓▓▓▒▒▒▒▒', '▒▓▓▓▒▒▒▒', '▒▒▓▓▓▒▒▒', '▒▒▒▓▓▓▒▒', '▒▒▒▒▓▓▓▒', '▒▒▒▒▒▓▓▓', '▒▒▒▒▒▒▓▓',
        '▒▒▒▒▒▒▒▓', '▒▒▒▒▒▒▓▓', '▒▒▒▒▒▓▓▓', '▒▒▒▒▓▓▓▒', '▒▒▒▓▓▓▒▒', '▒▒▓▓▓▒▒▒', '▒▓▓▓▒▒▒▒', '▓▓▓▒▒▒▒▒', '▓▓▒▒▒▒▒▒'
    ]
    BlockVerticalFill = ['▁', '▂', '▃', '▅', '▆', '▇']
    BlockVerticalFillAutoReverse = [
        '▁', '▂', '▃', '▅', '▆',
        '▇', '▆', '▅', '▃', '▂'
    ]
    BlockHorizontalFillAutoReverse = [
        '▏', '▎', '▍', '▋', '▊',
        '▉', '▊', '▋', '▍', '▎'
    ]
