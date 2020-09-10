#wxmychat-0.2.py
import wx
import time

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = "wanx Chat",
                         size = (520,450),
                         pos = (800,300))
        
        panel = wx.Panel(frame,-1)
        labelAll = wx.StaticText(panel,-1,'All Contents',
                                 pos = (210,5))
        self.textAll = wx.TextCtrl(panel,-1,
                                   size = (480,200),
                                   pos = (10,30),
                                   style = wx.TE_READONLY|wx.TE_MULTILINE)
        
        labelIn = wx.StaticText(panel,-1,'I Say',
                                pos = (230,230))
        self.textIn = wx.TextCtrl(panel,-1,
                                  size = (480,100),
                                  pos = (10,260),
                                  style = wx.TE_MULTILINE)
        
        self.buttonSent = wx.Button(panel,-1,"Sent",
                                    size = (75,25),
                                    pos = (175,370))
        self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.buttonSent)
        self.buttonCLear = wx.Button(panel,-1,"Clear",size = (75,25),pos = (260,370))
        self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.buttonCLear)
        
    
        frame.Show()
        return True
    
    def OnButtonSent(self,event):
        userinput = self.textin.GetValue()
        self.textIn.Clear()
        nowtime = time.ctime()
        inmsg = "You (%s) :\n%s \n"%(nowtime,userinput)
        self.textAll.AppendText(inmsg)
        
    def OnButtonClear(self,event):
        self.textAll.Clear()
    
if __name__ ==" __main__":
    app = MyApp()
    app.MainLoop()
