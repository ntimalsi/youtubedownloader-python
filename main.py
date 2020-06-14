from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

#total size container
file_size=0

#for updating percentage...
def progress(stream, chunk, file_handle, remaining=None):
    #gets the percentage of the file that has been downloaded
    file_downloaded=(file_size - file_handle)
    per = float((file_downloaded / file_size) * 100)
    dBtn.config(text="{:00.0f} % Downloaded".format(per))

def startDownload():
    global file_size
    try:
        url=urlField.get()
        print(url)
        #changing button text
        dBtn.config(text='Please wait...')
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        # creating youtube object with url..
        ob = YouTube(url, on_progress_callback=progress)
        strm = ob.streams.first()
        file_size=strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        strm.download(path_to_save_video)
        print("done....")
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded successfully")
        urlField.delete(0, END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("Error!")

def startDownloadThread():
    #create thread...
    thread=Thread(target=startDownload)
    thread.start()

#starting gui building
main=Tk()

#setting the title
main.title("My Youtube Downloader")

#set the icon
main.iconbitmap('icon.ico')

main.geometry("600x600")

#heading icon
file=PhotoImage(file='youtube.png')
headingIcon=Label(main, image=file)
headingIcon.pack(side=TOP)

#url textfield
urlField=Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)

#download button
dBtn=Button(main, text="Start Download", font=("verdana", 18), relief='ridge', command=startDownloadThread)
dBtn.pack(side=TOP, pady=10)

#video title
vTitle=Label(main, text="video title")
#vTitle.pack(side=TOP)

main.mainloop()