"""
A module with realisation of animations.
\n
The source of IndefiniteAnimation:
https://github.com/kopensource/colored_logs/blob/develop/colored_logs/models/animation_type.py
\n
Copyright © 2023 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class BasicAnimationType:
    """
    Basic wrapper class for animations type.
    """
    def __init__(self, animation: list):
        self.__animation: list = animation

    @property
    def animation(self) -> list:
        return self.__animation

class IndefiniteAnimationType(BasicAnimationType):
    """
    Wrapper class for indefinite animations type.
    """
    ...

class DefiniteAnimationType(BasicAnimationType):
    """
    Wrapper class for definite animations type.
    """
    ...

class IndefiniteAnimations:
    """
    The class with sets indefinite animations.
    """
    Dots = IndefiniteAnimationType(['.  ', '.. ', '...'])
    Wave = IndefiniteAnimationType([
        '⸳·⸳․․․․․',
        '․⸳·⸳․․․․',
        '․․⸳·⸳․․․',
        '․․․⸳·⸳․․',
        '․․․․⸳·⸳․',
        '․․․․․⸳·⸳',
        '⸳․․․․․⸳·',
        '·⸳․․․․․⸳'
    ])
    WaveAutoReverse = IndefiniteAnimationType([
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
    ])
    Clock1 = IndefiniteAnimationType(['⌏', '⌎', '⌌', '⌍'])
    Clock2 = IndefiniteAnimationType(['◴', '◷', '◶', '◵'])
    Clock3 = IndefiniteAnimationType(['◴   ', ' ◷  ', '  ◶ ', '   ◵', '  ◶ ', ' ◷  '])
    Circle = IndefiniteAnimationType(['◜ ', ' ◝', ' ◞', '◟ '])
    KnightRider = IndefiniteAnimationType(['▪▪▫▫▫▫▫', '▪▪▪▫▫▫▫', '▫▪▪▪▫▫▫', '▫▫▪▪▪▫▫', '▫▫▫▪▪▪▫', '▫▫▫▫▪▪▪', '▫▫▫▫▫▪▪'])
    KnightRiderAutoReverse = IndefiniteAnimationType([
        '▪▫▫▫▫▫▫', '▪▪▫▫▫▫▫', '▪▪▪▫▫▫▫', '▫▪▪▪▫▫▫', '▫▫▪▪▪▫▫', '▫▫▫▪▪▪▫', '▫▫▫▫▪▪▪', '▫▫▫▫▫▪▪',
        '▫▫▫▫▫▫▪', '▫▫▫▫▫▪▪', '▫▫▫▫▪▪▪', '▫▫▫▪▪▪▫', '▫▫▪▪▪▫▫', '▫▪▪▪▫▫▫', '▪▪▪▫▫▫▫', '▪▪▫▫▫▫▫'
    ])
    Blocks1 = IndefiniteAnimationType(['▖', '▗', '▝', '▘'])
    Blocks2 = IndefiniteAnimationType(['▚', '▞'])
    Blocks3 = IndefiniteAnimationType(['▟', '▙', '▛', '▜'])
    Blocks4 = IndefiniteAnimationType(['▖', '▗', '▝', '▘', '▚', '▞', '▟', '▙', '▛', '▜', '█'])
    BlocksAutoReverse = IndefiniteAnimationType(['▖', '▗', '▝', '▘', '▚', '▞', '▟', '▙', '▛', '▜', '█', '▜', '▛', '▙', '▟', '▞', '▚', '▘', '▝', '▗'])
    Line = IndefiniteAnimationType(['▓▓▒▒▒▒▒▒', '▓▓▓▒▒▒▒▒', '▒▓▓▓▒▒▒▒', '▒▒▓▓▓▒▒▒', '▒▒▒▓▓▓▒▒', '▒▒▒▒▓▓▓▒', '▒▒▒▒▒▓▓▓', '▒▒▒▒▒▒▓▓', '▓▒▒▒▒▒▒▓'])
    LineAutoReverse = IndefiniteAnimationType([
        '▓▒▒▒▒▒▒▒', '▓▓▒▒▒▒▒▒', '▓▓▓▒▒▒▒▒', '▒▓▓▓▒▒▒▒', '▒▒▓▓▓▒▒▒', '▒▒▒▓▓▓▒▒', '▒▒▒▒▓▓▓▒', '▒▒▒▒▒▓▓▓', '▒▒▒▒▒▒▓▓',
        '▒▒▒▒▒▒▒▓', '▒▒▒▒▒▒▓▓', '▒▒▒▒▒▓▓▓', '▒▒▒▒▓▓▓▒', '▒▒▒▓▓▓▒▒', '▒▒▓▓▓▒▒▒', '▒▓▓▓▒▒▒▒', '▓▓▓▒▒▒▒▒', '▓▓▒▒▒▒▒▒'
    ])
    BlockVerticalFill = IndefiniteAnimationType(['▁', '▂', '▃', '▅', '▆', '▇'])
    BlockVerticalFillAutoReverse = IndefiniteAnimationType([
        '▁', '▂', '▃', '▅', '▆',
        '▇', '▆', '▅', '▃', '▂'
    ])
    BlockHorizontalFillAutoReverse = IndefiniteAnimationType([
        '▏', '▎', '▍', '▋', '▊',
        '▉', '▊', '▋', '▍', '▎'
    ])

class DefiniteAnimations:
    """
    The class with sets definite animations.
    """
    Dots = DefiniteAnimationType(['        ', '.       ', '..      ', '...     ', '....    ', '.....   ', '......  ', '....... ', '........'])
    KnightRider = DefiniteAnimationType(['▫▫▫▫▫▫▫▫', '▪▫▫▫▫▫▫▫', '▪▪▫▫▫▫▫▫', '▪▪▪▫▫▫▫▫', '▪▪▪▪▫▫▫▫', '▪▪▪▪▪▫▫▫', '▪▪▪▪▪▪▫▫', '▪▪▪▪▪▪▪▫', '▪▪▪▪▪▪▪▪'])
    Line = DefiniteAnimationType(['▒▒▒▒▒▒▒▒', '▓▒▒▒▒▒▒▒', '▓▓▒▒▒▒▒▒', '▓▓▓▒▒▒▒▒', '▓▓▓▓▒▒▒▒', '▓▓▓▓▓▒▒▒', '▓▓▓▓▓▓▒▒', '▓▓▓▓▓▓▓▒', '▓▓▓▓▓▓▓▓'])
    BlockVerticalFill = DefiniteAnimationType(['        ', '▇       ', '▇▇      ', '▇▇▇     ', '▇▇▇▇    ', '▇▇▇▇▇   ', '▇▇▇▇▇▇  ', '▇▇▇▇▇▇▇ ', '▇▇▇▇▇▇▇▇'])
