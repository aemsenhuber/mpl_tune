This package defines two classes that hold common actions performed on [matplotlib](https://matplotlib.org/) plots.

## Installation

To install mpl_tune, run the following command:
```pip install mpl-tune```

## Usage

The package contains two classes:
* `FigSize` to control to size and margins of figures
* `FigText` to set properties (color, font size) on different elements of a figure

### FigSize

The idea behind FigSize is to give margins in absolute values and let the code compute the relative values that are required by matplotlib. So that in case one want to resize a figure, one does not need to recalculate the margins to fit the new plot size. An example of usage is:
```
figsize = mpl_tune.FigSize()
figsize.set_size_h( 3.5 ) # Horizontal size of the figure, in inches
figsize.set_size_v( 3.0 ) # Vertical size of the figure, in inches
figsize.set_margin_left( 0.6 ) # Left margin, in inches
figsize.set_margin_bottom( 0.4 ) # Bottom margin, in inches
figsize.set_margin_right( 0.1 ) # Right margin, in inches
figsize.set_margin_top( 0.1 ) # Top margin, in inches

# Create the figure from the values set in the figsize object
fig = matplotlib.pyplot.figure( **figsize.get_figure_args() )
fig.subplots_adjust( **figsize.get_subplots_args() )

ax = fig.add_subplot( 1, 1, 1 )

# Use fig and ax to make your plot
```

In addition to the features shown above, the FigSize class can also handle multiple subplots in one figure and reserve space for color bars.

An example usage including those features is:
```
figsize = mpl_tune.FigSize()
figsize.set_size_h( 7.0 )
figsize.set_size_v( 5.0 )
figsize.set_nrows( 2 )
figsize.set_ncols( 2 )
figsize.set_margin_left( 0.6 )
figsize.set_margin_bottom( 0.4 )
figsize.set_margin_right( 0.1 )
figsize.set_margin_top( 0.1 )
figsize.set_spacing_h( 0.65 ) # Horizontal spacing between suplot in in inches; optional, defaults to the sum of left and right margins
figsize.set_spacing_v( 0.45 ) # Vertical spacing between suplot in in inches; optional, defaults to the sum of top and bottom margins
figsize.set_cbar_loc( "bottom" ) # Location of the color bar; can be "left", "right", "top" or "bottom"
figsize.set_cbar_width( 0.1 ) # Width of the color bar, in inches
figsize.set_cbar_pad( 0.45 ) # Padding between the color bar and the nearest axes, in inches

# Create the figure from the values set in the figsize object
fig = matplotlib.pyplot.figure( **figsize.get_figure_args() )
fig.subplots_adjust( **figsize.get_subplots_args() )

ax1 = fig.add_subplot( 2, 2, 1 )
ax2 = fig.add_subplot( 2, 2, 2 )
ax3 = fig.add_subplot( 2, 2, 3 )
ax4 = fig.add_subplot( 2, 2, 4 )

# Use fig and ax* to make your plot

if figsize.has_cbar():
	# Note, in the call below, "coll" represent a collection (or else) that is used to define the color bar
	cax = fig.add_axes( figsize.get_cbar_ax_spec() )
	cb = fig.colorbar( coll, orientation = figsize.get_cbar_orientation(), cax = cax )
```

### FigText

The idea behind FigText is to set at the beginning the main foreground color of the plot and text size, and then to provide a few simple method to set these to the plot's elements.

An example of usage is:

```
usetex = True # or False

matplotlib.rc( "text", usetex = usetex )

figtext = mpl_tune.FigText( color = "black", size = "medium", tex = usetex )

# Create Figure and Axes objects, possibly with the help of FigSize

ax.set_xlabel( figtext.conv( "X axis label" ), **figtext.get_text_args() )
ax.set_ylabel( figtext.conv( "Y axis label" ), **figtext.get_text_args() )

figtext.set_axes( ax )

# If you have a Colorbar instance, you can use
figtext.set_cbar( cb )

# If you have a Legend instance, you can use
figtext.set_legend( legend )
```

The use of the `conv()` method will add the escaping sequences needed to run the text through the TeX (or mathtext) processor so that one does not need to run t
