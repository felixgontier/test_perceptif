import wx
import gui
import time
import os
import sys


class MainFrame11(gui.MainFrameBase111):
    def __init__(self, parent):
        gui.MainFrameBase111.__init__(self, parent)
        self.pas = 0
        self.np = 0
        self.r_1_101.SetValue(0)
        self.r_1_102.SetValue(0)
        self.r_1_103.SetValue(0)
        self.r_1_104.SetValue(0)
        self.r_1_105.SetValue(0)
        self.r_1_106.SetValue(0)
        self.r_1_107.SetValue(0)
        self.r_1_108.SetValue(0)
        self.r_1_109.SetValue(0)
        self.r_1_110.SetValue(0)
        self.r_1_111.SetValue(0)
        self.r_1_112.SetValue(0)
        self.r_1_113.SetValue(0)
        self.r_1_114.SetValue(0)
        self.r_1_115.SetValue(0)
        self.r_1_116.SetValue(0)
        self.r_1_117.SetValue(0)
        self.r_1_118.SetValue(0)
        self.r_1_119.SetValue(0)
        self.r_1_120.SetValue(0)

        self.f_Pt = open('Agr_Point.txt', 'r+')
        self.data = self.f_Pt.readline()
        a = int(self.data) + 1
        if a == 51:
            a = 1
        self.f_Pt.seek(
            0)  # Important: return to the top of the file before reading, otherwise you'll just read an empty string
        self.f_Pt.write(str(a))
        self.f_Pt.close()

        if os.path.isfile('./rnd_Agr_Point.txt'):
            self.f_Pt2 = open('rnd_Agr_Point.txt', 'r')
            self.data_2 = self.f_Pt2.readlines()
            self.data2 = self.data_2[a].split()
            self.rnd = [int(i) for i in self.data2]
            # print self.rnd
            self.f_Pt2.close()

        self.i = 0  # Fichier 1
        self.audio_path = 'audio/'
        self.f_Pt3 = open('audio_list.txt', 'r')
        self.data3 = self.f_Pt3.readlines()
        self.film = [self.audio_path + i for i in self.data3]
        self.f_Pt3.close()

        # self.film=["1_EW_01.wav","1_EW_02.wav","1_EW_06.wav","1_EW_09.wav","1_EW_12.wav","1_EW_15.wav", "1_EW_18.wav", "1_WE_01.wav","1_WE_02.wav", "1_WE_09.wav"]   #Charger les fichiers
        # Set MyFrame3 = affichage (Pour recuperer L identifiant)
        self.affichage = None
        self.affichage = MyFrame3(self)
        self.f = open(self.affichage.Iden() + '\Pt_.txt', 'a+')
        self.f.close()

        self.save = open(self.affichage.Iden() + '\Save.txt', 'a+')
        self.save.write(str(self.data) + "\n")
        self.save.write(str(self.rnd) + "\n")
        self.save.close()
        # Set MyFrame2 = affichage (Ecran Video)
        self.affichage2 = None
        if not self.affichage2:
            self.affichage2 = MyFrame2(self)
        # self.affichage2.Show()

        # Charger le premier film dans la base
        self.affichage2.SetLoad(self.film[self.rnd[self.i] - 1])

    def m_btHello2Click(self, event):
        # Play Button
        if self.affichage2.GetState() == 0:
            self.np = self.np + 1
        self.affichage2.SetPlay()
        self.m_btHello2.Disable()

    def m_button412Activation(self, event):
        self.ind = 0
        for a in range(1, 21):
            if a < 10:
                for b in range(1, 12):
                    if eval("self.r_" + str(b) + "_10" + str(a) + ".GetValue()"):
                        self.ind = self.ind + 1
                        break
            else:
                for b in range(1, 12):
                    if eval("self.r_" + str(b) + "_1" + str(a) + ".GetValue()"):
                        self.ind = self.ind + 1
                        break
        if self.ind == 20 and self.m_btHello2.IsEnabled() == 0:
            self.m_button412.Enable()
        else:
            self.m_button412.Disable()

    def m_button412OnButtonClick(self, event):
        # Suivant Button
        # if self.affichage2.GetState()==0:
        self.ind = 0
        for a in range(1, 21):
            if a < 10:
                for b in range(1, 12):
                    if eval("self.r_" + str(b) + "_10" + str(a) + ".GetValue()"):
                        self.ind = self.ind + 1
                        break
            else:
                for b in range(1, 12):
                    if eval("self.r_" + str(b) + "_1" + str(a) + ".GetValue()"):
                        self.ind = self.ind + 1
                        break
        if self.ind == 20:
            if self.affichage2.GetState() == 0 or self.np > 1:
                self.affichage2.SetStop()
                self.i = self.i + 1
                self.f = open(self.affichage.Iden() + '\Pt_.txt', 'a+')
                self.f.write(str(self.rnd[self.i - 1]) + "\t")
                for a in range(1, 21):
                    if a < 10:
                        for b in range(1, 12):
                            if eval("self.r_" + str(b) + "_10" + str(a) + ".GetValue()"):
                                eval("self.r_" + str(b) + "_10" + str(a) + ".SetValue(0)")
                                break
                    else:
                        for b in range(1, 12):
                            if eval("self.r_" + str(b) + "_1" + str(a) + ".GetValue()"):
                                eval("self.r_" + str(b) + "_1" + str(a) + ".SetValue(0)")
                                break
                    self.f.write(str(b) + "\t")
                self.f.write((self.m_textCtrl3.GetValue().encode('utf8')) + "\n")
                self.f.close()

                self.save = open(self.affichage.Iden() + '\Save.txt', 'a+')
                self.save.write(str(self.rnd[self.i - 1]) + "\n")
                self.save.close()

                if self.i == 13:
                    # print("Test termine, merci pour votre participation!")
                    # self.affichage = MainFrame1_2(self)
                    # self.affichage.Show()
                    self.Hide()
                # self.affichage2.Hide()
                else:
                    self.affichage2.SetLoad(self.film[self.rnd[self.i] - 1])
                    self.m_btHello2.Enable()
                    self.m_button412.Disable()
                    self.Refresh()
                    self.pas = 0
                    self.m_textCtrl3.SetLabel(" ")
                    self.m_staticText126.SetLabel(str(self.i + 1))
            else:
                # print "Attendre la fin de la Video ! "
        else:
            # print "Remplir bien tout !"


