# Copyright (c) 2018-2019 Arizona Board of Regents
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class FigText(object):
	"""Helper to set the main foreground color and text size.

	Also provides a method to prepare text to be analysed by LaTeX or mathtext.
	"""

	def __init__( self, size = None, color = None, fontproperties = None, tex = False ):
		self.size = size
		self.color = color
		self.fontproperties = fontproperties
		self.tex = tex

	def get_size( self ):
		"""Retrieve the default font size of the text items."""
		return self.size

	def set_size( self, size ):
		"""Set the default font size of the text items."""
		self.size = size

	def get_color( self ):
		"""Retrieve the default color of the text items."""
		return self.color

	def set_color( self, color ):
		"""Set the default color of the text items."""
		self.color = color

	def get_fontproperties( self ):
		"""Retrieve the default FontProperties object."""
		return self.fontproperties

	def set_fontproperties( self, fontproperties ):
		"""Set the default FontProperties object for text elements."""
		self.fontproperties = fontproperties

	def set_tex( self, tex ):
		"""Set whether the text should be analysed through LaTeX."""
		self.tex = tex

	def conv( self, text, math = True, tex = None ):
		"""Add needed escaping sequences to run the text through LaTeX (or mathtext) processor.

		Parameters
		----------
		text : The text to transform
		math : Flag that indicates whether the text contains mathematical notation

		Returns
		-------
		str
			The transformed text.
		"""

		if tex is None:
			tex = self.tex

		if tex:
			if math:
				return "$\\mathrm{" + text.replace( " ", "~" ) + "}$"
			else:
				return text.replace( "_", "\\_" ).replace( "^", "\\^" ).replace( "<", "$<$" ).replace( ">", "$>$" )
		elif math and ( "^" in text or "_" in text or "\\" in text ):
			return "$\\mathdefault{" + text.replace( " ", "\\ " ) + "}$"
		else:
			return text

	def get_text_args( self, color = None, size = None, tex = None ):
		"""Prepare additional arguments to a call that sets text.

		Parameters
		----------
		color : Override for the text's color
		size : Override for the text's size

		Returns
		-------
		dict
			Arguments that can be passed to various matplotlib calls that set text.
		"""
		if tex is None:
			ret = { "usetex": self.tex }
		else:
			ret = { "usetex": tex }

		if not color is None:
			ret[ "color" ] = color
		elif not self.color is None:
			ret[ "color" ] = self.color

		if self.fontproperties is None:
			if not size is None:
				ret[ "fontsize" ] = size
			elif not self.size is None:
				ret[ "fontsize" ] = self.size
		else:
			ret[ "fontproperties" ] = self.fontproperties.copy()

			if not size is None:
				ret[ "fontproperties" ].set_size( size )

		return ret

	def set_axes( self, ax, color = None, size = None ):
		"""Update the properties of a Axes object.

		Parameters
		----------
		ax : matplotlib.axes.Axes object
			Axes object to work on.
		color : Override for the text's color
		size : Override for the text's size
		"""
		ax.set_facecolor( "none" )

		ax.tick_params( axis = "both", which = "both", color = self.color if color is None else color )

		for key in ax.spines:
			ax.spines[ key ].set_color( self.color if color is None else color )

		for t in ax.get_xticklabels() + ax.get_yticklabels():
			self.set_text( t, color = color, size = size )

	def set_cbar( self, cbar, color = None, size = None ):
		"""Update the properties of a Colobar object.

		Parameters
		----------
		cbar : matplotlib.colorbar.Colobar object
			Colobar object to work on.
		color : Override for the text's color
		size : Override for the text's size
		"""
		self.set_axes( cbar.ax, color = color, size = size )
		cbar.outline.set_edgecolor( self.color if color is None else color )

	def set_legend( self, legend, color = None, size = None ):
		"""Update the properties of a Legend object.

		Parameters
		----------
		legend : matplotlib.legend.Legend object
			Legend object to work on.
		color : Override for the text's color
		size : Override for the text's size
		"""
		for t in legend.get_texts():
			self.set_text( t, color = color, size = size )

	def set_text( self, text, color = None, size = None ):
		"""Update the properties of a Text object.

		Parameters
		----------
		text : matplotlib.text.Text object
			Text object to work on.
		color : Override for the text's color
		size : Override for the text's size
		"""
		text.set_usetex( self.tex )
		text.set_color( self.color if color is None else color )
		if self.fontproperties is None:
			text.set_fontsize( self.size if size is None else size )
		else:
			if size is None:
				text.set_fontproperties( self.fontproperties )
			else:
				fp = self.fontproperties.copy()
				fp.set_size( size )
				text.set_fontproperties( fp )
