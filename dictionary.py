from tkinter import Entry, StringVar, Button , Tk
from tkinter.ttk import Label

window = Tk()
window.geometry("600x250")
window.title('Igbo Dictionary')

entry_text = Entry(window)
entry_text.pack()

result=StringVar()
result_label = Label(window,textvariable=result)
result_label.pack()

Igbo_dict = {
    'bia' : 'come' ,
    'anu' : 'meat' ,
    'oyi' : 'cold' ,
    'iko' : 'cup' ,
    'mmiri' : 'water' ,
    'ntutu' : 'hair' ,
    'chi' : 'God' ,
    'kedu' : 'How are you' ,
    'Ulo' : 'house' ,
    'Ego' : 'money' ,
    'Akpu' : 'cassava fufu' ,
    'ututu' : 'morning' ,
    'ahu' : 'body' ,
    'obi' : 'heart/soul/mind' ,
    'ike' : 'strength/power' ,
    'udo' : 'peace' ,
    'aka' : 'hand' ,
    'oru' : 'work' ,
    'ebe' : 'place/location' ,
    'okike' : 'creation/nature' ,
    'uwa' : 'world' ,
    'aku' : 'wealth / riches'


}


def search(word):
    if word in Igbo_dict:
        result.set(Igbo_dict[word])
        print(Igbo_dict[word])

    else:
        result.set('Not Found')


search_btn = Button(window, text='Search', command= lambda : search(entry_text.get()))
search_btn.pack()


#run the application
window.mainloop()