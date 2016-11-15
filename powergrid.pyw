import Tkinter as tk
import subprocess
import im_dat

class PowerGrid:

    def __init__(self, root):

        self.root = root

        # have to keep references to the images else they get garbage collected
        self.swapuser = tk.PhotoImage(data=im_dat.swapuser)
        self.logoff = tk.PhotoImage(data=im_dat.logoff)
        self.hibernate = tk.PhotoImage(data=im_dat.hibernate)
        self.shutdown = tk.PhotoImage(data=im_dat.shutdown)

        self.b1 = tk.Button(root, background="black", image=self.swapuser,
                            command=self._swapuser)
        self.b2 = tk.Button(root, background="black", activebackground="white", image=self.logoff,
                            command=self._logoff)
        self.b3 = tk.Button(root, background="black", image=self.hibernate,
                            command=self._hibernate)
        self.b4 = tk.Button(root, background="black", image=self.shutdown,
                            command=self._shutdown)

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=1, column=0)
        self.b4.grid(row=1, column=1)
# http://www.blog.pythonlibrary.org/2010/03/27/restarting-pcs-with-python/

    def _swapuser(self):
        import win32ts
        win32ts.WTSDisconnectSession(0, -1, False)
        self.root.quit()

    def _hibernate(self):
        #subprocess.Popen("rundll32 powrprof.dll,SetSuspendState Hibernate")
        try:
            subprocess.Popen("shutdown /h")
        finally:
            self.root.quit()

    def _logoff(self):
        try:
            subprocess.Popen("shutdown /l")
        finally:
            self.root.quit()

    def _shutdown(self):
        try:
            subprocess.Popen("shutdown /p")
        finally:
            self.root.quit()

root = tk.Tk()

pg = PowerGrid(root)

root.mainloop()

