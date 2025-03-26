**Matplotlib Pyplot: Complete Guide with Examples**

---

## **1. What is `pyplot`?**
`matplotlib.pyplot` is a collection of functions that make Matplotlib work like MATLAB. Each function makes some change to a figure, such as creating a figure, plotting a line, setting labels, etc.

```python
import matplotlib.pyplot as plt
```

---

## **2. Basic Plotting Functions**

### **2.1. `plt.plot()`**
**Purpose:** Used to plot **line graphs**.

**Syntax:**
```python
plt.plot(x, y, style, label, color, marker, linewidth, linestyle)
```
- `x, y`: Data points.
- `style`: A format string like `'bo'` (blue circle markers).
- `label`: Legend label.
- `color`: Color of the line.
- `marker`: Marker style (`o`, `x`, `s`, etc.).
- `linewidth`: Width of the line.
- `linestyle`: Dashed (`--`), solid (`-`), dotted (`:`), etc.

**Example:**
```python
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='Sine Wave', color='b', marker='o', linewidth=2, linestyle='--')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Line Plot Example')
plt.legend()
plt.show()
```

---

### **2.2. `plt.scatter()`**
**Purpose:** Used to plot **scatter plots**.

**Example:**
```python
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='r', marker='x')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()
```

---

### **2.3. `plt.bar()`**
**Purpose:** Creates a **bar chart**.

**Example:**
```python
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color=['red', 'blue', 'green', 'purple'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
```

---

### **2.4. `plt.hist()`**
**Purpose:** Plots a **histogram** (used for distributions).

**Example:**
```python
data = np.random.randn(1000)

plt.hist(data, bins=30, color='g', alpha=0.7)
plt.xlabel('Data Values')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
```

---

### **2.5. `plt.pie()`**
**Purpose:** Creates a **pie chart**.

**Example:**
```python
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 30, 20, 10]
colors = ['blue', 'green', 'red', 'purple']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True)
plt.title('Programming Language Popularity')
plt.show()
```

---

## **3. Customization Functions**

### **3.1. `plt.xlabel()` & `plt.ylabel()`**
**Purpose:** Labels the X and Y axes.

```python
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
```

---

### **3.2. `plt.title()`**
**Purpose:** Sets the title of the plot.

```python
plt.title('My Plot Title')
```

---

### **3.3. `plt.legend()`**
**Purpose:** Displays a legend.

```python
plt.legend(['Data 1', 'Data 2'])
```

---

### **3.4. `plt.grid()`**
**Purpose:** Adds grid lines.

```python
plt.grid(True, linestyle='--', linewidth=0.5)
```

---

### **3.5. `plt.xticks()` & `plt.yticks()`**
**Purpose:** Customizes tick marks.

```python
plt.xticks([0, 2, 4, 6, 8, 10], ['Zero', 'Two', 'Four', 'Six', 'Eight', 'Ten'])
```

---

## **4. Advanced Plot Features**

### **4.1. `plt.subplot()`**
**Purpose:** Creates multiple plots in one figure.

**Example:**
```python
fig, axs = plt.subplots(2, 2)

x = np.linspace(0, 10, 100)
y = np.sin(x)

axs[0, 0].plot(x, y)
axs[0, 0].set_title('Sine Wave')

axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Scatter Plot')

axs[1, 0].bar(['A', 'B', 'C'], [5, 7, 3])
axs[1, 0].set_title('Bar Chart')

axs[1, 1].hist(np.random.randn(1000))
axs[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
```

---

### **4.2. `plt.fill_between()`**
**Purpose:** Fills the area between two curves.

**Example:**
```python
y1 = np.sin(x)
y2 = np.cos(x)

plt.fill_between(x, y1, y2, color='gray', alpha=0.3)
plt.plot(x, y1, label='Sine')
plt.plot(x, y2, label='Cosine')
plt.legend()
plt.show()
```

---

### **4.3. `plt.axhline()` & `plt.axvline()`**
**Purpose:** Draws horizontal (`axhline`) and vertical (`axvline`) lines.

```python
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=5, color='red', linestyle='dotted')
```

---

### **4.4. `plt.annotate()`**
**Purpose:** Adds annotations to the plot.

```python
plt.annotate('Max Value', xy=(1.5, 1), xytext=(2, 1.5), arrowprops=dict(facecolor='red'))
```

---

## **5. Saving & Displaying Plots**

### **5.1. `plt.savefig()`**
**Purpose:** Saves the figure.

