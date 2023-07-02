"src" package
=============

.. toctree::
	:maxdepth: 2
	:caption: Contents:
	:hidden:

	mighty_logger-src-lib_types_collection-package

.. hint:: To use, you need to enter

	.. code-block:: python
		:linenos:

		from mighty_logger.src import ...

.. currentmodule:: mighty_logger.src.animations

.. rubric:: list IndefiniteAnimations
.. py:class:: IndefiniteAnimations

	The class with sets indefinite animations.

	:since: v0.6.0

	.. py:attribute:: Dots

		...

		:since: v0.6.0

	.. py:attribute:: Wave

		...

		:since: v0.6.0

	.. py:attribute:: WaveAutoReverse

		...

		:since: v0.6.0

	.. py:attribute:: Star

		...

		:since: v0.6.1

	.. py:attribute:: StarAutoReverse

		...

		:since: v0.6.1

	.. py:attribute:: StarHorizontalFill

		...

		:since: v0.6.1

	.. py:attribute:: StarHorizontalFillAutoReverse

		...

		:since: v0.6.1

	.. py:attribute:: Arrow

		...

		:since: v0.6.1

	.. py:attribute:: ArrowAutoReverse

		...

		:since: v0.6.1

	.. py:attribute:: Sunrise

		...

		:since: v0.6.1

	.. py:attribute:: Sunset

		...

		:since: v0.6.1

	.. py:attribute:: SunriseSunset

		...

		:since: v0.6.1

	.. py:attribute:: Clock1

		...

		:since: v0.6.0

	.. py:attribute:: Clock2

		...

		:since: v0.6.0

	.. py:attribute:: Clock3

		...

		:since: v0.6.0

	.. py:attribute:: Circle

		...

		:since: v0.6.0

	.. py:attribute:: KnightRider

		...

		:since: v0.6.0

	.. py:attribute:: KnightRiderAutoReverse

		...

		:since: v0.6.0

	.. py:attribute:: Blocks1

		...

		:since: v0.6.0

	.. py:attribute:: Blocks2

		...

		:since: v0.6.0

	.. py:attribute:: Blocks3

		...

		:since: v0.6.0

	.. py:attribute:: Blocks4

		...

		:since: v0.6.0

	.. py:attribute:: BlocksAutoReverse

		...

		:since: v0.6.0

	.. py:attribute:: Line

		...

		:since: v0.6.0

	.. py:attribute:: LineAutoReverse

		...

		:since: v0.6.0

	.. py:attribute:: BlockVerticalFill

		...

		:since: v0.6.0

	.. py:attribute:: BlockVerticalFillAutoReverse

		...

		:since: v0.6.0

	.. py:attribute:: BlockHorizontalFillAutoReverse

		...

		:since: v0.6.0

	.. py:attribute:: SuperSpace

		...

		:since: v0.6.1

.. rubric:: list DefiniteAnimations
.. py:class:: DefiniteAnimations

	The class with sets definite animations.

	:since: v0.6.0

	.. py:attribute:: Dots

		...

		:since: v0.6.0

	.. py:attribute:: Star

		...

		:since: v0.6.1

	.. py:attribute:: Arrow

		...

		:since: v0.6.1

	.. py:attribute:: KnightRider

		...

		:since: v0.6.0

	.. py:attribute:: Line

		...

		:since: v0.6.0

	.. py:attribute:: BlockVerticalFill

		...

		:since: v0.6.0

.. currentmodule:: mighty_logger.src.ansi_format

.. rubric:: data AnsiFormat
.. py:data:: AnsiFormat

	...

	:source: https://en.wikipedia.org/wiki/ANSI_escape_code
	:since: v0.2.0

.. rubric:: function _RecursiveGetAnsiFormat
.. py:function:: _RecursiveGetAnsiFormat(ansi_address: str, ansi: dict) -> str

	Recursively extracts a string with an ANSI escape code from a heavily nested dictionary.

	:since: v0.2.1
	:param ansi_address: Path to ANSI escape code value
	:type ansi_address: str
	:param ansi: External/nested dictionary
	:type ansi: dict
	:return: value - ANSI escape code
	:rtype: str

