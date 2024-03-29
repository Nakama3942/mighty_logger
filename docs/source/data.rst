Data
====

The library stores various important data for use that you may need to know while using the library.

.. contents::
	:class: this-will-duplicate-information-and-it-is-still-useful-here

Environments
------------

- CONSOLE
- PLAIN_CONSOLE
- HTML
- MARKDOWN
- PLAIN

.. _settings:

Settings
--------

- Global:
	- global_bold_font
	- global_italic_font
	- global_invert_font (used in CONSOLE and PLAIN_CONSOLE)
	- global_background
- Local:
	- bold
	- italic
	- invert (used in CONSOLE and PLAIN_CONSOLE)
	- background

.. _entry_categories_and_types:

Entry categories and types
--------------------------

- No category
	- empty (v0.6.0)
- Logger debug (%):
	- debug
	- debug_performance
	- performance
- Logger event (~):
	- event
	- audit
	- metrics
	- user
- Logger message (@):
	- message
	- info
	- notice
- Logger error (!):
	- warning
	- error
	- critical
	- resolved (v0.6.0)
	- unresolved (v0.6.0)
- Process (&):
	- initiation (v0.6.0)
	- process (v0.6.0)
	- achievement (v0.6.0)
	- milestone (v0.6.0)
	- success
	- fail
- Timer (^):
	- start_timer (v0.6.1)
	- timer_mark (v0.6.1)
	- stop_timer (v0.6.1)
- Additional (/):
	- hint (v1.0.0)
	- tip (v1.0.0)
	- important (v1.0.0)
	- attention (v1.0.0)
	- caution (v1.0.0)
	- danger (v1.0.0)

Symbol meanings
---------------

- ``?`` - entry
- ``$`` - initial string
- ``*`` - time
- ``#`` - status
- ``%`` - category: Logger debug
- ``~`` - category: Logger event
- ``@`` - category: Logger message
- ``!`` - category: Logger error
- ``&`` - category: Process
- ``^`` - category: Timer
- ``/`` - category: Additional

Icon sets
---------

.. table:: Icon sets

	================= =========== =========== =========== ===========
	Type                #1          #2          #3          #4
	================= =========== =========== =========== ===========
	debug               🐛          🐞          🚧          🔬
	debug_performance   ⏱️          ⌛️           🔍          📈
	performance         ⏱️          🚀          📊          ⚡️
	event               🔔          🎉          📣          🚨
	audit               🔍          🔒          📋          🔐
	metrics             📊          📈          📉          📄
	user                👤          👥          🙋‍♂️          🙋‍♀️
	message             💬          📝          🗒️          📨
	info                ℹ️          🔍          📌          🔔
	notice              📌          📎           🔖          🚩
	warning             ⚠️          ⚡️          ⛔️          ⚠️
	error               ❌          🚫          💔          🔺
	critical            🔥          🚨           ⛔️          🚒
	resolved            ✅          ❗            🟦          🟢
	unresolved          ❎          ❓           🟥          🔴
	initiation          🚀          🚀          🔥          🔧
	process             ⏳          🔄          ⚙️          🕰️
	achievement         🏆          🏆          🌟          🎖️
	milestone           🔖          🔖          🎯          🗺️
	success             ✔️          🎉          👍          ✅
	fail                ❌          🚫          👎          ❎
	start_timer         ⏰          🕑          🟩          ⏳
	timer_mark          ⌚          🕕          🟨          ⏱️
	stop_timer          ⏲️          🕙          🟪          ⌛
	hint                🔍          🔎          🕵️          🔬
	tip                 💡           🌟          🎯          🔔
	important           ❗️            ‼️          ⚠️          🚨
	attention           ⚡️          ⛔️          ⏰          🛑
	caution             ⚠️          ⚡️          ⚙️          🚧
	danger              🔥          💣          ☠️          ⚡️
	================= =========== =========== =========== ===========

Sort keys
---------

- SORT_ON_TIME
- SORT_ON_TIME_WITH_REVERSE
- SORT_ON_CATEGORY
- SORT_ON_TYPE

Animations
----------

- Indefinite Animations
	- Dots
	- Wave
	- WaveAutoReverse
	- Star (v0.6.1)
	- StarAutoReverse (v0.6.1)
	- StarHorizontalFill (v0.6.1)
	- StarHorizontalFillAutoReverse (v0.6.1)
	- Arrow (v0.6.1)
	- ArrowAutoReverse (v0.6.1)
	- Sunrise (v0.6.1)
	- Sunset (v0.6.1)
	- SunriseSunset (v0.6.1)
	- Clock1
	- Clock2
	- Clock3
	- Circle
	- KnightRider
	- KnightRiderAutoReverse
	- Blocks1
	- Blocks2
	- Blocks3
	- Blocks4
	- BlocksAutoReverse
	- Line
	- LineAutoReverse
	- BlockVerticalFill
	- BlockVerticalFillAutoReverse
	- BlockHorizontalFillAutoReverse
	- SuperSpace (v0.6.1)
- Definite Animations
	- Dots
	- Star (v0.6.1)
	- Arrow (v0.6.1)
	- KnightRider
	- Line
	- BlockVerticalFill

.. _ansi:

Tree of ANSI escape code
------------------------

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

X11 color table
---------------

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