# Implementing MyFrame2 - Fenetre Media
class MyFrame2(gui.MyFrame2):
    def __init__(self, parent):
        gui.MyFrame2.__init__(self, parent)

    def Tellme(self):
        return self.m_mediaCtrl12.Tell()

    def SetPause(self):
        self.m_mediaCtrl12.Pause()

    def GetState(self):
        State = self.m_mediaCtrl12.GetState()
        return State

    def SetLoad(self, film):
        self.m_mediaCtrl12.Load(film)

    def SetPlay(self):
        self.m_mediaCtrl12.Play()

    def SetStop(self):
        self.m_mediaCtrl12.Stop()


# Implementing MyFrame2 - Fenetre introduction
class MyFrame3(gui.MyFrame3):
    def __init__(self, parent):
        gui.MyFrame3.__init__(self, parent)

    def m_button5Activation(self, event):
        if self.m_textCtrl1.GetLineLength(0) == 5:
            self.m_button5.Enable()
        else:
            self.m_button5.Disable()

    def m_button5OnButtonClick(self, event):
        global Identifiant
        self.affichage = None
        Identifiant = self.m_textCtrl1.GetLineText(0)
        try:
            os.mkdir(Identifiant)
            if self.m_textCtrl1.GetLineLength(0) == 5:
                if not self.affichage:
                    self.affichage = MainFrame11(self)
                    self.affichage.Show()
                    self.Hide()
        except OSError:
            # print "Identifiant deja existant"

    def Iden(self):
        return Identifiant


# Application principale
class oneMinutePython(wx.App):
    def OnInit(self):
        self.m_frame = MyFrame3(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True


app = oneMinutePython(0)
app.MainLoop()
