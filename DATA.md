## Data
The library stores various important data for use that you may need to know while using the library.

###### Entry types:
- DEBUG
- DEBUG_PERFORMANCE
- PERFORMANCE
- EVENT
- AUDIT
- METRICS
- USER
- MESSAGE
- INFO
- NOTICE
- WARNING
- ERROR
- CRITICAL
- ~~PROGRESS~~ (*not implemented because the non-implemented START_PROCESS and STOP_PROCESS methods control this type*)
- SUCCESS
- FAIL

###### X11 color table:
- Red category:
    - MAROON
    - DARKRED
    - RED
    - LIGHTRED
    - FIREBRICK
    - CRIMSON
    - INDIANRED
    - LIGHTCORAL
    - SALMON
    - DARKSALMON
    - LIGHTSALMON
- Pink category:
    - MEDIUMVIOLETRED
    - DEEPPINK
    - PALEVIOLETRED
    - HOTPINK
    - LIGHTPINK
    - PINK
- Orange category:
    - ORANGERED
    - TOMATO
    - DARKORANGE
    - CORAL
    - ORANGE
- Yellow category:
    - DARKKHAKI
    - GOLD
    - KHAKI
    - PEACHPUFF
    - YELLOW
    - DARKYELLOW
    - PALEGOLDENROD
    - MOCCASIN
- Purple category:
    - INDIGO
    - PURPLE
    - DARKMAGENTA
    - DARKVIOLET
    - DARKSLATEBLUE
    - BLUEVIOLET
    - DARKORCHID
    - FUCHSIA
    - SLATEBLUE
    - MEDIUMSLATEBLUE
    - MEDIUMORCHID
    - MEDIUMPURPLE
    - ORCHID
    - VIOLET
    - PLUM
    - THISTLE
    - LAVENDER
- Green category:
    - DARKGREEN
    - GREEN
    - DARKOLIVEGREEN
    - FORESTGREEN
    - SEAGREEN
    - DARKSLATEGRAY
    - OLIVE
    - OLIVEDRAB
    - MEDIUMSEAGREEN
    - LIMEGREEN
    - LIME
    - SPRINGGREEN
    - MEDIUMSPRINGGREEN
    - DARKSEAGREEN
    - MEDIUMAQUAMARINE
    - YELLOWGREEN
    - LAWNGREEN
    - CHARTREUSE
    - LIGHTGREEN
    - GREENYELLOW
    - PALEGREEN
- Aqua category:
    - TEAL
    - DARKCYAN
    - LIGHTSEAGREEN
    - CADETBLUE
    - DARKTURQUOISE
    - MEDIUMTURQUOISE
    - TURQUOISE
    - AQUA
    - AQUAMARINE
    - SKYBLUE
    - LIGHTSKYBLUE
    - LIGHTSTEELBLUE
    - LIGHTBLUE
    - POWDERBLUE
    - PALETURQUOISE
- Blue category:
    - MIDNIGHTBLUE
    - NAVY
    - DARKBLUE
    - MEDIUMBLUE
    - BLUE
    - ROYALBLUE
    - STEELBLUE
    - DODGERBLUE
    - DEEPSKYBLUE
    - CORNFLOWERBLUE
- Brown category:
    - BROWN
    - SADDLEBROWN
    - SIENNA
    - CHOCOLATE
    - DARKGOLDENROD
    - PERU
    - ROSYBROWN
    - GOLDENROD
    - SANDYBROWN
    - TAN
    - BURLYWOOD
    - WHEAT
    - NAVAJOWHITE
    - BISQUE
    - BLANCHEDALMOND
- White category:
    - WHITE
    - SNOW
    - HONEYDEW
    - MINTCREAM
    - AZURE
    - LIGHTCYAN
    - ALICEBLUE
    - GHOSTWHITE
    - WHITESMOKE
    - SEASHELL
    - BEIGE
    - OLDLACE
    - FLORALWHITE
    - IVORY
    - ANTIQUEWHITE
    - LINEN
    - LAVENDERBLUSH
    - MISTYROSE
    - PAPAYAWHIP
    - LIGHTGOLDENRODYELLOW
    - CORNSILK
    - LEMONCHIFFON
    - LIGHTYELLOW
- Gray and black category:
    - BLACK
    - DARKGRAY
    - DIMGRAY
    - SLATEGRAY
    - GRAY
    - LIGHTSLATEGRAY
    - SILVER
    - LIGHTGRAY
    - GAINSBORO