```python
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

---

## **Conclusion**
This guide covered:
- Basic `pyplot` functions.
- Customization of plots.
- Advanced plotting features.

*Pylot function are below given**
**['AbstractContextManager', 'Annotation', 'Arrow', 'Artist', 'AutoLocator', 'AxLine', 'Axes', 'BackendFilter', 'Button', 'Circle', 'Colorizer', 'ColorizingArtist', 'Colormap', 'Enum', 'ExitStack', 'Figure', 'FigureBase', 'FigureCanvasBase', 'FigureManagerBase', 'FixedFormatter', 'FixedLocator', 'FormatStrFormatter', 'Formatter', 'FuncFormatter', 'GridSpec', 'IndexLocator', 'Line2D', 'LinearLocator', 'Locator', 'LogFormatter', 'LogFormatterExponent', 'LogFormatterMathtext', 'LogLocator', 'MaxNLocator', 'MouseButton', 'MultipleLocator', 'Normalize', 'NullFormatter', 'NullLocator', 'PolarAxes', 'Polygon', 'Rectangle', 'ScalarFormatter', 'Slider', 'Subplot', 'SubplotSpec', 'TYPE_CHECKING', 'Text', 'TickHelper', 'Widget', '_ColorizerInterface', '_NO_PYPLOT_NOTE', '_REPL_DISPLAYHOOK', '_ReplDisplayHook', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_add_pyplot_note', '_api', '_auto_draw_if_interactive', '_backend_mod', '_color_sequences', '_colormaps', '_copy_docstring_and_deprecators', '_docstring', '_draw_all_if_interactive', '_get_backend_mod', '_get_pyplot_commands', '_log', '_pylab_helpers', '_warn_if_gui_out_of_main_thread', 'acorr', 'angle_spectrum', 'annotate', 'annotations', 'arrow', 'autoscale', 'autumn', 'axes', 'axhline', 'axhspan', 'axis', 'axline', 'axvline', 'axvspan', 'backend_registry', 'bar', 'bar_label', 'barbs', 'barh', 'bone', 'box', 'boxplot', 'broken_barh', 'cast', 'cbook', 'cla', 'clabel', 'clf', 'clim', 'close', 'cm', 'cohere', 'color_sequences', 'colorbar', 'colormaps', 'connect', 'contour', 'contourf', 'cool', 'copper', 'csd', 'cycler', 'delaxes', 'disconnect', 'draw', 'draw_all', 'draw_if_interactive', 'ecdf', 'errorbar', 'eventplot', 'figaspect', 'figimage', 'figlegend', 'fignum_exists', 'figtext', 'figure', 'fill', 'fill_between', 'fill_betweenx', 'findobj', 'flag', 'functools', 'gca', 'gcf', 'gci', 'get', 'get_backend', 'get_cmap', 'get_current_fig_manager', 'get_figlabels', 'get_fignums', 'get_plot_commands', 'get_scale_names', 'getp', 'ginput', 'gray', 'grid', 'hexbin', 'hist', 'hist2d', 'hlines', 'hot', 'hsv', 'importlib', 'imread', 'imsave', 'imshow', 'inferno', 'inspect', 'install_repl_displayhook', 'interactive', 'ioff', 'ion', 'isinteractive', 'jet', 'legend', 'locator_params', 'logging', 'loglog', 'magma', 'magnitude_spectrum', 'margins', 'matplotlib', 'matshow', 'minorticks_off', 'minorticks_on', 'mlab', 'new_figure_manager', 'nipy_spectral', 'np', 'overload', 'pause', 'pcolor', 'pcolormesh', 'phase_spectrum', 'pie', 'pink', 'plasma', 'plot', 'plot_date', 'polar', 'prism', 'psd', 'quiver', 'quiverkey', 'rc', 'rcParams', 'rcParamsDefault', 'rcParamsOrig', 'rc_context', 'rcdefaults', 'rcsetup', 'rgrids', 'savefig', 'sca', 'scatter', 'sci', 'semilogx', 'semilogy', 'set_cmap', 'set_loglevel', 'setp', 'show', 'specgram', 'spring', 'spy', 'stackplot', 'stairs', 'stem', 'step', 'streamplot', 'style', 'subplot', 'subplot2grid', 'subplot_mosaic', 'subplot_tool', 'subplots', 'subplots_adjust', 'summer', 'suptitle', 'switch_backend', 'sys', 'table', 'text', 'thetagrids', 'threading', 'tick_params', 'ticklabel_format', 'tight_layout', 'time', 'title', 'tricontour', 'tricontourf', 'tripcolor', 'triplot', 'twinx', 'twiny', 'uninstall_repl_displayhook', 'violinplot', 'viridis', 'vlines', 'waitforbuttonpress', 'winter', 'xcorr', 'xkcd', 'xlabel', 'xlim', 'xscale', 'xticks', 'ylabel', 'ylim', 'yscale', 'yticks']**

