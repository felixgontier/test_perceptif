# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.media


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.CAPTION | wx.MAXIMIZE_BOX | wx.STAY_ON_TOP | wx.NO_BORDER)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_mediaCtrl12 = wx.media.MediaCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize)
        self.m_mediaCtrl12.Load(u"C:\\Python27\\Template\\Extrait 1.mp4")
        self.m_mediaCtrl12.SetPlaybackRate(1)
        self.m_mediaCtrl12.SetVolume(1)
        bSizer6.Add(self.m_mediaCtrl12, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer6)
        self.m_panel2.Layout()
        bSizer6.Fit(self.m_panel2)
        bSizer5.Add(self.m_panel2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1168, 845), style=wx.MAXIMIZE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Bienvenue ! \n\n"
                                                            u"Vous allez écouter 13 scènes sonores urbaines et les évaluer selon 20 "
                                                            u"critères.\n Vous ne pourrez écouter chaque extrait qu'une seule fois.\n\n "
                                                            u"Ce test a une durée d'environ 20 minutes.\n\n",
                                           wx.Point(-1, -1), wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))

        bSizer7.Add(self.m_staticText3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Identifiant (5 lettres)", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(23, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gSizer3.Add(self.m_staticText4, 1,
                    wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_textCtrl1.SetMaxLength(5)
        self.m_textCtrl1.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        gSizer3.Add(self.m_textCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        bSizer7.Add(gSizer3, 0, wx.ALIGN_CENTER, 5)

        self.m_panel11 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 10), wx.TAB_TRAVERSAL)
        self.m_panel11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        self.m_panel11.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        bSizer7.Add(self.m_panel11, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Suivant", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_button5.SetFont(wx.Font(23, 70, 90, 90, False, wx.EmptyString))

        bSizer7.Add(self.m_button5, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button5.Bind(wx.EVT_BUTTON, self.m_button5OnButtonClick)
        self.Bind(wx.EVT_IDLE, self.m_button5Activation)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_button5OnButtonClick(self, event):
        event.Skip()

    def m_button5Activation(self, event):

        event.Skip()


###########################################################################
## Class MainFrameBase111
###########################################################################

class MainFrameBase111(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Detection de transition", pos=wx.DefaultPosition,
                          size=wx.Size(1391, 829), style=wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.NO_BORDER)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_button17 = wx.Button(self.m_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size(20, 20),
                                    0 | wx.NO_BORDER)
        self.m_button17.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        self.m_button17.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer5.Add(self.m_button17, 0, wx.ALL, 5)

        fgSizer7 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText127 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Point", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_LEFT)
        self.m_staticText127.Wrap(-1)
        self.m_staticText127.SetFont(wx.Font(20, 70, 94, 90, False, wx.EmptyString))
        self.m_staticText127.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer7.Add(self.m_staticText127, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_staticText126 = wx.StaticText(self.m_panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_LEFT)
        self.m_staticText126.Wrap(-1)
        self.m_staticText126.SetFont(wx.Font(20, 70, 94, 90, False, wx.EmptyString))
        self.m_staticText126.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer7.Add(self.m_staticText126, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticText1261 = wx.StaticText(self.m_panel, wx.ID_ANY, u"/13", wx.DefaultPosition, wx.DefaultSize,
                                              wx.ALIGN_LEFT)
        self.m_staticText1261.Wrap(-1)
        self.m_staticText1261.SetFont(wx.Font(20, 70, 94, 90, False, wx.EmptyString))
        self.m_staticText1261.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer7.Add(self.m_staticText1261, 0, wx.ALL, 5)

        bSizer5.Add(fgSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel9 = wx.Panel(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer1 = wx.FlexGridSizer(0, 3, 1, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)

        self.m_staticText91 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Général", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText91.Wrap(-1)
        self.m_staticText91.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText91.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer1.Add(self.m_staticText91, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticline213 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_VERTICAL)
        fgSizer1.Add(self.m_staticline213, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer41 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer41.SetFlexibleDirection(wx.BOTH)
        fgSizer41.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText9 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText9.Wrap(-1)
        self.m_staticText9.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText9.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Bruyant", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText10.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText10, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        fgSizer1513 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer1513.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer1513.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1513.SetMinSize(wx.Size(50, 20))
        self.r_1_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_101.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer1513.Add(self.r_1_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_2_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_3_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_4_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer1513.Add(self.r_5_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_6_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_7_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_8_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_9_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_10_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_101 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_101.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_101.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513.Add(self.r_11_101, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer41.Add(fgSizer1513, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText11 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Silencieux", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText12.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Ennuyeux, inintéressant", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        self.m_staticText13.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText13.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText13, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        fgSizer15132 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer15132.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer15132.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer15132.SetMinSize(wx.Size(50, 20))
        self.r_1_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_102.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer15132.Add(self.r_1_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_2_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_3_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_4_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer15132.Add(self.r_5_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_6_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_7_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_8_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_9_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_10_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_102 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_102.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_102.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132.Add(self.r_11_102, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer41.Add(fgSizer15132, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText14 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Stimulant, intéressant", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        self.m_staticText14.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText14.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.m_staticText15 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText15.Wrap(-1)
        self.m_staticText15.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText15.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText15, 0, wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Inerte, amorphe", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        self.m_staticText16.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText16.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText16, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        fgSizer151321 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer151321.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer151321.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer151321.SetMinSize(wx.Size(50, 20))
        self.r_1_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_103.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer151321.Add(self.r_1_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_2_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_3_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_4_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer151321.Add(self.r_5_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_6_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_7_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_8_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_9_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_10_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_103 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_103.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_103.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151321.Add(self.r_11_103, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer41.Add(fgSizer151321, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText17 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Animé, mouvementé", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText17.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_staticText151 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText151.Wrap(-1)
        self.m_staticText151.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText151.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText151, 0, wx.ALL, 5)

        self.m_staticText161 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Agité, chaotique", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText161.Wrap(-1)
        self.m_staticText161.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText161.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText161, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        fgSizer1513211 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer1513211.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer1513211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1513211.SetMinSize(wx.Size(50, 20))
        self.r_1_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_104.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer1513211.Add(self.r_1_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_2_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_3_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_4_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer1513211.Add(self.r_5_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_6_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_7_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_8_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_9_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_10_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_104 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_104.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_104.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513211.Add(self.r_11_104, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer41.Add(fgSizer1513211, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText171 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Calme, tranquille", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText171.Wrap(-1)
        self.m_staticText171.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText171.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer41.Add(self.m_staticText171, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer41, 1, wx.EXPAND, 5)

        self.m_staticline2131 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.LI_VERTICAL)
        fgSizer1.Add(self.m_staticline2131, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline21312 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.LI_VERTICAL)
        fgSizer1.Add(self.m_staticline21312, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline21311 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.LI_VERTICAL)
        fgSizer1.Add(self.m_staticline21311, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText911 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Sources", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText911.Wrap(-1)
        self.m_staticText911.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText911.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer1.Add(self.m_staticText911, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_staticline2132 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.LI_VERTICAL)
        fgSizer1.Add(self.m_staticline2132, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer42 = wx.FlexGridSizer(0, 8, 0, 0)
        fgSizer42.SetFlexibleDirection(wx.BOTH)
        fgSizer42.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText9112 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText9112.Wrap(-1)
        self.m_staticText9112.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText9112.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText9112, 0, wx.ALL, 5)

        self.m_staticText91121 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText91121.Wrap(-1)
        self.m_staticText91121.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText91121.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText91121, 0, wx.ALL, 5)

        self.m_staticText9111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Volume sonore", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText9111.Wrap(-1)
        self.m_staticText9111.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText9111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText9111, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText911211 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText911211.Wrap(-1)
        self.m_staticText911211.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText911211.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText911211, 0, wx.ALL, 5)

        self.m_staticText911212 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText911212.Wrap(-1)
        self.m_staticText911212.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText911212.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText911212, 0, wx.ALL, 5)

        self.m_staticText911213 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText911213.Wrap(-1)
        self.m_staticText911213.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText911213.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText911213, 0, wx.ALL, 5)

        self.m_staticText91111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Temps de présence", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText91111.Wrap(-1)
        self.m_staticText91111.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText91111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText91111, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText9112131 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText9112131.Wrap(-1)
        self.m_staticText9112131.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText9112131.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText9112131, 0, wx.ALL, 5)

        self.m_staticline51 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline51, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline511 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline511, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline512 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline512, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline513 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline513, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline5121 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline5121, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline514 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline514, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline516 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline516, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline517 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        fgSizer42.Add(self.m_staticline517, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText91112 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Circulation routière", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText91112.Wrap(-1)
        self.m_staticText91112.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText91112.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText91112, 0, wx.ALL, 5)

        self.m_staticText3712 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText3712.Wrap(-1)
        self.m_staticText3712.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3712.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3712, 0, wx.ALL, 5)

        fgSizer15132712 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer15132712.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer15132712.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer15132712.SetMinSize(wx.Size(50, 20))
        self.r_1_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_105.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer15132712.Add(self.r_1_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_2_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_3_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_4_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer15132712.Add(self.r_5_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_6_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_7_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_8_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_9_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_10_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_105 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_105.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_105.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712.Add(self.r_11_105, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer15132712, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3812 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText3812.Wrap(-1)
        self.m_staticText3812.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3812.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3812, 0, wx.ALL, 5)

        self.m_staticline21321 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline21321, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText37111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition, wx.DefaultSize,
                                               0)
        self.m_staticText37111.Wrap(-1)
        self.m_staticText37111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText37111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText37111, 0, wx.ALL, 5)

        fgSizer15132711 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer15132711.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer15132711.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer15132711.SetMinSize(wx.Size(50, 20))
        self.r_1_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_106.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer15132711.Add(self.r_1_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_2_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_3_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_4_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer15132711.Add(self.r_5_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_6_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_7_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_8_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_9_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_10_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_106 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_106.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_106.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711.Add(self.r_11_106, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer15132711, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText38111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText38111.Wrap(-1)
        self.m_staticText38111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText38111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText38111, 0, wx.ALL, 5)

        self.m_staticText911121 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Deux roues", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText911121.Wrap(-1)
        self.m_staticText911121.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText911121.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText911121, 0, wx.ALL, 5)

        self.m_staticText37121 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText37121.Wrap(-1)
        self.m_staticText37121.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText37121.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText37121, 0, wx.ALL, 5)

        fgSizer151327121 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer151327121.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer151327121.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer151327121.SetMinSize(wx.Size(50, 20))
        self.r_1_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_107.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer151327121.Add(self.r_1_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_2_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_3_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_4_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer151327121.Add(self.r_5_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_6_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_7_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_8_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_9_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_10_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_107 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_107.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_107.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121.Add(self.r_11_107, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer151327121, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText38121 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText38121.Wrap(-1)
        self.m_staticText38121.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText38121.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText38121, 0, wx.ALL, 5)

        self.m_staticline213211 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline213211, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText371111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.m_staticText371111.Wrap(-1)
        self.m_staticText371111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText371111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText371111, 0, wx.ALL, 5)

        fgSizer151327111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer151327111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer151327111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer151327111.SetMinSize(wx.Size(50, 20))
        self.r_1_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_108.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer151327111.Add(self.r_1_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_2_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_3_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_4_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer151327111.Add(self.r_5_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_6_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_7_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_8_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_9_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_10_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_108 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_108.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_108.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111.Add(self.r_11_108, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer151327111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText381111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText381111.Wrap(-1)
        self.m_staticText381111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText381111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText381111, 0, wx.ALL, 5)

        self.m_staticText9111211 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Véhicules légers", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText9111211.Wrap(-1)
        self.m_staticText9111211.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText9111211.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText9111211, 0, wx.ALL, 5)

        self.m_staticText371211 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText371211.Wrap(-1)
        self.m_staticText371211.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText371211.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText371211, 0, wx.ALL, 5)

        fgSizer1513271211 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer1513271211.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer1513271211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1513271211.SetMinSize(wx.Size(50, 20))
        self.r_1_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_109.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer1513271211.Add(self.r_1_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_2_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_3_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_4_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer1513271211.Add(self.r_5_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_6_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_7_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_8_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_9_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_10_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_109 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_109.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_109.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211.Add(self.r_11_109, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer1513271211, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText381211 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText381211.Wrap(-1)
        self.m_staticText381211.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText381211.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText381211, 0, wx.ALL, 5)

        self.m_staticline2132111 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline2132111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText3711111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition, wx.DefaultSize,
                                                 0)
        self.m_staticText3711111.Wrap(-1)
        self.m_staticText3711111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3711111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3711111, 0, wx.ALL, 5)

        fgSizer1513271111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer1513271111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer1513271111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1513271111.SetMinSize(wx.Size(50, 20))
        self.r_1_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_110.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer1513271111.Add(self.r_1_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_2_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_3_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_4_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer1513271111.Add(self.r_5_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_6_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_7_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_8_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_9_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_10_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_110 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_110.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_110.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111.Add(self.r_11_110, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer1513271111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3811111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText3811111.Wrap(-1)
        self.m_staticText3811111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3811111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3811111, 0, wx.ALL, 5)

        self.m_staticText91112111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Véhicules lourds", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.m_staticText91112111.Wrap(-1)
        self.m_staticText91112111.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText91112111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText91112111, 0, wx.ALL, 5)

        self.m_staticText3712111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText3712111.Wrap(-1)
        self.m_staticText3712111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3712111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3712111, 0, wx.ALL, 5)

        fgSizer15132712111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer15132712111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer15132712111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer15132712111.SetMinSize(wx.Size(50, 20))
        self.r_1_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_111.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer15132712111.Add(self.r_1_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_2_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_3_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_4_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer15132712111.Add(self.r_5_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_6_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_7_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_8_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_9_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_10_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_111 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_111.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111.Add(self.r_11_111, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer15132712111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3812111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText3812111.Wrap(-1)
        self.m_staticText3812111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3812111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3812111, 0, wx.ALL, 5)

        self.m_staticline21321111 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline21321111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText37111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.m_staticText37111111.Wrap(-1)
        self.m_staticText37111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText37111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText37111111, 0, wx.ALL, 5)

        fgSizer15132711111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer15132711111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer15132711111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer15132711111.SetMinSize(wx.Size(50, 20))
        self.r_1_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_112.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer15132711111.Add(self.r_1_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_2_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_3_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_4_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer15132711111.Add(self.r_5_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_6_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_7_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_8_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_9_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_10_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_112 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_112.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_112.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111.Add(self.r_11_112, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer15132711111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText38111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.m_staticText38111111.Wrap(-1)
        self.m_staticText38111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText38111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText38111111, 0, wx.ALL, 5)

        self.m_staticText911121111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Petits oiseaux", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_staticText911121111.Wrap(-1)
        self.m_staticText911121111.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText911121111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText911121111, 0, wx.ALL, 5)

        self.m_staticText37121111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.m_staticText37121111.Wrap(-1)
        self.m_staticText37121111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText37121111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText37121111, 0, wx.ALL, 5)

        fgSizer151327121111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer151327121111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer151327121111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer151327121111.SetMinSize(wx.Size(50, 20))
        self.r_1_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_113.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer151327121111.Add(self.r_1_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_2_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_3_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_4_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer151327121111.Add(self.r_5_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_6_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_7_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_8_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_9_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_10_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_113 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_113.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_113.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111.Add(self.r_11_113, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer151327121111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText38121111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.m_staticText38121111.Wrap(-1)
        self.m_staticText38121111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText38121111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText38121111, 0, wx.ALL, 5)

        self.m_staticline213211111 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline213211111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText371111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_staticText371111111.Wrap(-1)
        self.m_staticText371111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText371111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText371111111, 0, wx.ALL, 5)

        fgSizer151327111111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer151327111111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer151327111111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer151327111111.SetMinSize(wx.Size(50, 20))
        self.r_1_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_114.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer151327111111.Add(self.r_1_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_2_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_3_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_4_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer151327111111.Add(self.r_5_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_6_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_7_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_8_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_9_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_10_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_114 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_114.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_114.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111.Add(self.r_11_114, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer151327111111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText381111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_staticText381111111.Wrap(-1)
        self.m_staticText381111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText381111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText381111111, 0, wx.ALL, 5)

        self.m_staticText9111211111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Klaxons, sirènes", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText9111211111.Wrap(-1)
        self.m_staticText9111211111.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText9111211111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText9111211111, 0, wx.ALL, 5)

        self.m_staticText371211111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_staticText371211111.Wrap(-1)
        self.m_staticText371211111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText371211111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText371211111, 0, wx.ALL, 5)

        fgSizer1513271211111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer1513271211111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer1513271211111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1513271211111.SetMinSize(wx.Size(50, 20))
        self.r_1_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_115.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer1513271211111.Add(self.r_1_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_2_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_3_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_4_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer1513271211111.Add(self.r_5_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_6_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_7_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_8_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_9_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_10_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_115 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_115.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_115.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271211111.Add(self.r_11_115, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer1513271211111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText381211111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_staticText381211111.Wrap(-1)
        self.m_staticText381211111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText381211111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText381211111, 0, wx.ALL, 5)

        self.m_staticline2132111111 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                    wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline2132111111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText3711111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText3711111111.Wrap(-1)
        self.m_staticText3711111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3711111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3711111111, 0, wx.ALL, 5)

        fgSizer1513271111111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer1513271111111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer1513271111111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1513271111111.SetMinSize(wx.Size(50, 20))
        self.r_1_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_116.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer1513271111111.Add(self.r_1_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_2_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_3_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_4_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer1513271111111.Add(self.r_5_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_6_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_7_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_8_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_9_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_10_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_116 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_116.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_116.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer1513271111111.Add(self.r_11_116, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer1513271111111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3811111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText3811111111.Wrap(-1)
        self.m_staticText3811111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3811111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3811111111, 0, wx.ALL, 5)

        self.m_staticText91112111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Voix", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.m_staticText91112111111.Wrap(-1)
        self.m_staticText91112111111.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText91112111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText91112111111, 0, wx.ALL, 5)

        self.m_staticText3712111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText3712111111.Wrap(-1)
        self.m_staticText3712111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3712111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3712111111, 0, wx.ALL, 5)

        fgSizer15132712111111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer15132712111111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer15132712111111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer15132712111111.SetMinSize(wx.Size(50, 20))
        self.r_1_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_117.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer15132712111111.Add(self.r_1_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_2_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_3_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_4_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer15132712111111.Add(self.r_5_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_6_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_7_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_8_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_9_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_10_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_117 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_117.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_117.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132712111111.Add(self.r_11_117, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer15132712111111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3812111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText3812111111.Wrap(-1)
        self.m_staticText3812111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3812111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText3812111111, 0, wx.ALL, 5)

        self.m_staticline21321111111 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                     wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline21321111111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText37111111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.m_staticText37111111111.Wrap(-1)
        self.m_staticText37111111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText37111111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText37111111111, 0, wx.ALL, 5)

        fgSizer15132711111111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer15132711111111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer15132711111111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer15132711111111.SetMinSize(wx.Size(50, 20))
        self.r_1_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_118.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer15132711111111.Add(self.r_1_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_2_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_3_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_4_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer15132711111111.Add(self.r_5_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_6_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_7_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_8_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_9_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_10_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_118 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_118.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_118.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer15132711111111.Add(self.r_11_118, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer15132711111111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText38111111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.m_staticText38111111111.Wrap(-1)
        self.m_staticText38111111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText38111111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText38111111111, 0, wx.ALL, 5)

        self.m_staticText911121111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Bruits de pas", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.m_staticText911121111111.Wrap(-1)
        self.m_staticText911121111111.SetFont(wx.Font(18, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText911121111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText911121111111, 0, wx.ALL, 5)

        self.m_staticText37121111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très faible", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.m_staticText37121111111.Wrap(-1)
        self.m_staticText37121111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText37121111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText37121111111, 0, wx.ALL, 5)

        fgSizer151327121111111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer151327121111111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer151327121111111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer151327121111111.SetMinSize(wx.Size(50, 20))
        self.r_1_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_119.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer151327121111111.Add(self.r_1_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_2_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_3_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_4_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer151327121111111.Add(self.r_5_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_6_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_7_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_8_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_9_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_10_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_119 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_119.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_119.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327121111111.Add(self.r_11_119, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer151327121111111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText38121111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Très fort", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.m_staticText38121111111.Wrap(-1)
        self.m_staticText38121111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText38121111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText38121111111, 0, wx.ALL, 5)

        self.m_staticline213211111111 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                      wx.LI_VERTICAL)
        fgSizer42.Add(self.m_staticline213211111111, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText371111111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Jamais", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.m_staticText371111111111.Wrap(-1)
        self.m_staticText371111111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText371111111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText371111111111, 0, wx.ALL, 5)

        fgSizer151327111111111 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer151327111111111.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer151327111111111.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer151327111111111.SetMinSize(wx.Size(50, 20))
        self.r_1_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      wx.RB_GROUP | wx.NO_BORDER)
        self.r_1_120.SetFont(wx.Font(30, 73, 94, 90, False, "@Adobe Kaiti Std R"))
        self.r_1_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer151327111111111.Add(self.r_1_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_2_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_2_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_2_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_3_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_3_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_3_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_4_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_4_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_4_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_5_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_5_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        fgSizer151327111111111.Add(self.r_5_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_6_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_6_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_6_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_7_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_7_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_7_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_8_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_8_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_8_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_9_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                      0 | wx.NO_BORDER)
        self.r_9_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_9_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_10_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_10_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_10_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.r_11_120 = wx.RadioButton(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(20, 20),
                                       0 | wx.NO_BORDER)
        self.r_11_120.SetFont(wx.Font(40, 70, 90, 90, False, wx.EmptyString))
        self.r_11_120.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        fgSizer151327111111111.Add(self.r_11_120, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer42.Add(fgSizer151327111111111, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText381111111111 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Continuellement", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.m_staticText381111111111.Wrap(-1)
        self.m_staticText381111111111.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText381111111111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        fgSizer42.Add(self.m_staticText381111111111, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer42, 1, wx.EXPAND, 5)

        bSizer5.Add(fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel91 = wx.Panel(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5.Add(self.m_panel91, 1, wx.EXPAND | wx.ALL, 5)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText57 = wx.StaticText(self.m_panel, wx.ID_ANY, u"Commentaires", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText57.Wrap(-1)
        self.m_staticText57.SetFont(wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText57.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        bSizer19.Add(self.m_staticText57, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, 100),
                                       0)
        bSizer19.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        bSizer5.Add(bSizer19, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel911 = wx.Panel(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5.Add(self.m_panel911, 1, wx.EXPAND | wx.ALL, 5)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_btHello2 = wx.Button(self.m_panel, wx.ID_ANY, u"Écouter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_btHello2.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer17.Add(self.m_btHello2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button412 = wx.Button(self.m_panel, wx.ID_ANY, u"Suivant", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button412.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))
        self.m_button412.Enable(False)

        bSizer17.Add(self.m_button412, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer5.Add(bSizer17, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel5 = wx.Panel(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.m_panel5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))

        bSizer5.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer3.Add(bSizer4, 1, wx.EXPAND, 5)

        self.m_panel.SetSizer(bSizer3)
        self.m_panel.Layout()
        bSizer3.Fit(self.m_panel)
        bSizer2.Add(self.m_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(bSizer2)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_MOTION, self.MainFrameBase1OnMotion)
        self.m_button17.Bind(wx.EVT_BUTTON, self.m_button17OnButtonClick)
        self.r_1_101.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_102.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_103.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_104.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_105.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_106.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_107.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_108.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_109.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_110.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_111.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_112.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_113.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_114.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_115.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_116.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_117.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_118.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_119.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.r_1_120.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn321212OnRadioButton)
        self.m_btHello2.Bind(wx.EVT_BUTTON, self.m_btHello2Click)
        self.m_button412.Bind(wx.EVT_BUTTON, self.m_button412OnButtonClick)
        self.m_panel5.Bind(wx.EVT_MOTION, self.m_panel5OnMotion)
        self.Bind(wx.EVT_IDLE, self.m_button412Activation)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def MainFrameBase1OnMotion(self, event):
        event.Skip()

    def m_button17OnButtonClick(self, event):
        event.Skip()

    def m_radioBtn321212OnRadioButton(self, event):
        event.Skip()

    def m_btHello2Click(self, event):
        event.Skip()

    def m_button412OnButtonClick(self, event):
        event.Skip()

    def m_panel5OnMotion(self, event):
        event.Skip()

    def m_button412Activation(self, event):
        event.Skip()
