from __future__ import print_function
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
import wx.grid as gridlib
import wx
import numpy as np
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from copy import deepcopy
import tempfile

import gc
import os
import pickle as pickle
import random
import sys
import time

import matplotlib
import pandas as pd

# matplotlib requires wxPython 2.8+
# set the wxPython version in lib\site-packages\wx.pth file
# or if you have wxversion installed un-comment the lines below
# import wxversion
# wxversion.ensureMinimal('2.8')


matplotlib.use("WXAgg")

# import wx.xrc as xrc
# from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

# from matplotlib.figure import Figure


class PlotFrame(wx.Frame):
    def __init__(self, parent, xdata, ydata):
        wx.Frame.__init__(self, parent, wx.NewId())
        panel = wx.Panel(self)

        self.fig = Figure((5, 4), 75)
        self.canvas = FigureCanvasWxAgg(self, -1, self.fig)
        self.toolbar = NavigationToolbar2Wx(self.canvas)  # matplotlib toolbar
        self.toolbar.Realize()

        # Now put all into a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        # This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        # Best to allow the toolbar to resize!
        sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(sizer)
        self.Fit()

        self.graph = self.fig.add_subplot(111)
        self.lines = self.graph.plot(xdata, ydata, "ro")

        self.toolbar.update()  # Not sure why this is needed - ADS

    def GetToolBar(self):
        # You will need to override GetToolBar if you are using an
        # unmanaged toolbar in your frame
        return self.toolbar

    def SetData(self, xdata, ydata):
        self.lines[0].set_data(xdata, ydata)
        self.canvas.draw()

    def onEraseBackground(self, evt):
        # this is supposed to prevent redraw flicker on some X servers...
        pass


if __name__ == "__main__":
    app = wx.App(0)
    x = np.linspace(0, 2, 100)
    y = np.sin(x)
    frame = PlotFrame(None, x, y)
    frame.Show()
    app.MainLoop()