###### Logger Color Chart:
| Color name                        | Foreground color  | Background color |
|-----------------------------------|-------------------|------------------|
| INITIAL_COLOR                     | GOLD              | INDIGO           |
| INITIAL_BACKGROUND                | -                 | GOLD             |
| DEBUG_TIME                        | ORCHID            | DARKMAGENTA      |
| DEBUG_STATUS                      | ORANGE            | DARKRED          |
| DEBUG_STATUS_MESSAGE              | DARKORANGE        | MAROON           |
| TYPE_DEBUG                        | BURLYWOOD         | NAVY             |
| DEBUG_MESSAGE                     | TAN               | MIDNIGHTBLUE     |
| DEBUG_BACKGROUND                  | -                 | TAN              |
| DEBUG_PERFORMANCE_TIME            | ORCHID            | DARKMAGENTA      |
| DEBUG_PERFORMANCE_STATUS          | ORANGE            | DARKRED          |
| DEBUG_PERFORMANCE_STATUS_MESSAGE  | DARKORANGE        | MAROON           |
| TYPE_DEBUG_PERFORMANCE            | NAVAJOWHITE       | NAVY             |
| DEBUG_PERFORMANCE_MESSAGE         | WHEAT             | MIDNIGHTBLUE     |
| DEBUG_PERFORMANCE_BACKGROUND      | -                 | WHEAT            |
| PERFORMANCE_TIME                  | ORCHID            | DARKMAGENTA      |
| PERFORMANCE_STATUS                | ORANGE            | DARKRED          |
| PERFORMANCE_STATUS_MESSAGE        | DARKORANGE        | MAROON           |
| TYPE_PERFORMANCE                  | BLANCHEDALMOND    | NAVY             |
| PERFORMANCE_MESSAGE               | BISQUE            | MIDNIGHTBLUE     |
| PERFORMANCE_BACKGROUND            | -                 | BISQUE           |
| EVENT_TIME                        | ORCHID            | DARKMAGENTA      |
| EVENT_STATUS                      | ORANGE            | DARKRED          |
| EVENT_STATUS_MESSAGE              | DARKORANGE        | MAROON           |
| TYPE_EVENT                        | GREENYELLOW       | NAVY             |
| EVENT_MESSAGE                     | YELLOWGREEN       | MIDNIGHTBLUE     |
| EVENT_BACKGROUND                  | -                 | YELLOWGREEN      |
| AUDIT_TIME                        | ORCHID            | DARKMAGENTA      |
| AUDIT_STATUS                      | ORANGE            | DARKRED          |
| AUDIT_STATUS_MESSAGE              | DARKORANGE        | MAROON           |
| TYPE_AUDIT                        | MEDIUMSPRINGGREEN | NAVY             |
| AUDIT_MESSAGE                     | SPRINGGREEN       | MIDNIGHTBLUE     |
| AUDIT_BACKGROUND                  | -                 | SPRINGGREEN      |
| METRICS_TIME                      | ORCHID            | DARKMAGENTA      |
| METRICS_STATUS                    | ORANGE            | DARKRED          |
| METRICS_STATUS_MESSAGE            | DARKORANGE        | MAROON           |
| TYPE_METRICS                      | PALEGREEN         | NAVY             |
| METRICS_MESSAGE                   | LIGHTGREEN        | MIDNIGHTBLUE     |
| METRICS_BACKGROUND                | -                 | LIGHTGREEN       |
| USER_TIME                         | ORCHID            | DARKMAGENTA      |
| USER_STATUS                       | ORANGE            | DARKRED          |
| USER_STATUS_MESSAGE               | DARKORANGE        | MAROON           |
| TYPE_USER                         | CHARTREUSE        | NAVY             |
| USER_MESSAGE                      | LAWNGREEN         | MIDNIGHTBLUE     |
| USER_BACKGROUND                   | -                 | LAWNGREEN        |
| MESSAGE_TIME                      | ORCHID            | DARKMAGENTA      |
| MESSAGE_STATUS                    | ORANGE            | DARKRED          |
| MESSAGE_STATUS_MESSAGE            | DARKORANGE        | MAROON           |
| TYPE_MESSAGE                      | PALETURQUOISE     | NAVY             |
| MESSAGE_MESSAGE                   | POWDERBLUE        | MIDNIGHTBLUE     |
| MESSAGE_BACKGROUND                | -                 | POWDERBLUE       |
| INFO_TIME                         | ORCHID            | DARKMAGENTA      |
| INFO_STATUS                       | ORANGE            | DARKRED          |
| INFO_STATUS_MESSAGE               | DARKORANGE        | MAROON           |
| TYPE_INFO                         | LIGHTSKYBLUE      | NAVY             |
| INFO_MESSAGE                      | SKYBLUE           | MIDNIGHTBLUE     |
| INFO_BACKGROUND                   | -                 | SKYBLUE          |
| NOTICE_TIME                       | ORCHID            | DARKMAGENTA      |
| NOTICE_STATUS                     | ORANGE            | DARKRED          |
| NOTICE_STATUS_MESSAGE             | DARKORANGE        | MAROON           |
| TYPE_NOTICE                       | LIGHTBLUE         | NAVY             |
| NOTICE_MESSAGE                    | LIGHTSTEELBLUE    | MIDNIGHTBLUE     |
| NOTICE_BACKGROUND                 | -                 | LIGHTSTEELBLUE   |
| WARNING_TIME                      | ORCHID            | DARKMAGENTA      |
| WARNING_STATUS                    | ORANGE            | DARKRED          |
| WARNING_STATUS_MESSAGE            | DARKORANGE        | MAROON           |
| TYPE_WARNING                      | YELLOW            | NAVY             |
| WARNING_MESSAGE                   | DARKYELLOW        | MIDNIGHTBLUE     |
| WARNING_BACKGROUND                | -                 | DARKYELLOW       |
| ERROR_TIME                        | ORCHID            | PLUM             |
| ERROR_STATUS                      | ORANGE            | ORANGE           |
| ERROR_STATUS_MESSAGE              | DARKORANGE        | DARKORANGE       |
| TYPE_ERROR                        | FIREBRICK         | GAINSBORO        |
| ERROR_MESSAGE                     | DARKRED           | LIGHTGRAY        |
| ERROR_BACKGROUND                  | -                 | DARKRED          |
| CRITICAL_TIME                     | ORCHID            | PLUM             |
| CRITICAL_STATUS                   | ORANGE            | ORANGE           |
| CRITICAL_STATUS_MESSAGE           | DARKORANGE        | DARKORANGE       |
| TYPE_CRITICAL                     | FIREBRICK         | DARKSALMON       |
| CRITICAL_MESSAGE                  | DARKRED           | LIGHTSALMON      |
| CRITICAL_BACKGROUND               | -                 | MAROON           |
| PROGRESS_TIME                     | ORCHID            | PURPLE           |
| PROGRESS_STATUS                   | ORANGE            | DARKRED          |
| PROGRESS_STATUS_MESSAGE           | DARKORANGE        | MAROON           |
| TYPE_PROGRESS                     | LIGHTSKYBLUE      | NAVY             |
| PROGRESS_MESSAGE                  | SKYBLUE           | MIDNIGHTBLUE     |
| PROGRESS_BACKGROUND               | -                 | SKYBLUE          |
| SUCCESS_TIME                      | ORCHID            | LAVENDERBLUSH    |
| SUCCESS_STATUS                    | ORANGE            | CHARTREUSE       |
| SUCCESS_STATUS_MESSAGE            | DARKORANGE        | LAWNGREEN        |
| TYPE_SUCCESS                      | GREEN             | PALEGREEN        |
| SUCCESS_MESSAGE                   | DARKGREEN         | LIGHTGREEN       |
| SUCCESS_BACKGROUND                | -                 | DARKGREEN        |
| FAIL_TIME                         | ORCHID            | LAVENDERBLUSH    |
| FAIL_STATUS                       | ORANGE            | ORANGE           |
| FAIL_STATUS_MESSAGE               | DARKORANGE        | DARKORANGE       |
| TYPE_FAIL                         | FIREBRICK         | YELLOW           |
| FAIL_MESSAGE                      | DARKRED           | DARKYELLOW       |
| FAIL_BACKGROUND                   | -                 | DARKRED          |

###### Tree of ANSI escape code:
- reset
    - on
- bold
    - on
    - off (doubly underlined)
- faint
    - on
    - off
- italic
    - on
    - fraktur
    - off
- underline
    - on
    - off
- blink
    - slow
    - rapid
    - off
- proportional spacing
    - on
    - off
- invert
    - on
    - off
- hide
    - on
    - off
- strike
    - on
    - off
- over line
    - on
    - off
- framed
    - on
    - encircled
    - off
- font
    - primary
    - 1st alternative
    - 2nd alternative
    - 3rd alternative
    - 4th alternative
    - 5th alternative
    - 6th alternative
    - 7th alternative
    - 8th alternative
    - 9th alternative
- color
    - foreground
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - background
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - bright foreground
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - bright background
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - set
        - foreground
            - R;G;B
        - background
            - R;G;B
        - bright foreground
            - R;G;B
        - bright background
            - R;G;B
        - underline
            - R;G;B
    - default
        - foreground
        - background
        - bright foreground
        - bright background
        - underline