.. rubric:: function GetAnsiFormat
.. py:function:: GetAnsiFormat(ansi_address: str) -> str

	Returns the ANSI escape code value.

	The following values are possible: see the list inREADME.md/Data/"Tree of ANSI escape code".

	An example of getting an ANSI escape code:

	.. code-block:: python
		:linenos:

		print(f"{GetAnsiFormat('italic/fraktur')}Test string")
		print(f"{GetAnsiFormat('blink/slow')}Test string")
		print(f"{GetAnsiFormat('invert/off')}Test string")
		print(f"{GetAnsiFormat('font/3th alternative')}Test string")
		print(f"{GetAnsiFormat('color/foreground/green')}Test string")
		print(f"{GetAnsiFormat('color/set/background/255;255;255')}Test string")
		print(f"{GetAnsiFormat('reset/on')}Test string")

	:since: v0.2.1
	:param ansi_address: Path to ANSI escape code value
	:type ansi_address: str
	:return: ANSI escape code
	:rtype: str

.. currentmodule:: mighty_logger.src.color_picker

.. rubric:: data ColorPicker
.. py:data:: ColorPicker

	Color table

	:source: https://en.wikipedia.org/wiki/Web_colors
	:since: v0.0.4

.. rubric:: function DecColor
.. py:function:: DecColor(color_name: str) -> list[int, int, int]

	Returns a decimal color value.

	:since: v0.0.4
	:param color_name: Color name
	:type color_name: str
	:return: Decimal color value
	:rtype: list[int, int, int]
	:raises ColorException: This color is not in the dictionary

.. rubric:: function HexColor
.. py:function:: HexColor(color_name: str) -> str

	Returns a hexadecimal color value.

	:since: v0.0.4
	:param color_name: Color name
	:type color_name: str
	:return: Hexadecimal color value
	:rtype: str
	:raises ColorException: This color is not in the dictionary

.. rubric:: function AnsiColor
.. py:function:: AnsiColor(color_name: str, color_ground: str) -> str

	Returns an ANSI color value. In AnsiFormat, the following levels are available under the "color/set/..." path:

	- foreground
	- background
	- bright foreground
	- bright background
	- underline

	:since: v0.0.4
	:param color_name: Color name
	:type color_name: str
	:param color_ground: Color level
	:type color_ground: str
	:return: ANSI color value
	:rtype: str
	:raises ColorException: This color is not in the dictionary

.. rubric:: function Dec2Hex
.. py:function:: Dec2Hex(dec_colors: list[int, int, int]) -> str

	Converts a decimal color value to a hexadecimal.

	:since: v0.2.0
	:param dec_colors: Decimal color value
	:type dec_colors: list[int, int, int]
	:return: Hexadecimal color value
	:rtype: str

.. rubric:: function Dec2Ansi
.. py:function:: Dec2Ansi(dec_colors: list[int, int, int], color_ground: str) -> str

	Converts a decimal color value to an ANSI escape code.

	:since: v0.2.0
	:param dec_colors: Decimal color value
	:type dec_colors: list[int, int, int]
	:param color_ground: Color level (read AnsiColor() function documentation)
	:type color_ground: str
	:return: ANSI escape code color value
	:rtype: str

.. rubric:: function Hex2Dec
.. py:function:: Hex2Dec(hex_color: str) -> list[int, int, int]

	Converts a hexadecimal color value to a decimal.

	:since: v0.2.0
	:param hex_color: Hexadecimal color value
	:type hex_color: str
	:return: Decimal color value
	:rtype: list[int, int, int]

.. rubric:: function Hex2Ansi
.. py:function:: Hex2Ansi(hex_color: str, color_ground: str) -> str

	Converts a hexadecimal color value to an ANSI escape code.

	:since: v0.2.0
	:param hex_color: Hexadecimal color value
	:type hex_color: str
	:param color_ground: Color level (read AnsiColor() function documentation)
	:type color_ground: str
	:return: ANSI escape code color value
	:rtype: str

.. rubric:: function Ansi2Dec
.. py:function:: Ansi2Dec(ansi_color: str) -> list[int, int, int]

	Converts an ANSI escape code color value to a decimal. When converting to ANSI escape code, you need to know which level the color is applied to, and when from ANSI escape code, you don’t need to, because in other formats the levels are defined differently and are not included in the command along with the color.

	:since: v0.2.0
	:param ansi_color: ANSI escape code color value
	:type ansi_color: str
	:return: Decimal color value
	:rtype: list[int, int, int]

.. rubric:: function Ansi2Hex
.. py:function:: Ansi2Hex(ansi_color: str) -> str

	Converts an ANSI escape code color value to a hexadecimal. When converting to ANSI escape code, you need to know which level the color is applied to, and when from ANSI escape code, you don’t need to, because in other formats the levels are defined differently and are not included in the command along with the color.

	:since: v0.2.0
	:param ansi_color: ANSI escape code color value
	:type ansi_color: str
	:return: Hexadecimal color value
	:rtype: str
