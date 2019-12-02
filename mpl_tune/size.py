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


class FigSize(object):
	"""Helper to compute the size of matplotlib figures.

	The idea is to perform conversion between absolute margin sizes (and spacing between rows and columns
	in case of multiple subplots) and their corresponding relative that are needed for matplotlib.

	Additionnally, there is the possibility to reserve room on a plot to add a color bar.
	"""

	SIZE_ALL = 1
	SIZE_NO_CBAR = 2
	SIZE_AXES = 3
	SIZE_AX = 4
	SIZE_RATIO_AX = 5

	def __init__( self, size_h = None, size_v = None, nrows = 1, ncols = 1, margin_left = None, margin_bottom = None, margin_right = None, margin_top = None ):
		self.size_h = size_h
		self.type_h = self.SIZE_ALL
		self.size_v = size_v
		self.type_v = self.SIZE_ALL
		self.nrows = nrows
		self.ncols = ncols
		self.margin_left = margin_left
		self.margin_bottom = margin_bottom
		self.margin_right = margin_right
		self.margin_top = margin_top
		self.spacing_h = None
		self.spacing_v = None
		self.cbar_loc = None
		self.cbar_width = None
		self.cbar_pad = None

	def set_size_h( self, size_h, type_h = None ):
		"""Set the horizontal size of the figure.

		Parameters
		----------
		size_h : float
			Horizontal size of the figure in inches, the meaning depends on the value of parameter `type_h`.

		type_h : int
			Mode for the horizontal size, one of the SIZE_* constants.
			- SIZE_ALL: `size_h` is the total size of the figure, including margins and color bar (default)
			- SIZE_NO_CBAR: `size_h` is the size of the figure, without the potential color bar
			- SIZE_AXES: `size_h` is the size of the axis region of the figure, without the margins and the potential color bar.
			- SIZE_AX: `size_h` is the size of one of the axis.
			- SIZE_RATIO_AX: `size_h` is the ratio of the vertical size of the axis region.
		"""
		self.size_h = size_h
		if not type_h is None:
			self.type_h = type_h

	def set_size_v( self, size_v, type_v = None ):
		"""Set the vertical size of the figure.

		Parameters
		----------
		size_v : float
			Vertical size of the figure, the meaning depends on the value of parameter `type_v`.

		type_v : int
			Mode for the vertical size, one of the SIZE_* constants.
			- SIZE_ALL: `size_v` is the total size of the figure, including margins and color bar (default)
			- SIZE_NO_CBAR: `size_v` is the size of the figure, without the potential color bar
			- SIZE_AXES: `size_v` is the size of the axis region of the figure, without the margins and the potential color bar.
			- SIZE_AX: `size_v` is the size of one of the axis.
			- SIZE_RATIO_AX: `size_v` is the ratio of the horizontal size of the axis region.
		"""
		self.size_v = size_v
		if not type_v is None:
			self.type_v = type_v

	def set_nrows( self, nrows ):
		"""Set the number of rows of subplots that will be inserted in the figure

		This is used to compute the vertical spacing between the rows.

		Parameters
		----------
		nrows : int
			Number of rows of subplots that will be inserted in the figure
		"""
		self.nrows = nrows

	def set_ncols( self, ncols ):
		"""Set the number of columns of subplots that will be inserted in the figure

		This is used to compute the horizontal spacing between the rows.

		Parameters
		----------
		ncols : int
			Number of columns of subplots that will be inserted in the figure
		"""
		self.ncols = ncols

	def get_margin_left( self ):
		"""Retrieve the left margin"""
		return self.margin_left

	def set_margin_left( self, margin_left ):
		"""Set the left margin

		Parameters
		----------
		margin_left : float
			Left margin, in inches
		"""
		self.margin_left = margin_left

	def get_margin_bottom( self ):
		"""Retrieve the bottom margin"""
		return self.margin_bottom

	def set_margin_bottom( self, margin_bottom ):
		"""Set the bottom margin

		Parameters
		----------
		margin_bottom : float
			Bottom margin, in inches
		"""
		self.margin_bottom = margin_bottom

	def get_margin_right( self ):
		"""Retrieve the right margin"""
		return self.margin_right

	def set_margin_right( self, margin_right ):
		"""Set the right margin

		Parameters
		----------
		margin_right : float
			Right margin, in inches
		"""
		self.margin_right = margin_right

	def get_margin_top( self ):
		"""Retrieve the top margin"""
		return self.margin_top

	def set_margin_top( self, margin_top ):
		"""Set the top margin

		Parameters
		----------
		margin_top : float
			Top margin, in inches
		"""
		self.margin_top = margin_top

	def set_spacing_h( self, spacing_h ):
		"""Set the horizontal spacing between panels.
		By default it is equal to the sum of the left and right margins.

		Parameters
		----------
		spacing_h : float or None
			Horizontal spacing in inches, or None to reset to default.
		"""
		self.spacing_h = spacing_h

	def set_spacing_v( self, spacing_v ):
		"""Set the vertical spacing between panels.
		By default it is equal to the sum of the top and bottom margins.

		Parameters
		----------
		spacing_v : float or None
			Vertical spacing in inches, or None to reset to default.
		"""
		self.spacing_v = spacing_v

	def set_cbar_loc( self, cbar_loc ):
		"""Set the location of the color bar

		Parameters
		----------
		cbar_loc : "left", "bottom", "right" or "top"
			Location of the color with respect to the plot area,
			any other value will not reserve any room for the color bar on the figure.
		"""
		self.cbar_loc = cbar_loc

	def set_cbar_width( self, cbar_width ):
		"""Set the width of the color bar

		Parameters
		----------
		cbar_width : float
			Set the width of the color bar plot area, in inches
		"""
		self.cbar_width = cbar_width

	def set_cbar_pad( self, cbar_pad ):
		"""Set the padding between the color bar and the plot area.

		Parameters
		----------
		cbar_loc : float
			Set the width of the color bar axis area, in inches
		"""
		self.cbar_pad = cbar_pad

	def get_figure_size( self ):
		"""Determine the actual size of the figure.

		This will determine the total size of the figure, including margins and color bar if needed.

		Returns
		-------
		tuple
			Horizontal and vertical size of the figure, in inches
		"""
		size_h = self.size_h
		size_v = self.size_v

		if self.spacing_h is None:
			spacing_h = self.margin_left + self.margin_right
		else:
			spacing_h = self.spacing_h

		if self.spacing_v is None:
			spacing_v = self.margin_bottom + self.margin_top
		else:
			spacing_v = self.spacing_v

		if self.type_h == self.SIZE_RATIO_AX:
			if self.type_v == self.SIZE_RATIO_AX:
				raise Exception( "type_h and type_v cannot be both SIZE_RATIO_AX at the same time." )
			elif self.type_v == self.SIZE_AX:
				size_h *= size_v
			elif self.type_v == self.SIZE_AXES:
				size_h *= ( size_v - spacing_v * ( self.nrows - 1 ) ) / self.nrows
			elif self.type_v == self.SIZE_NO_CBAR:
				size_h *= ( size_v - self.margin_bottom - self.margin_top - spacing_v * ( self.nrows - 1 ) ) / self.nrows
			else:
				size_h *= ( size_v - ( self.cbar_width + self.cbar_pad if self.cbar_loc == "bottom" or self.cbar_loc == "top" else 0. ) - self.margin_bottom - self.margin_top - spacing_v * ( self.nrows - 1 ) ) / self.nrows

		if self.type_v == self.SIZE_RATIO_AX:
			if self.type_h == self.SIZE_RATIO_AX:
				# Should not happen, but just in case
				raise Exception( "type_h and type_v cannot be both SIZE_RATIO_AX at the same time." )
			elif self.type_h == self.SIZE_AX:
				size_v *= size_h
			elif self.type_h == self.SIZE_AXES:
				size_v *= ( size_h - spacing_h * ( self.ncols - 1 ) ) / self.ncols
			elif self.type_h == self.SIZE_NO_CBAR:
				size_v *= ( size_h - self.margin_left - self.margin_right - spacing_h * ( self.ncols - 1 ) ) / self.ncols
			else:
				size_v *= ( size_h - ( self.cbar_width + self.cbar_pad if self.cbar_loc == "left" or self.cbar_loc == "right" else 0. ) - self.margin_left - self.margin_right - spacing_h * ( self.ncols - 1 ) ) / self.ncols

		if self.type_h == self.SIZE_AX or self.type_h == self.SIZE_RATIO_AX:
			size_h *= self.ncols
			size_h += spacing_h * ( self.ncols - 1 )

		if self.type_v == self.SIZE_AX or self.type_v == self.SIZE_RATIO_AX:
			size_v *= self.nrows
			size_v += spacing_v * ( self.nrows - 1 )

		if self.type_h == self.SIZE_AXES or self.type_h == self.SIZE_AX or self.type_h == self.SIZE_RATIO_AX:
			size_h += self.margin_left + self.margin_right
		if self.type_v == self.SIZE_AXES or self.type_v == self.SIZE_AX or self.type_v == self.SIZE_RATIO_AX:
			size_v += self.margin_bottom + self.margin_top

		if ( self.type_h == self.SIZE_NO_CBAR or self.type_h == self.SIZE_AXES or self.type_h == self.SIZE_AX or self.type_h == self.SIZE_RATIO_AX ) and ( self.cbar_loc == "left" or self.cbar_loc == "right" ):
			size_h += self.cbar_width + self.cbar_pad
		if ( self.type_v == self.SIZE_NO_CBAR or self.type_v == self.SIZE_AXES or self.type_v == self.SIZE_AX or self.type_v == self.SIZE_RATIO_AX ) and ( self.cbar_loc == "bottom" or self.cbar_loc == "top" ):
			size_v += self.cbar_width + self.cbar_pad

		return ( size_h, size_v )

	def get_figure_args( self ):
		"""
		Get the size arguments for when creating a figure.

		Returns
		-------
		dict
			Arguments for the matplotlib.pyplot.figure() function.
		"""
		return { "figsize": self.get_figure_size() }

	def get_subplots_args( self ):
		"""
		Get the arguments for the location of the subplots.

		Returns
		-------
		dict
			Arguments for the Figure.subplots_adjust() function.
		"""
		size_h, size_v = self.get_figure_size()

		left = self.margin_left
		bottom = self.margin_bottom
		right = self.margin_right
		top = self.margin_top

		if self.cbar_loc == "left":
			left += self.cbar_width + self.cbar_pad
		if self.cbar_loc == "right":
			right += self.cbar_width + self.cbar_pad
		if self.cbar_loc == "bottom":
			bottom += self.cbar_width + self.cbar_pad
		if self.cbar_loc == "top":
			top += self.cbar_width + self.cbar_pad

		if self.spacing_h is None:
			spacing_h = self.margin_left + self.margin_right
		else:
			spacing_h = self.spacing_h

		if self.spacing_v is None:
			spacing_v = self.margin_bottom + self.margin_top
		else:
			spacing_v = self.spacing_v

		if self.ncols > 1 and spacing_h > 0.:
			wspace = self.ncols / ( ( size_h - right - left ) / spacing_h - ( self.ncols - 1 ) )
		else:
			wspace = 0.

		if self.nrows > 1 and spacing_v > 0.:
			hspace = self.nrows / ( ( size_v - top - bottom ) / spacing_v - ( self.nrows - 1 ) )
		else:
			hspace = 0.

		return { "left": left / size_h, "bottom": bottom / size_v, "right": 1. - right / size_h, "top": 1. - top / size_v, "wspace": wspace, "hspace": hspace }

	def has_cbar( self ):
		"""Retrieve whether room has been reserved for the color bar.

		Returns
		-------
		bool
			Whether room is reserved for the color bar.
		"""
		return self.cbar_loc == "left" or self.cbar_loc == "right" or self.cbar_loc == "bottom" or self.cbar_loc == "top"

	def get_cbar_ax_spec( self ):
		"""Retrieve the location of the color bar in the figure.

		Returns
		-------
		list
			Location of the area for the color bar, which can be used as an argument to Figure.add_axes().
		"""
		size_h, size_v = self.get_figure_size()

		if self.cbar_loc == "left":
			return [ self.margin_left / size_h, self.margin_bottom / size_v, self.cbar_width / size_h, 1. - ( self.margin_bottom + self.margin_top ) / size_v ]
		if self.cbar_loc == "right":
			return [ 1. - ( self.cbar_width + self.cbar_pad ) / size_h, self.margin_bottom / size_v, self.cbar_width / size_h, 1. - ( self.margin_bottom + self.margin_top ) / size_v ]
		if self.cbar_loc == "bottom":
			return [ self.margin_left / size_h, self.margin_bottom / size_v, 1. - ( self.margin_left + self.margin_right ) / size_h, self.cbar_width / size_v ]
		if self.cbar_loc == "top":
			return [ self.margin_left / size_h, 1. - ( self.cbar_width + self.margin_top ) / size_v, 1. - ( self.margin_left + self.margin_right ) / size_h, self.cbar_width / size_v ]

		return None

	def get_cbar_orientation( self ):
		"""Retrieve the orientation of the color bar.

		Returns
		-------
		"vertical", "horizontal" or None
			Orientation of the color bar, which can be provided as the value of the "orientation" parameter of Figure.colorbar(), or None if disabled.
		"""
		if self.cbar_loc == "left" or self.cbar_loc == "right":
			return "vertical"
		if self.cbar_loc == "bottom" or self.cbar_loc == "top":
			return "horizontal"

		return None
