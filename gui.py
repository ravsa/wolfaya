import pygtk,gtk
import time
import gobject
import urllib2 
import webkit
import pdfkit
class gui():
    _static=True
    _focus=True
    _first="https://www.google.com/search?client=ubuntu&channel=fs&q="
    _second="&ie=utf-8&oe=utf-8"
    _st1=0
    _prf=True
    _hist=True
    _js1,_js2="ON",'ON'
    _mv1,_mv2="OFF",'OFF'
    _tm1,_tm2="OFF",'OFF'
    _ig1,_ig2="OFF",'OFF'
    def __init__(self):
        self.main_window=gtk.Window()
        self.hist=open('history','a+')
        self.histbox=gtk.VBox()
        self.field=list(range(20))
        for i in range(20):
            self.field[i]=gtk.Entry()
            self.field[i].set_size_request(200,20)
            self.field[i].connect('activate',self.load_hist,i)
            self.histbox.pack_start(self.field[i],False)
        self.main_window.set_icon_from_file('images/wolfaya1.jpg')
        self.main_window.connect('destroy',self.exit)
        self.main_window.set_default_size(gtk.gdk.screen_width(),gtk.gdk.screen_height())
        self.wid=0

        self.settings1=webkit.WebSettings()
        self.settings2=webkit.WebSettings()
        self.website1="file:///home/ravsa/net.html"
        self.website2="file:///home/ravsa/net.html"
        self.progress1=gtk.ProgressBar()
        self.progress1.set_size_request(gtk.gdk.screen_width(),5)
        self.vbox1=gtk.VBox()
        self.menu_bar()
        self.horiz=gtk.VBox()
        self.tool_bar()
        self.side_window()
        self.side_action()
        self.hbox=gtk.HBox()
        self.hbox.pack_start(self.horiz,False)
        self.hbox.pack_start(self.histbox,False)
        self.view1=gtk.ScrolledWindow()
        self.view2=gtk.ScrolledWindow()

        self.view1_x=self.view1.get_hadjustment()
        self.view1_y=self.view1.get_vadjustment()
        self.view1_x.connect('value_changed',self.switch_win,1,1)
        self.view1_y.connect('value_changed',self.switch_win,1,1)

        self.view2_x=self.view2.get_hadjustment()
        self.view2_y=self.view2.get_vadjustment()
        self.view2_x.connect('value_changed',self.switch_win,2,2)
        self.view2_y.connect('value_changed',self.switch_win,2,2)

        self.main_window.add(self.vbox1)
        self.vbox1.pack_start(self.progress1,False)
        self.view1.set_border_width(1)
        self.web1=webkit.WebView()
        self.web1.open(self.website1)
        gobject.timeout_add(5,self.status)
        self.web1.connect('title-changed',self.title1)
        self.web1.connect('load-committed',self.load_page1)
        self.view1.add(self.web1)
        self.hbox.pack_start(self.view1,True)

        self.view2.set_border_width(1)
        self.web2=webkit.WebView()
        self.web2.open(self.website2)
        self.view2.add(self.web2)
        self.hbox.pack_start(self.view2,True)
        gobject.timeout_add(5,self.status)
        self.web2.connect('title-changed',self.title2)
        self.web2.connect('load-committed',self.load_page2)
        self.vbox1.pack_start(self.hbox)
        self.tool_actions()
        self.main_window.show_all()
        self.view2.hide()
        self.horiz.hide()
        self.histbox.hide()
        gtk.main()
    def load_hist(self,etc,etc1):
        url=self.field[etc1].get_text()
        if gui._focus:
            self.web1.open(url)
            self.address.set_text(url)
            gobject.timeout_add(5,self.status)
            self.write_history(url)
        else:
            self.web2.open(url)
            self.address2.set_text(url)
            gobject.timeout_add(5,self.status)
            self.write_history(url)
    def menu_bar(self):
        self.menubar=gtk.MenuBar()
        actiongroup=gtk.ActionGroup('Basegroup')
        file_action=gtk.Action('File','_File',None,None)
        actiongroup.add_action(file_action)
        file_menuitem=file_action.create_menu_item()        
        edit_action=gtk.Action('Edit','_Edit',None,None)
        actiongroup.add_action(edit_action)
        edit_menuitem=edit_action.create_menu_item()
        history_action=gtk.Action('History','_History',None,None)
        actiongroup.add_action(history_action)
        history_menuitem=history_action.create_menu_item()
        download_action=gtk.Action('Download','_Download',None,None)
        actiongroup.add_action(download_action)
        download_menuitem=download_action.create_menu_item()
        tool_action=gtk.Action('Tools','_Tools',None,None)
        actiongroup.add_action(tool_action)
        tool_menuitem=tool_action.create_menu_item()
        help_action=gtk.Action('Help','_Help',None,None)
        actiongroup.add_action(help_action)
        help_menuitem=help_action.create_menu_item()
        about_action=gtk.Action('About','_About',None,None)
        actiongroup.add_action(about_action)
        about_menuitem=about_action.create_menu_item()
        self.menubar.append(file_menuitem)
        self.menubar.append(edit_menuitem)
        self.menubar.append(history_menuitem)
        self.menubar.append(download_menuitem)
        self.menubar.append(tool_menuitem)
        self.menubar.append(help_menuitem)
        self.menubar.append(about_menuitem)
        self.menubar.show()
        self.vbox1.pack_start(self.menubar,False)
    def tool_bar(self):
        self.toolbox=gtk.HBox()
        self.split_image=gtk.Image()
        self.split_image.set_from_file('./images/split.jpg')
        self.spl_but=gtk.ToggleButton()
        self.spl_but.add(self.split_image)
        self.spl_but.set_size_request(30,30)
        self.forward=gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        self.pref=gtk.ToolButton(gtk.STOCK_PREFERENCES)
        self.backward=gtk.ToolButton(gtk.STOCK_GO_BACK)
        self.address=gtk.Entry()
        self.address.set_text("http://www.google.com")
        self.address2=gtk.Entry()
        self.address2.set_text("http://www.google.com")
        self.address2.set_size_request(0,0)
        self.address.set_size_request(640,27)
        self.refresh=gtk.ToolButton(gtk.STOCK_REFRESH)
        self.search=gtk.Entry()
        self.search.set_text("Search:wolfaya")
        self.search.set_size_request(180,27)
        self.toolbox.pack_start(self.pref,False)
        self.toolbox.pack_start(self.backward,False)
        self.toolbox.pack_start(self.forward,False)
        self.toolbox.pack_start(self.refresh,False)
        self.toolbox.pack_start(self.address,False)
        self.toolbox.pack_start(self.address2,False)
        self.toolbox.pack_start(self.search,True)
        self.toolbox.pack_start(self.spl_but,False)
        self.toolbox.show()
        self.vbox1.pack_start(self.toolbox,False)
    def get_update(self):
        if gui._focus:
            self._js=gui._js1
            self._tm=gui._tm1
            self._ig=gui._ig1
            self._mv=gui._mv1
            self.address2.modify_text(gtk.STATE_NORMAL,self.address2.get_colormap().alloc_color('light gray'))
            self.address.modify_text(gtk.STATE_NORMAL,self.address.get_colormap().alloc_color('black'))
        else:
            self._js=gui._js2
            self._tm=gui._tm2
            self._ig=gui._ig2
            self._mv=gui._mv2
            self.address.modify_text(gtk.STATE_NORMAL,self.address.get_colormap().alloc_color('light gray'))
            self.address2.modify_text(gtk.STATE_NORMAL,self.address2.get_colormap().alloc_color('black'))
        self.update_label()
    def set_update(self):
        if gui._focus:
            gui._js1=self._js
            gui._tm1=self._tm
            gui._ig1=self._ig
            gui._mv1=self._mv
        else:
            gui._js2=self._js
            gui._tm2=self._tm
            gui._ig2=self._ig
            gui._mv2=self._mv
        self.get_update()
    def switch_win(self,etc,code1,code2):

        if code2==1:
            gui._focus=True
            self.get_update()
        elif code2==2:
            gui._focus=False
            self.get_update()
    def side_window(self):
        self.js_con=gtk.HBox()
        self.js_lab=gtk.Label()
        self.js_lab.set_size_request(50,20)
        self.js_but=gtk.ToggleButton("JavaScript")
        self.js_but.set_active(True)
        self.js_but.set_size_request(100,27)
        self.js_con.pack_start(self.js_but,False)
        self.js_con.pack_start(self.js_lab,False)
        self.horiz.pack_start(self.js_con,False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.tm_con=gtk.HBox()
        self.tm_lab=gtk.Label()
        self.tm_lab.set_size_request(50,20)
        self.tm_but=gtk.ToggleButton("TextMode")
        self.tm_but.set_size_request(100,27)
        self.tm_con.pack_start(self.tm_but,False)
        self.tm_con.pack_start(self.tm_lab,False)
        self.horiz.pack_start(self.tm_con,False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.ig_con=gtk.HBox()
        self.ig_lab=gtk.Label()
        self.ig_lab.set_size_request(50,20)
        self.ig_but=gtk.ToggleButton("incognito")
        self.ig_but.set_size_request(100,27)
        self.ig_con.pack_start(self.ig_but,False)
        self.ig_con.pack_start(self.ig_lab,False)
        self.horiz.pack_start(self.ig_con,False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.mv_con=gtk.HBox()
        self.mv_lab=gtk.Label()
        self.mv_lab.set_size_request(50,20)
        self.mv_but=gtk.ToggleButton("MobileVeiw")
        self.mv_but.set_size_request(100,27)
        self.mv_con.pack_start(self.mv_but,False)
        self.mv_con.pack_start(self.mv_lab,False)
        self.horiz.pack_start(self.mv_con,False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.hst_but=gtk.Button("History")
        self.hst_but.set_size_request(150,30)
        self.horiz.pack_start(self.hst_but,False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.horiz.pack_start(gtk.HSeparator(),False)
        self.get_update()
    def update_label(self):
        self.js_lab.set_text(self._js)
        self.mv_lab.set_text(self._mv)
        self.ig_lab.set_text(self._ig)
        self.tm_lab.set_text(self._tm)
        if self._js == "ON" :
            self.js_but.set_active(True)
            self.js_lab.modify_fg(gtk.STATE_NORMAL,self.js_lab.get_colormap().alloc_color('green'))
        else:
            self.js_but.set_active(False)
            self.js_lab.modify_fg(gtk.STATE_NORMAL,self.js_lab.get_colormap().alloc_color('red'))

        if self._tm == 'ON':
            self.tm_but.set_active(True)
            self.tm_lab.modify_fg(gtk.STATE_NORMAL,self.tm_lab.get_colormap().alloc_color('green'))
        else:
            self.tm_but.set_active(False)
            self.tm_lab.modify_fg(gtk.STATE_NORMAL,self.tm_lab.get_colormap().alloc_color('red'))

        if self._mv == "ON":
            self.mv_but.set_active(True)
            self.mv_lab.modify_fg(gtk.STATE_NORMAL,self.mv_lab.get_colormap().alloc_color('green'))
        else:
            self.mv_but.set_active(False)
            self.mv_lab.modify_fg(gtk.STATE_NORMAL,self.mv_lab.get_colormap().alloc_color('red'))

        if self._ig == "ON":
            self.ig_but.set_active(True)
            self.ig_lab.modify_fg(gtk.STATE_NORMAL,self.ig_lab.get_colormap().alloc_color('green'))
        else:
            self.ig_but.set_active(False)
            self.ig_lab.modify_fg(gtk.STATE_NORMAL,self.ig_lab.get_colormap().alloc_color('red'))
         
    def side_action(self):
        self.js_but.connect('toggled',self.js_action)
        self.tm_but.connect('toggled',self.tm_action)
        self.mv_but.connect('toggled',self.mv_action)
        self.ig_but.connect('toggled',self.ig_action)
        self.hst_but.connect('clicked',self.show_history,'')
    def side_win_action(self,etc):
        def motion(self,condition):
            self.horiz.show()
            if condition:
                self.wid=self.wid+3
                self.horiz.set_size_request(self.wid,600)
                if self.wid >=170:
                    return False
                return True
            else:
                self.wid=self.wid-5
                if self.wid <= 0:
                    self.horiz.hide()
                    return False
                self.horiz.set_size_request(self.wid,600)
                return True
        if gui._prf:
            gobject.timeout_add(1,motion,self,True)
            gui._prf=False
        else:
            gobject.timeout_add(1,motion,self,False)
            gui._prf=True
    def tool_actions(self):
        self.pref.connect('clicked',self.side_win_action)
        self.spl_but.connect("clicked",self.cont2)
        self.backward.connect('clicked',self.back_q)
        self.forward.connect('clicked',self.forward_q)
        self.refresh.connect('clicked',self.refresh_old)
        self.address.connect('activate',self.goto1)
        self.address.connect('button_press_event',self.switch_win,1)
        self.address2.connect('activate',self.goto2)
        self.search.connect('activate',self.search_q)
        self.address2.connect('button_press_event',self.switch_win,2)
    def tm_action(self,etc):
        if self.tm_but.get_active():
            self._tm="ON"
            self.tm_lab.set_text(self._tm)
            self.set_update()
            if gui._focus:
                self.settings1.set_property('auto-load-images',False)
                self.web1.set_settings(self.settings1)
            else:
                self.settings2.set_property('auto-load-images',False)
                self.web2.set_settings(self.settings2)
        else:
            self._tm="OFF"
            self.tm_lab.set_text(self._tm)
            self.set_update()
            if gui._focus:
                self.settings1.set_property('auto-load-images',True)
                self.web1.set_settings(self.settings1)
            else:
                self.settings2.set_property('auto-load-images',True)
                self.web2.set_settings(self.settings2)
 
    def js_action(self,etc):
        if self.js_but.get_active():
            self._js='ON'
            self.js_lab.set_text(self._js)
            self.set_update()
            if gui._focus:
                self.settings1.set_property('enable-scripts',True)
                self.web1.set_settings(self.settings1)
            else:
                self.settings2.set_property('enable-scripts',True)
                self.web2.set_settings(self.settings2)
        else:
            self._js='OFF'
            self.js_lab.set_text(self._js)
            self.set_update()
            if gui._focus:
                self.settings1.set_property('enable-scripts',False)
                self.web1.set_settings(self.settings1)
            else:
                self.settings2.set_property('enable-scripts',False)
                self.web2.set_settings(self.settings2)

    def mv_action(self,etc):
        if self.mv_but.get_active():
            self._mv="ON"
            self.mv_lab.set_text(self._mv)
            self.set_update()
            if gui._focus:
                self.settings1.set_property('user-agent','Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/22.478; U; en) Presto/2.5.25 Version/10.54')
                self.web1.set_settings(self.settings1)
            else:
                self.settings2.set_property('user-agent','Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/22.478; U; en) Presto/2.5.25 Version/10.54')
                self.web2.set_settings(self.settings2)
                
        else:
            self._mv="OFF"
            self.mv_lab.set_text(self._mv)
            self.set_update()
            if gui._focus:
                self.settings2.set_property('user agent','Mozilla/30')
                self.web1.set_settings(self.settings2)
            else:
                self.settings2.set_property('user agent','Mozilla/30')
                self.web2.set_settings(self.settings2)


    def ig_action(self,etc):
        if self.ig_but.get_active():
            self._ig='ON'
            self.ig_lab.set_text(self._ig)
            self.set_update()
            if gui._focus:
                self.settings1.set_property('enable-private-browsing',True)
                self.web1.set_settings(self.settings1)
            else:
                self.settings2.set_property('enable-private-browsing',True)
                self.web2.set_settings(self.settings2)
        else:
            self._ig='OFF'
            self.ig_lab.set_text(self._ig)
            self.set_update()
            if gui._focus:
                self.settings1.set_property('enable-private-browsing',False)
                self.web1.set_settings(self.settings1)
            else:
                self.settings2.set_property('enable-private-browsing',False)
                self.web2.set_settings(self.settings2)


    def back_q(self,etc):
        if gui._focus:
            self.web1.go_back()
            gobject.timeout_add(5,self.status)
        else:
            self.web2.go_back()
            gobject.timeout_add(5,self.status)
    def forward_q(self,etc):
        if gui._focus:
            self.web1.go_forward()
        else:
            self.web2.go_forward()
    def refresh_old(self,etc):
        if gui._focus:
            self.web1.reload()
            gobject.timeout_add(5,self.status)
        else:
            self.web2.reload()
            gobject.timeout_add(5,self.status)

    def goto1(self,etc):
        gui._focus=True
        self.get_update()
        self.website1=self.address.get_text()
        if self.website1.startswith('http://') or self.website1.startswith('https://'):
           pass
        else:
           self.website1='http://'+self.website1
        self.address.set_text(self.website1)
        self.write_history(self.website1)
        self.web1.open(self.website1)
        gobject.timeout_add(5,self.status)
    def goto2(self,etc):
        gui._focus=False
        self.get_update()
        self.website2=self.address2.get_text()
        if self.website2.startswith('http://') or self.website2.startswith('https://'):
            pass
        else:
            self.website2='http://'+self.website2
        self.address2.set_text(self.website2)
        self.write_history(self.website2)
        self.web2.open(self.website2)
        gobject.timeout_add(5,self.status)

    def search_q(self,etc):
        self.search_me=self.search.get_text()
        self.search_me=gui._first+self.search_me.replace(' ','+')+gui._second
        if gui._focus:
            self.website1=self.search_me
            self.write_history(self.website1)
            self.web1.open(self.website1)
            gobject.timeout_add(5,self.status)
        else:
            self.website2=self.search_me
            self.write_history(self.website2)
            self.web2.open(self.website2)
            gobject.timeout_add(5,self.status)
    def title1(self,etc,frame,title):
        self.main_window.set_title(title)       
    def title2(self,etc,frame,title):
        self.main_window.set_title(title)        
    def load_page1(self,etc,page):
        uri=page.get_uri()
        self.address.set_text(uri)
    def load_page2(self,etc,page):
        uri=page.get_uri()
        self.address2.set_text(uri)
    def delta(self):
        if gui._static:
            self.address.set_size_request(300,26)
            self.address2.set_size_request(300,26)
            self.address.show() 
            self.address2.show()
        else:
            self.address.set_size_request(640,27)
            self.address2.set_size_request(0,0)
            self.address.show() 
            self.address2.show()
    def status(self):
        self.progress1.pulse()
        gui._st1=self.web1.get_progress()
        if gui._st1 == 0.0:
            gui._st1=0
            self.progress1.set_fraction(gui._st1)
            return False
        self.progress1.set_fraction(gui._st1)
        return True
    def cont2(self,etc):
        if gui._static:
            self.delta()
            gui._static=False
            self.view2.show()
            self.switch_win(2,2,2)
        else:
            self.switch_win(1,1,1)
            self.view2.hide()
            self.delta()
            gui._static=True
    def show_history(self,etc,col):
        if gui._hist:
            self.histbox.show()
            self.hist.seek(0,0)
            field=[]
            store=self.hist.read().split('#!#')
            store.reverse()
            store.remove('')
            count=0
            for i in store:
                if i != '' and count < 20:
                    self.field[count].set_text(str(i))
                    count+=1
            self.histbox.show()
            gui._hist=False
        else:
            gui._hist=True
            self.histbox.hide()
    def write_history(self,url):
        self.hist.write(url+'#!#')
        self.hist.flush()
    def exit(self,etc):
        self.hist.close()
        gtk.main_quit()




if __name__=='__main__':
    start=gui()
