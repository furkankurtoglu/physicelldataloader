# mcdsts.plot_contour()


## input:
```
            self: pyMCDSts class instance

            focus: string
                column name within conc dataframe.

            z_slice: floating point number; default is 0
                z-axis position to slice a 2D xy-plain out of the
                3D substrate concentration mesh. if z_slice position
                is not an exact mesh center coordinate, then z_slice
                will be adjusted to the nearest mesh center value,
                the smaller one, if the coordinate lies on a saddle point.

            extrema: tuple of two floats; default is None
                default takes min and max from data.

            alpha: floating point number; default is 1
                alpha channel transparency value
                between 1 (not transparent at all) and 0 (totally transparent).

            fill: boolean; default True
                True generates a matplotlib contourf plot.
                False generates a matplotlib contour plot.

            cmap: string; default viridis.
                matplotlib colormap.
                https://matplotlib.org/stable/tutorials/colors/colormaps.html

            grid: boolean; default True.
                plot axis grid lines.

            xlim: tuple of two floats; default is None
                x axis min and max value.
                default takes min and max from mesh x axis range.

            ylim: tuple of two floats; default is None
                y axis min and max value.
                default takes min and max from mesh y axis range.

            xyequal: boolean; default True
                to specify equal axis spacing for x and y axis.

            figsizepx: list of two integers; default is None
                size of the figure in pixels, (x, y).
                the given x and y will be rounded to the nearest even number,
                to be able to generate movies from the images.
                None tries to take the values from the initial.svg file.
                fall back setting is [640, 480].

            ext: string; default is jpeg
                output image format. possible formats are jpeg, png, and tiff.

            figbgcolor: string; default is None which is transparent (png)
                or white (jpeg, tiff).
                figure background color.

```

## output:
```
            image files under the returned path.

```

## description:
```
            this function generates a matplotlib contour (or contourf) plot
            time series.

            jpeg is by definition a lossy compressed image format.
            png is by definition a lossless compressed image format.
            tiff can by definition be a lossy or lossless compressed format.
            https://en.wikipedia.org/wiki/JPEG
            https://en.wikipedia.org/wiki/Portable_Network_Graphics
            https://en.wikipedia.org/wiki/TIFF
        
```