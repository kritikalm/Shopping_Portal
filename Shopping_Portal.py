from Tkinter import *
from tkMessageBox import *

root = Tk()
root.configure(bg='black')
root.geometry('465x278')
root.title("SHOPPING PORTAL")
Label(root, text="NAME:", font='Calibri 15 bold', bg='black', foreground='magenta').grid(row=0, column=0, sticky='w')
Label(root, text="KRITIKA SINGH", font='Calibri 15 bold italic', bg='black', foreground='orange').grid(row=0, column=1,
                                                                                                       sticky='e')
Label(root, text="BATCH:", font='Calibri 15 bold', foreground='magenta', bg='black').grid(row=1, column=0, sticky='w')
Label(root, text="B3 (BX)", font='Calibri 15 bold italic', foreground='orange', bg='black').grid(row=1, column=1,
                                                                                                 sticky='e')
Label(root, text="ENROLLMENT NUMBER:", font='Calibri 15 bold', foreground='magenta', bg='black').grid(row=2, column=0,
                                                                                                      sticky='w')
Label(root, text="151311", font='Calibri 15 bold italic', foreground='orange', bg='black').grid(row=2, column=1,
                                                                                                sticky='e')
Label(root, text="SEMESTER:", font='calibri 15 bold', foreground='magenta', bg='black').grid(row=3, column=0,
                                                                                             sticky='w')
Label(root, text="III SEM", font='calibri 15 bold', foreground='orange', bg='black').grid(row=3, column=1, sticky='e')
Label(root, text="YEAR:", font='calibri 15 bold', foreground='magenta', bg='black').grid(row=4, column=0, sticky='w')
Label(root, text="2nd YR.", font='calibri 15 bold', fg='orange', bg='black').grid(row=4, column=1, sticky='e')
Label(root, text="EMAIL:", font='calibri 15 bold', fg='magenta', bg='black').grid(row=5, column=0, sticky='w')
Label(root, text="kritikasingh.97.lm@gmail.com", font='calibri 15 bold', fg='orange', bg='black').grid(row=5, column=1,
                                                                                                       sticky='e')
Label(root, text="PROJECT:", font='calibri 15 bold', fg='magenta', bg='black').grid(row=6, column=0, sticky='w')
Label(root, text="SHOPPING PORTAL", font='calibri 15 bold', fg='orange', bg='black').grid(row=6, column=1, sticky='e')


def fun():
    root.destroy()
    rt = Tk()
    rt.title("SHOPAHOLIC")
    rt.configure(bg='black')

    def fun1():
        rt.destroy()
        rtk = Tk()
        rtk.title("SHOPAHOLIC-WOMEN")
        rtk.configure(bg='lightgoldenrod1')
        Label(rtk, text="WOMEN's CATEGORY", font='arial 20 italic underline bold', bg='lightgoldenrod1',
              fg='orange red').grid(row=0, column=5)
        Label(rtk, text="CLOTHES:", font='arial 15 bold', fg='orange red', bg='lightgoldenrod1').grid(row=3, column=0,
                                                                                                      sticky='w')

        def clothes():
            rtk.destroy()
            clo = Tk()
            global total
            clo.title("SHOPAHOLIC-WOMEN-CLOTHES")
            clo.configure(bg='peachpuff')
            Label(clo, text="WOMEN's CATEGORY", font='arial 25 italic underline bold', fg='maroon',
                  bg='peachpuff').grid(row=0, column=0, columnspan=5, sticky='ewns')
            Label(clo, text="CLOTHES:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=3, column=0,
                                                                                                    sticky='w')

            def dresses():
                v1 = IntVar()
                v2 = IntVar()
                v3 = IntVar()

                def mini():
                    Label(clo, text="Rs.2500", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=6, column=2,
                                                                                                       sticky='e')

                def partydress():
                    Label(clo, text="Rs3159", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=6, column=3,
                                                                                                      sticky='e')

                def maxidress():
                    Label(clo, text="Rs.4000", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=6, column=4,
                                                                                                       sticky='e')

                Checkbutton(clo, text="Mini dresses", font='arial 10 bold', fg='orange red', bg='peachpuff',
                            variable=v1, onvalue=2500, command=mini).grid(row=4, column=2, sticky='e')
                Checkbutton(clo, text="Party dresses", font='arial 10 bold', fg='orange red', bg='peachpuff',
                            variable=v2, onvalue=3159, command=partydress).grid(row=4, column=3, sticky='e')
                Checkbutton(clo, text="Maxi dresses", font='arial 10 bold', fg='orange red', bg='peachpuff',
                            variable=v3, onvalue=4000, command=maxidress).grid(row=4, column=4, sticky='e')

                img = PhotoImage(file="mini.gif")
                Label(clo, image=img).grid(row=5, column=2, sticky='e')
                img1 = PhotoImage(file="party.gif")
                Label(clo, image=img1).grid(row=5, column=3, sticky='e')
                img2 = PhotoImage(file="maxi.gif")
                Label(clo, image=img2).grid(row=5, column=4, sticky='e')

                def total1(a, b, c):
                    total1 = (a + b + c)
                    Label(clo, text=total1, font='arial 15 bold', fg='black', bg='peachpuff').grid(row=4, column=6,
                                                                                                   sticky='w')

                Button(clo, text="Total Amount for Dresses", font='arial 10 bold', fg='black', bg='peachpuff',
                       command=lambda: total1(v1.get(), v2.get(), v3.get())).grid(row=4, column=5, sticky='w')
                mainloop()

            def tops():
                v4 = IntVar()
                v5 = IntVar()
                v6 = IntVar()

                def tshirt():
                    Label(clo, text="Rs.750", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=9, column=2,
                                                                                                      sticky='e')

                def croptops():
                    Label(clo, text="Rs.965", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=9, column=3,
                                                                                                      sticky='e')

                def partytops():
                    Label(clo, text="Rs.1000", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=9, column=4,
                                                                                                       sticky='e')

                Checkbutton(clo, text="T-Shirts", font='arial 10 bold', fg='orange red', bg='peachpuff', variable=v4,
                            onvalue=750, command=tshirt).grid(row=7, column=2, sticky='w')
                Checkbutton(clo, text="Crop tops", font='arial 10 bold', fg='orange red', bg='peachpuff', variable=v5,
                            onvalue=965, command=croptops).grid(row=7, column=3, sticky='w')
                Checkbutton(clo, text="Party Tops", font='arial 10 bold', fg='orange red', bg='peachpuff', variable=v6,
                            onvalue=1000, command=partytops).grid(row=7, column=4, sticky='w')
                img3 = PhotoImage(file="tshirt.gif")
                Label(clo, image=img3).grid(row=8, column=2, sticky='e')
                img4 = PhotoImage(file="crop.gif")
                Label(clo, image=img4).grid(row=8, column=3, sticky='e')
                img5 = PhotoImage(file="topparty.gif")
                Label(clo, image=img5).grid(row=8, column=4, sticky='e')

                def total2(d, e, f):
                    total2 = (d + e + f)
                    Label(clo, text=total2, font='arial 15 bold', fg='black', bg='peachpuff').grid(row=7, column=6)

                Button(clo, text="Total Amount for Tshirts", font='arial 10 bold', fg='black', bg='peachpuff',
                       command=lambda: total2(v4.get(), v5.get(), v6.get())).grid(row=7, column=5, sticky='w')
                mainloop()

            def jeans():
                v7 = IntVar()
                v8 = IntVar()
                v9 = IntVar()

                def jea():
                    Label(clo, text="RS.1450", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=12, column=2,
                                                                                                       sticky='e')

                def shorts():
                    Label(clo, text="Rs.1200", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=12, column=3,
                                                                                                       sticky='e')

                def skirts():
                    Label(clo, text="Rs.1300", font='arial 15 bold', fg='purple', bg='peachpuff').grid(row=12, column=4,
                                                                                                       sticky='e')

                Checkbutton(clo, text="Jeans", font='arial 10 bold', fg='orange red', bg='peachpuff', command=jea,
                            variable=v7, onvalue=1450).grid(row=10, column=2, sticky='w')
                Checkbutton(clo, text="Shorts", font='arial 10 bold', fg='orange red', bg='peachpuff', command=shorts,
                            variable=v8, onvalue=1200).grid(row=10, column=3, sticky='w')
                Checkbutton(clo, text="Skirts", font='arial 10 bold', fg='orange red', bg='peachpuff', command=skirts,
                            variable=v9, onvalue=1300).grid(row=10, column=4, sticky='w')
                img6 = PhotoImage(file="dungaree.gif")
                Label(clo, image=img6).grid(row=11, column=2, sticky='e')
                img7 = PhotoImage(file="shorts.gif")
                Label(clo, image=img7).grid(row=11, column=3, sticky='e')
                img8 = PhotoImage(file="skirt.gif")
                Label(clo, image=img8).grid(row=11, column=4, sticky='e')

                def total3(g, h, i):
                    total3 = (g + h + i)
                    Label(clo, text=total3, font='arial 15 bold', fg='black', bg='peachpuff').grid(row=10, column=6)

                Button(clo, text="Total Amount for Jeans", font='arial 10 bold', fg='black', bg='peachpuff',
                       command=lambda: total3(v7.get(), v8.get(), v9.get())).grid(row=10, column=5, sticky='w')
                mainloop()

            Button(clo, text="DRESSES:", font='arial 15 bold', fg='orange red', bg='peachpuff', command=dresses).grid(
                row=4, column=0, sticky='w')
            Button(clo, text="TOPS & TEES:", font='arial 15 bold', fg='orange red', bg='peachpuff', command=tops).grid(
                row=7, column=0, sticky='w')
            Button(clo, text="JEANS & SKIRTS:", font='arial 15 bold', fg='orange red', bg='peachpuff',
                   command=jeans).grid(row=10, column=0, sticky='w')
            Label(clo, text="NOTE-To uncheck any option click again on its category.", font='arial 15 bold', fg='black',
                  bg='peachpuff').grid(row=15, column=0, sticky='w')

            def proceed():
                clo.destroy()
                pro = Tk()
                pro.title("CHECKOUT")
                pro.configure(bg='peachpuff')
                Label(pro, text="CHECKOUT", font='arial 25 italic underline bold', fg='maroon', bg='peachpuff').grid(
                    row=0, column=0, columnspan=5, sticky='ewns')
                Label(pro, text="SHIPPING ADDRESS:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=3,
                                                                                                                 column=0,
                                                                                                                 sticky='w')
                Label(pro, text="First Name", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=4,
                                                                                                          column=0,
                                                                                                          sticky='w')
                e = Entry(font='arial 15 bold')
                e.grid(row=4, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Last Name:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=6,
                                                                                                          column=0,
                                                                                                          sticky='w')
                f = Entry(font='arial 15 bold')
                f.grid(row=6, column=3, columnspan=43, sticky='ewns')
                Label(pro, text="Email:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=8, column=0,
                                                                                                      sticky='w')
                g = Entry(font='arial 15 bold')
                g.grid(row=8, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Address Line 1:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=10,
                                                                                                               column=0,
                                                                                                               sticky='w')
                h = Entry(font='arial 15 bold')
                h.grid(row=10, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="City:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=12, column=0,
                                                                                                     sticky='w')
                i = Entry(font='arial 15 bold')
                i.grid(row=12, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="State:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=14, column=0,
                                                                                                      sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=14, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Pincode:", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=16,
                                                                                                        column=0,
                                                                                                        sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=16, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="DEBIT CARD NUMBER", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=17,
                                                                                                                 column=0,
                                                                                                                 sticky='w')
                a = Entry(font='arial 15 bold')
                a.grid(row=18, column=0)
                Label(pro, text="CVV", font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=19, column=0,
                                                                                                   sticky='w')
                b = Entry(font='arial 15 bold')
                b.grid(row=20, column=0)

                def showinfo():
                    if (
                                                    a.get() == '' or b.get() == '' or e.get() == '' or f.get() == '' or g.get() == '' or h.get() == '' or i.get() == '' or j.get() == ''):
                        c = "Please fill all the columns then proceed"
                        showerror("WARNING", c)
                    else:
                        mess = Tk()
                        mess.title("PAYMENT DONE")
                        mess.configure(bg='peachpuff')
                        Label(mess, text="Payment Done", font='arial 30 bold', fg='orange red', bg='peachpuff').grid()

                        def sub():
                            mess.destroy()
                            sub = Tk()
                            sub.title("RECEIPT")
                            sub.configure(bg='peachpuff')
                            Label(sub, text="RECEIPT", font='arial 30 bold', fg='orange red', bg='peachpuff').grid(
                                row=0, column=5)
                            Label(sub, text='Name: ' + e.get() + f.get(), font='arial 20 bold', fg='orange red',
                                  bg='peachpuff').grid(row=2, column=5)
                            Label(sub, text='Email: ' + g.get(), font='arial 20 bold', fg='orange red',
                                  bg='peachpuff').grid(row=3, column=5)
                            Label(sub, text='Address: ' + h.get() + ',' + i.get() + ',' + j.get(), font='arial 20 bold',
                                  fg='orange red', bg='peachpuff').grid(row=4, column=5)
                            Label(sub, text="Thanks for Shopping from SHOPAHOLIC", font='arial 20 bold',
                                  fg='orange red', bg='peachpuff').grid(row=5, column=5)
                            Label(sub, text="Your Order will be delivered within 7 business days.HAVE A NICE DAY",
                                  font='arial 20 bold', fg='orange red', bg='peachpuff').grid(row=6, column=5)

                            def exi():
                                pro.destroy()
                                sub.destroy()

                            Button(sub, text="Exit", font='arial 20 bold', fg='orange red', bg='lawn green',
                                   command=exi).grid(row=7, column=5)

                        Button(mess, text="Proceed to receipt", font='arial 30 bold', fg='orange red', bg='lawn green',
                               command=sub).grid()

                Button(pro, text="PAY", font='arial 20 bold', fg='orange red', bg='lawn green', command=showinfo).grid(
                    row=21, column=5)

            Button(clo, text="Proceed to CheckOut", font='arial 15 bold', fg='orange red', bg='lawn green',
                   command=proceed).grid(row=20, column=5, sticky='ewns')
            Label(clo, text="If don't want to buy anything exit", font='arial 15 bold', fg='black',
                  bg='peachpuff').grid(row=19, column=0, sticky='w')
            Button(clo, text="EXIT", font='arial 15 bold', fg='orange red', bg='lawn green', command=clo.destroy).grid(
                row=20, column=0, sticky='w')
            mainloop()

        Button(rtk, text="select", font='arial 15 bold', fg='black', bg='red2', bd=6, command=clothes).grid(row=3,
                                                                                                            column=7,
                                                                                                            sticky='e')
        Label(rtk, text="FOOTWEAR:", font='arial 15 bold', fg='orange red', bg='lightgoldenrod1').grid(row=4, column=0,
                                                                                                       sticky='w')

        def footwear():
            rtk.destroy()
            clo = Tk()
            global total
            clo.title("SHOPAHOLIC-WOMEN-FOOTWEAR")
            clo.configure(bg='dark slate grey')
            Label(clo, text="WOMEN's CATEGORY", font='arial 25 italic underline bold', fg='green yellow',
                  bg='dark slate grey').grid(row=0, column=0, columnspan=5, sticky='ewns')
            Label(clo, text="FOOTWEAR:", font='arial 20 bold', fg='cyan', bg='dark slate grey').grid(row=3, column=0,
                                                                                                     sticky='w')

            def heels():
                v1 = IntVar()
                v2 = IntVar()
                v3 = IntVar()

                def wedges():
                    Label(clo, text="Rs.1500", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=6, column=2, sticky='e')

                def boots():
                    Label(clo, text="Rs1200", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(row=6,
                                                                                                                  column=3,
                                                                                                                  sticky='e')

                def stiletto():
                    Label(clo, text="Rs.1270", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=6, column=4, sticky='e')

                Checkbutton(clo, text="Wedges", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v1, onvalue=1500, command=wedges).grid(row=4, column=2, sticky='w')
                Checkbutton(clo, text="Boots", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v2, onvalue=1200, command=boots).grid(row=4, column=3, sticky='w')
                Checkbutton(clo, text="Stiletto", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v3, onvalue=1270, command=stiletto).grid(row=4, column=4, sticky='w')

                img = PhotoImage(file="wedges.gif")
                Label(clo, image=img).grid(row=5, column=2, sticky='e')
                img1 = PhotoImage(file="boots.gif")
                Label(clo, image=img1).grid(row=5, column=3, sticky='e')
                img2 = PhotoImage(file="stiletto.gif")
                Label(clo, image=img2).grid(row=5, column=4, sticky='e')

                def total1(a, b, c):
                    total1 = (a + b + c)
                    Label(clo, text=total1, font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(row=4,
                                                                                                                column=6,
                                                                                                                sticky='w')

                Button(clo, text="Total Amount for Heels", font='arial 10 bold', fg='black', bg='aquamarine',
                       command=lambda: total1(v1.get(), v2.get(), v3.get())).grid(row=4, column=5, sticky='w')
                mainloop()

            def shoes():
                v4 = IntVar()
                v5 = IntVar()
                v6 = IntVar()

                def casual():
                    Label(clo, text="Rs.1000", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=9, column=2, sticky='e')

                def sneakers():
                    Label(clo, text="Rs.1320", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=9, column=3, sticky='e')

                def sports():
                    Label(clo, text="Rs.2000", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=9, column=4, sticky='e')

                Checkbutton(clo, text="Casual Shoes", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v4, onvalue=1000, command=casual).grid(row=7, column=2, sticky='w')
                Checkbutton(clo, text="Sneakers", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v5, onvalue=1320, command=sneakers).grid(row=7, column=3, sticky='w')
                Checkbutton(clo, text="Sports Shoes", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v6, onvalue=2000, command=sports).grid(row=7, column=4, sticky='w')
                img3 = PhotoImage(file="casual.gif")
                Label(clo, image=img3).grid(row=8, column=2, sticky='e')
                img4 = PhotoImage(file="sneakers.gif")
                Label(clo, image=img4).grid(row=8, column=3, sticky='e')
                img5 = PhotoImage(file="sports.gif")
                Label(clo, image=img5).grid(row=8, column=4, sticky='e')

                def total2(d, e, f):
                    total2 = (d + e + f)
                    Label(clo, text=total2, font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(row=7,
                                                                                                                column=6)

                Button(clo, text="Total Amount for Shoes", font='arial 10 bold', fg='black', bg='aquamarine',
                       command=lambda: total2(v4.get(), v5.get(), v6.get())).grid(row=7, column=5, sticky='w')
                mainloop()

            def sandals():
                v7 = IntVar()
                v8 = IntVar()
                v9 = IntVar()

                def flipflop():
                    Label(clo, text="RS.750", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=12, column=2, sticky='e')

                def flats():
                    Label(clo, text="Rs.1250", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=12, column=3, sticky='e')

                def strappy():
                    Label(clo, text="Rs.1120", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=12, column=4, sticky='e')

                Checkbutton(clo, text="Flip-Flops", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            command=flipflop, variable=v7, onvalue=750).grid(row=10, column=2, sticky='w')
                Checkbutton(clo, text="Flats", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            command=flats, variable=v8, onvalue=1250).grid(row=10, column=3, sticky='w')
                Checkbutton(clo, text="Bellies", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            command=strappy, variable=v9, onvalue=1120).grid(row=10, column=4, sticky='w')
                img6 = PhotoImage(file="flipflop.gif")
                Label(clo, image=img6).grid(row=11, column=2, sticky='e')
                img7 = PhotoImage(file="flats.gif")
                Label(clo, image=img7).grid(row=11, column=3, sticky='e')
                img8 = PhotoImage(file="belly.gif")
                Label(clo, image=img8).grid(row=11, column=4, sticky='e')

                def total3(g, h, i):
                    total3 = (g + h + i)
                    Label(clo, text=total3, font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(row=10,
                                                                                                                column=6)

                Button(clo, text="Total Amount for Sandals", font='arial 10 bold', fg='black', bg='aquamarine',
                       command=lambda: total3(v7.get(), v8.get(), v9.get())).grid(row=10, column=5, sticky='w')
                mainloop()

            Button(clo, text="HEELS:", font='arial 15 bold', fg='green yellow', bg='dark slate grey',
                   command=heels).grid(row=4, column=0, sticky='w')
            Button(clo, text="SHOES:", font='arial 15 bold', fg='green yellow', bg='dark slate grey',
                   command=shoes).grid(row=7, column=0, sticky='w')
            Button(clo, text="SANDALS:", font='arial 15 bold', fg='green yellow', bg='dark slate grey',
                   command=sandals).grid(row=10, column=0, sticky='w')
            Label(clo, text="NOTE-To uncheck any option click again on its category.", font='arial 15 bold',
                  fg='green yellow', bg='dark slate grey').grid(row=15, column=0, sticky='w')

            def proceed():
                clo.destroy()
                pro = Tk()
                pro.title("CHECKOUT")
                pro.configure(bg='dark slate grey')
                Label(pro, text="CHECKOUT", font='arial 25 italic underline bold', fg='green yellow',
                      bg='dark slate grey').grid(row=0, column=0, columnspan=5, sticky='ewns')
                Label(pro, text="SHIPPING ADDRESS:", font='arial 20 bold', fg='green yellow',
                      bg='dark slate grey').grid(row=3, column=0, sticky='w')
                Label(pro, text="First Name", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=4,
                                                                                                                  column=0,
                                                                                                                  sticky='w')
                e = Entry(font='arial 15 bold')
                e.grid(row=4, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Last Name:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=6,
                                                                                                                  column=0,
                                                                                                                  sticky='w')
                f = Entry(font='arial 15 bold')
                f.grid(row=6, column=3, columnspan=43, sticky='ewns')
                Label(pro, text="Email:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=8,
                                                                                                              column=0,
                                                                                                              sticky='w')
                g = Entry(font='arial 15 bold')
                g.grid(row=8, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="ADDRESS Line 1:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(
                    row=10, column=0, sticky='w')
                h = Entry(font='arial 15 bold')
                h.grid(row=10, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="City:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=12,
                                                                                                             column=0,
                                                                                                             sticky='w')
                i = Entry(font='arial 15 bold')
                i.grid(row=12, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="State:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=14,
                                                                                                              column=0,
                                                                                                              sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=14, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Pincode:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=16,
                                                                                                                column=0,
                                                                                                                sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=16, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="DEBIT CARD NUMBER", font='arial 20 bold', fg='green yellow',
                      bg='dark slate grey').grid(row=17, column=0, sticky='w')
                a = Entry(font='arial 15 bold')
                a.grid(row=18, column=0)
                Label(pro, text="CVV", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=19,
                                                                                                           column=0,
                                                                                                           sticky='w')
                b = Entry(font='arial 15 bold')
                b.grid(row=20, column=0)

                def showinfo():
                    if (
                                                    a.get() == '' or b.get() == '' or e.get() == '' or f.get() == '' or g.get() == '' or h.get() == '' or i.get() == '' or j.get() == ''):
                        c = "Please fill all the columns then proceed"
                        showerror("WARNING", c)
                    else:
                        mess = Tk()
                        mess.title("PAYMENT DONE")
                        mess.configure(bg='dark slate grey')
                        Label(mess, text="Payment Done", font='arial 30 bold', fg='green yellow',
                              bg='dark slate grey').grid()

                        def sub():
                            mess.destroy()
                            sub = Tk()
                            sub.title("RECEIPT")
                            sub.configure(bg='dark slate grey')
                            Label(sub, text="RECEIPT", font='arial 30 bold', fg='green yellow',
                                  bg='dark slate grey').grid(row=0, column=5)
                            Label(sub, text='Name: ' + e.get() + f.get(), font='arial 20 bold', fg='green yellow',
                                  bg='dark slate grey').grid(row=2, column=5)
                            Label(sub, text='Email: ' + g.get(), font='arial 20 bold', fg='green yellow',
                                  bg='dark slate grey').grid(row=3, column=5)
                            Label(sub, text='Address: ' + h.get() + ',' + i.get() + ',' + j.get(), font='arial 20 bold',
                                  fg='green yellow', bg='dark slate grey').grid(row=4, column=5)
                            Label(sub, text="Thanks for Shopping from SHOPAHOLIC", font='arial 20 bold',
                                  fg='green yellow', bg='dark slate grey').grid(row=5, column=5)
                            Label(sub, text="Your Order will be delivered within 7 business days.HAVE A NICE DAY",
                                  font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=6, column=5)

                            def exi():
                                pro.destroy()
                                sub.destroy()

                            Button(sub, text="Exit", font='arial 20 bold', fg='orange red', bg='lawn green',
                                   command=exi).grid(row=7, column=5)

                        Button(mess, text="Proceed to receipt", font='arial 30 bold', fg='orange red', bg='lawn green',
                               command=sub).grid()

                Button(pro, text="PAY", font='arial 20 bold', fg='orange red', bg='lawn green', command=showinfo).grid(
                    row=21, column=5)

            Button(clo, text="Proceed to CheckOut", font='arial 15 bold', fg='orange red', bg='lawn green',
                   command=proceed).grid(row=20, column=5, sticky='ewns')
            Label(clo, text="If don't want to buy anything exit", font='arial 15 bold', fg='green yellow',
                  bg='dark slate grey').grid(row=19, column=0, sticky='w')
            Button(clo, text="EXIT", font='arial 15 bold', fg='orange red', bg='lawn green', command=clo.destroy).grid(
                row=20, column=0, sticky='w')
            mainloop()

        Button(rtk, text="select", font='arial 15 bold', fg='black', bg='red2', bd=6, command=footwear).grid(row=4,
                                                                                                             column=7,
                                                                                                             sticky='e')

        def accessories():
            rtk.destroy()
            clo = Tk()
            global total
            clo.title("SHOPAHOLIC-WOMEN-ACCESORIES")
            clo.configure(bg='spring green2')
            Label(clo, text="WOMEN's CATEGORY", font='arial 25 italic underline bold', fg='deep pink',
                  bg='spring green2').grid(row=0, column=0, columnspan=5, sticky='ewns')
            Label(clo, text="ACCESSORIES:", font='arial 20 bold', fg='magenta4', bg='spring green2').grid(row=3,
                                                                                                          column=0,
                                                                                                          sticky='w')

            def acess():
                v1 = IntVar()
                v2 = IntVar()
                v3 = IntVar()

                def bags():
                    Label(clo, text="Rs.3650", font='arial 15 bold', fg='deep pink', bg='spring green2').grid(row=6,
                                                                                                              column=2,
                                                                                                              sticky='e')

                def necklace():
                    Label(clo, text="Rs.1450", font='arial 15 bold', fg='deep pink', bg='spring green2').grid(row=6,
                                                                                                              column=3,
                                                                                                              sticky='e')

                def earing():
                    Label(clo, text="Rs.875", font='arial 15 bold', fg='deep pink', bg='spring green2').grid(row=6,
                                                                                                             column=4,
                                                                                                             sticky='e')

                def watch():
                    Label(clo, text="Rs.5490", font='arial 15 bold', fg='deep pink', bg='spring green2').grid(row=9,
                                                                                                              column=2,
                                                                                                              sticky='e')

                def belts():
                    Label(clo, text="Rs.4890", font='arial 15 bold', fg='deep pink', bg='spring green2').grid(row=9,
                                                                                                              column=3,
                                                                                                              sticky='e')

                def scarf():
                    Label(clo, text="Rs.2000", font='arial 15 bold', fg='deep pink', bg='spring green2').grid(row=9,
                                                                                                              column=4,
                                                                                                              sticky='e')

                v4 = IntVar()
                v5 = IntVar()
                v6 = IntVar()
                Checkbutton(clo, text="Bags", font='arial 10 bold', fg='deep pink', bg='spring green2', variable=v1,
                            onvalue=3650, command=bags).grid(row=4, column=2, sticky='w')
                Checkbutton(clo, text="Necklace", font='arial 10 bold', fg='deep pink', bg='spring green2', variable=v2,
                            onvalue=1450, command=necklace).grid(row=4, column=3, sticky='w')
                Checkbutton(clo, text="Earings", font='arial 10 bold', fg='deep pink', bg='spring green2', variable=v3,
                            onvalue=875, command=earing).grid(row=4, column=4, sticky='w')

                img = PhotoImage(file="bag.gif")
                Label(clo, image=img).grid(row=5, column=2, sticky='e')
                img1 = PhotoImage(file="necklace.gif")
                Label(clo, image=img1).grid(row=5, column=3, sticky='e')
                img2 = PhotoImage(file="earing.gif")
                Label(clo, image=img2).grid(row=5, column=4, sticky='e')

                Checkbutton(clo, text="Watches", font='arial 10 bold', fg='deep pink', bg='spring green2', variable=v4,
                            onvalue=5490, command=watch).grid(row=7, column=2, sticky='w')
                Checkbutton(clo, text="Belts", font='arial 10 bold', fg='deep pink', bg='spring green2', variable=v5,
                            onvalue=4890, command=belts).grid(row=7, column=3, sticky='w')
                Checkbutton(clo, text="Scarves", font='arial 10 bold', fg='deep pink', bg='spring green2', variable=v6,
                            onvalue=2000, command=scarf).grid(row=7, column=4, sticky='w')
                img3 = PhotoImage(file="watch.gif")
                Label(clo, image=img3).grid(row=8, column=2, sticky='e')
                img4 = PhotoImage(file="belt.gif")
                Label(clo, image=img4).grid(row=8, column=3, sticky='e')
                img5 = PhotoImage(file="scarf.gif")
                Label(clo, image=img5).grid(row=8, column=4, sticky='e')

                def total1(a, b, c, d, e, f):
                    total1 = (a + b + c + d + e + f)
                    Label(clo, text=total1, font='arial 15 bold', fg='deep pink', bg='spring green2').grid(row=4,
                                                                                                           column=6,
                                                                                                           sticky='w')

                Button(clo, text="Total Amount for Accesories", font='arial 10 bold', fg='antique white', bg='magenta4',
                       command=lambda: total1(v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get())).grid(row=4,
                                                                                                                column=5,
                                                                                                                sticky='w')
                mainloop()

            Button(clo, text="ACCESSORIES:", font='arial 15 bold', fg='deep pink', bg='spring green2',
                   command=acess).grid(row=4, column=0, sticky='w')
            Label(clo, text="NOTE-To uncheck any option click again on its category.", font='arial 15 bold',
                  fg='deep pink', bg='spring green2').grid(row=15, column=0, sticky='w')

            def proceed():
                clo.destroy()
                pro = Tk()
                pro.title("CHECKOUT")
                pro.configure(bg='spring green2')
                Label(pro, text="CHECKOUT", font='arial 25 italic underline bold', fg='deep pink',
                      bg='spring green2').grid(row=0, column=0, columnspan=5, sticky='ewns')
                Label(pro, text="SHIPPING ADDRESS:", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(
                    row=3, column=0, sticky='w')
                Label(pro, text="First Name", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=4,
                                                                                                             column=0,
                                                                                                             sticky='w')
                e = Entry(font='arial 15 bold')
                e.grid(row=4, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Last Name:", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=6,
                                                                                                             column=0,
                                                                                                             sticky='w')
                f = Entry(font='arial 15 bold')
                f.grid(row=6, column=3, columnspan=43, sticky='ewns')
                Label(pro, text="Email:", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=8,
                                                                                                         column=0,
                                                                                                         sticky='w')
                g = Entry(font='arial 15 bold')
                g.grid(row=8, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Address Line 1:", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(
                    row=10, column=0, sticky='w')
                h = Entry(font='arial 15 bold')
                h.grid(row=10, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="City:", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=12,
                                                                                                        column=0,
                                                                                                        sticky='w')
                i = Entry(font='arial 15 bold')
                i.grid(row=12, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="State:", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=14,
                                                                                                         column=0,
                                                                                                         sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=14, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Pincode:", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=16,
                                                                                                           column=0,
                                                                                                           sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=16, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="DEBIT CARD NUMBER", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(
                    row=17, column=0, sticky='w')
                a = Entry(font='arial 15 bold')
                a.grid(row=18, column=0)
                Label(pro, text="CVV", font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=19, column=0,
                                                                                                      sticky='w')
                b = Entry(font='arial 15 bold')
                b.grid(row=20, column=0)

                def showinfo():
                    if (
                                                    a.get() == '' or b.get() == '' or e.get() == '' or f.get() == '' or g.get() == '' or h.get() == '' or i.get() == '' or j.get() == ''):
                        c = "Please fill all the columns then proceed"
                        showerror("WARNING", c)
                    else:
                        mess = Tk()
                        mess.title("PAYMENT DONE")
                        mess.configure(bg='spring green2')
                        Label(mess, text="Payment Done", font='arial 30 bold', fg='deep pink',
                              bg='spring green2').grid()

                        def sub():
                            mess.destroy()
                            sub = Tk()
                            sub.title("RECEIPT")
                            sub.configure(bg='spring green2')
                            Label(sub, text="RECEIPT", font='arial 30 bold', fg='deep pink', bg='spring green2').grid(
                                row=0, column=5)
                            Label(sub, text='Name: ' + e.get() + f.get(), font='arial 20 bold', fg='deep pink',
                                  bg='spring green2').grid(row=2, column=5)
                            Label(sub, text='Email: ' + g.get(), font='arial 20 bold', fg='deep pink',
                                  bg='spring green2').grid(row=3, column=5)
                            Label(sub, text='Address: ' + h.get() + ',' + i.get() + ',' + j.get(), font='arial 20 bold',
                                  fg='deep pink', bg='spring green2').grid(row=4, column=5)
                            Label(sub, text="Thanks for Shopping from SHOPAHOLIC", font='arial 20 bold', fg='deep pink',
                                  bg='spring green2').grid(row=5, column=5)
                            Label(sub, text="Your Order will be delivered within 7 business days.HAVE A NICE DAY",
                                  font='arial 20 bold', fg='deep pink', bg='spring green2').grid(row=6, column=5)

                            def exi():
                                pro.destroy()
                                sub.destroy()

                            Button(sub, text="Exit", font='arial 20 bold', fg='orange red', bg='lawn green',
                                   command=exi).grid(row=7, column=5)

                        Button(mess, text="Proceed to receipt", font='arial 30 bold', fg='orange red', bg='lawn green',
                               command=sub).grid()

                Button(pro, text="PAY", font='arial 20 bold', fg='orange red', bg='lawn green', command=showinfo).grid(
                    row=21, column=5)

            Button(clo, text="Proceed to CheckOut", font='arial 15 bold', fg='orange red', bg='lawn green',
                   command=proceed).grid(row=20, column=5, sticky='ewns')
            Label(clo, text="If don't want to buy anything exit", font='arial 15 bold', fg='deep pink',
                  bg='spring green2').grid(row=19, column=0, sticky='w')
            Button(clo, text="EXIT", font='arial 15 bold', fg='orange red', bg='lawn green', command=clo.destroy).grid(
                row=20, column=0, sticky='w')
            mainloop()

        Label(rtk, text="ACCESORIES:", font='arial 15 bold', fg='orange red', bg='lightgoldenrod1').grid(row=5,
                                                                                                         column=0,
                                                                                                         sticky='w')
        Button(rtk, text="select", font='arial 15 bold', fg='black', bg='red2', bd=6, command=accessories).grid(row=5,
                                                                                                                column=7,
                                                                                                                sticky='e')

    def fun2():
        rt.destroy()
        rtm = Tk()
        rtm.title("SHOPAHOLIC-MEN")
        rtm.configure(bg='mint cream')
        Label(rtm, text="MEN's CATEGORY", font='arial 20 italic bold underline', fg='midnight blue',
              bg='mint cream').grid(row=0, column=5)
        Label(rtm, text="CLOTHES:", font='arial 15 bold', fg='midnight blue', bg='mint cream').grid(row=3, column=0,
                                                                                                    sticky='w')

        def clothes():
            rtm.destroy()
            clo = Tk()
            global total
            clo.title("SHOPAHOLIC-MEN-CLOTHES")
            clo.configure(bg='dodger blue')
            Label(clo, text="MEN's CATEGORY", font='arial 25 italic underline bold', fg='midnight blue',
                  bg='dodger blue').grid(row=0, column=0, columnspan=5, sticky='ewns')
            Label(clo, text="CLOTHES:", font='arial 20 bold', fg='black', bg='dodger blue').grid(row=3, column=0,
                                                                                                 sticky='w')

            def suits():
                v1 = IntVar()
                v2 = IntVar()
                v3 = IntVar()

                def halfcoat():
                    Label(clo, text="Rs.3500", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=6, column=2,
                                                                                                        sticky='e')

                def doublesuit():
                    Label(clo, text="Rs7500", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=6, column=3,
                                                                                                       sticky='e')

                def tuxedo():
                    Label(clo, text="Rs.15000", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=6,
                                                                                                         column=4,
                                                                                                         sticky='e')

                Checkbutton(clo, text="Half Coat", font='arial 10 bold', fg='midnight blue', bg='dodger blue',
                            variable=v1, onvalue=3500, command=halfcoat).grid(row=4, column=2, sticky='e')
                Checkbutton(clo, text="Double Breasted Suit", font='arial 10 bold', fg='midnight blue',
                            bg='dodger blue', variable=v2, onvalue=7500, command=doublesuit).grid(row=4, column=3,
                                                                                                  sticky='e')
                Checkbutton(clo, text="Tuxedo", font='arial 10 bold', fg='midnight blue', bg='dodger blue', variable=v3,
                            onvalue=15000, command=tuxedo).grid(row=4, column=4, sticky='e')

                img = PhotoImage(file="halfcoat.gif")
                Label(clo, image=img).grid(row=5, column=2, sticky='e')
                img1 = PhotoImage(file="doublesuit.gif")
                Label(clo, image=img1).grid(row=5, column=3, sticky='e')
                img2 = PhotoImage(file="tuxedo.gif")
                Label(clo, image=img2).grid(row=5, column=4, sticky='e')

                def total1(a, b, c):
                    total1 = (a + b + c)
                    Label(clo, text=total1, font='arial 15 bold', fg='black', bg='dodger blue').grid(row=4, column=6,
                                                                                                     sticky='w')

                Button(clo, text="Total Amount for Suits", font='arial 10 bold', fg='black', bg='dodger blue',
                       command=lambda: total1(v1.get(), v2.get(), v3.get())).grid(row=4, column=5, sticky='w')
                mainloop()

            def tshirtss():
                v4 = IntVar()
                v5 = IntVar()
                v6 = IntVar()

                def tshirt():
                    Label(clo, text="Rs.1000", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=9, column=2,
                                                                                                        sticky='e')

                def shirts():
                    Label(clo, text="Rs.1230", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=9, column=3,
                                                                                                        sticky='e')

                def sweats():
                    Label(clo, text="Rs.950", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=9, column=4,
                                                                                                       sticky='e')

                Checkbutton(clo, text="T-Shirts", font='arial 10 bold', fg='midnight blue', bg='dodger blue',
                            variable=v4, onvalue=1000, command=tshirt).grid(row=7, column=2, sticky='w')
                Checkbutton(clo, text="Shirts", font='arial 10 bold', fg='midnight blue', bg='dodger blue', variable=v5,
                            onvalue=1230, command=shirts).grid(row=7, column=3, sticky='w')
                Checkbutton(clo, text="Sweatshirt", font='arial 10 bold', fg='midnight blue', bg='dodger blue',
                            variable=v6, onvalue=950, command=sweats).grid(row=7, column=4, sticky='w')
                img3 = PhotoImage(file="tshirtmen.gif")
                Label(clo, image=img3).grid(row=8, column=2, sticky='e')
                img4 = PhotoImage(file="shirtmen.gif")
                Label(clo, image=img4).grid(row=8, column=3)
                img5 = PhotoImage(file="sweats.gif")
                Label(clo, image=img5).grid(row=8, column=4, sticky='e')

                def total2(d, e, f):
                    total2 = (d + e + f)
                    Label(clo, text=total2, font='arial 15 bold', fg='black', bg='dodger blue').grid(row=7, column=6)

                Button(clo, text="Total Amount for Tshirts", font='arial 10 bold', fg='black', bg='dodger blue',
                       command=lambda: total2(v4.get(), v5.get(), v6.get())).grid(row=7, column=5, sticky='w')
                mainloop()

            def jeans():
                v7 = IntVar()
                v8 = IntVar()
                v9 = IntVar()

                def jea():
                    Label(clo, text="RS.2540", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=12,
                                                                                                        column=2,
                                                                                                        sticky='e')

                def shorts():
                    Label(clo, text="Rs.1287", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=12,
                                                                                                        column=3,
                                                                                                        sticky='e')

                def jackets():
                    Label(clo, text="Rs.4500", font='arial 15 bold', fg='black', bg='dodger blue').grid(row=12,
                                                                                                        column=4,
                                                                                                        sticky='e')

                Checkbutton(clo, text="Jeans", font='arial 10 bold', fg='midnight blue', bg='dodger blue', command=jea,
                            variable=v7, onvalue=2540).grid(row=10, column=2, sticky='w')
                Checkbutton(clo, text="Shorts", font='arial 10 bold', fg='midnight blue', bg='dodger blue',
                            command=shorts, variable=v8, onvalue=1287).grid(row=10, column=3, sticky='w')
                Checkbutton(clo, text="Jackets", font='arial 10 bold', fg='midnight blue', bg='dodger blue',
                            command=jackets, variable=v9, onvalue=4500).grid(row=10, column=4, sticky='w')
                img6 = PhotoImage(file="jeansmen.gif")
                Label(clo, image=img6).grid(row=11, column=2, sticky='e')
                img7 = PhotoImage(file="shortsmen.gif")
                Label(clo, image=img7).grid(row=11, column=3)
                img8 = PhotoImage(file="jackets.gif")
                Label(clo, image=img8).grid(row=11, column=4, sticky='e')

                def total3(g, h, i):
                    total3 = (g + h + i)
                    Label(clo, text=total3, font='arial 15 bold', fg='black', bg='dodger blue').grid(row=10, column=6)

                Button(clo, text="Total Amount for Jeans", font='arial 10 bold', fg='black', bg='dodger blue',
                       command=lambda: total3(v7.get(), v8.get(), v9.get())).grid(row=10, column=5, sticky='w')
                mainloop()

            Button(clo, text="SUITS:", font='arial 15 bold', fg='white', bg='dodger blue', command=suits).grid(row=4,
                                                                                                               column=0,
                                                                                                               sticky='w')
            Button(clo, text="TSHIRTS & TEES:", font='arial 15 bold', fg='white', bg='dodger blue',
                   command=tshirtss).grid(row=7, column=0, sticky='w')
            Button(clo, text="JEANS & JACKETS:", font='arial 15 bold', fg='white', bg='dodger blue',
                   command=jeans).grid(row=10, column=0, sticky='w')
            Label(clo, text="NOTE-To uncheck any option click again on its category.", font='arial 15 bold', fg='black',
                  bg='dodger blue').grid(row=15, column=0, sticky='w')

            def proceed():
                clo.destroy()
                pro = Tk()
                pro.title("CHECKOUT")
                pro.configure(bg='dodger blue')
                Label(pro, text="CHECKOUT", font='arial 25 italic underline bold', fg='maroon', bg='dodger blue').grid(
                    row=0, column=0, columnspan=5, sticky='ewns')
                Label(pro, text="SHIPPING ADDRESS:", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(
                    row=3, column=0, sticky='w')
                Label(pro, text="First Name", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=4,
                                                                                                               column=0,
                                                                                                               sticky='w')
                e = Entry(font='arial 15 bold')
                e.grid(row=4, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Last Name:", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=6,
                                                                                                               column=0,
                                                                                                               sticky='w')
                f = Entry(font='arial 15 bold')
                f.grid(row=6, column=3, columnspan=43, sticky='ewns')
                Label(pro, text="Email:", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=8,
                                                                                                           column=0,
                                                                                                           sticky='w')
                g = Entry(font='arial 15 bold')
                g.grid(row=8, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Address Line 1:", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(
                    row=10, column=0, sticky='w')
                h = Entry(font='arial 15 bold')
                h.grid(row=10, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="City:", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=12,
                                                                                                          column=0,
                                                                                                          sticky='w')
                i = Entry(font='arial 15 bold')
                i.grid(row=12, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="State:", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=14,
                                                                                                           column=0,
                                                                                                           sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=14, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Pincode:", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=16,
                                                                                                             column=0,
                                                                                                             sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=16, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="DEBIT CARD NUMBER", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(
                    row=17, column=0, sticky='w')
                a = Entry(font='arial 15 bold')
                a.grid(row=18, column=0)
                Label(pro, text="CVV", font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=19,
                                                                                                        column=0,
                                                                                                        sticky='w')
                b = Entry(font='arial 15 bold')
                b.grid(row=20, column=0)

                def showinfo():
                    if (
                                                    a.get() == '' or b.get() == '' or e.get() == '' or f.get() == '' or g.get() == '' or h.get() == '' or i.get() == '' or j.get() == ''):
                        c = "Please fill all the columns then proceed"
                        showerror("WARNING", c)
                    else:
                        mess = Tk()
                        mess.title("PAYMENT DONE")
                        mess.configure(bg='dodger blue')
                        Label(mess, text="Payment Done", font='arial 30 bold', fg='midnight blue',
                              bg='dodger blue').grid()

                        def sub():
                            mess.destroy()
                            sub = Tk()
                            sub.title("RECEIPT")
                            sub.configure(bg='dodger blue')
                            Label(sub, text="RECEIPT", font='arial 30 bold', fg='midnight blue', bg='dodger blue').grid(
                                row=0, column=5)
                            Label(sub, text='Name: ' + e.get() + f.get(), font='arial 20 bold', fg='midnight blue',
                                  bg='dodger blue').grid(row=2, column=5)
                            Label(sub, text='Email: ' + g.get(), font='arial 20 bold', fg='midnight blue',
                                  bg='dodger blue').grid(row=3, column=5)
                            Label(sub, text='Address: ' + h.get() + ',' + i.get() + ',' + j.get(), font='arial 20 bold',
                                  fg='midnight blue', bg='dodger blue').grid(row=4, column=5)
                            Label(sub, text="Thanks for Shopping from SHOPAHOLIC", font='arial 20 bold',
                                  fg='midnight blue', bg='dodger blue').grid(row=5, column=5)
                            Label(sub, text="Your Order will be delivered within 7 business days.HAVE A NICE DAY",
                                  font='arial 20 bold', fg='midnight blue', bg='dodger blue').grid(row=6, column=5)

                            def exi():
                                pro.destroy()
                                sub.destroy()

                            Button(sub, text="Exit", font='arial 20 bold', fg='midnight blue', bg='lawn green',
                                   command=exi).grid(row=7, column=5)

                        Button(mess, text="Proceed to receipt", font='arial 30 bold', fg='orange red', bg='lawn green',
                               command=sub).grid()

                Button(pro, text="PAY", font='arial 20 bold', fg='orange red', bg='lawn green', command=showinfo).grid(
                    row=21, column=5)

            Button(clo, text="Proceed to CheckOut", font='arial 15 bold', fg='orange red', bg='lawn green',
                   command=proceed).grid(row=20, column=5, sticky='ewns')
            Label(clo, text="If don't want to buy anything exit", font='arial 15 bold', fg='black',
                  bg='dodger blue').grid(row=19, column=0, sticky='w')
            Button(clo, text="EXIT", font='arial 15 bold', fg='orange red', bg='lawn green', command=clo.destroy).grid(
                row=20, column=0, sticky='w')
            mainloop()

        Button(rtm, text="select", font='arial 15 bold', fg='navy blue', bg='black', bd=6, command=clothes).grid(row=3,
                                                                                                                 column=7,
                                                                                                                 sticky='e')
        Label(rtm, text="FOOTWEAR:", font='arial 15 bold', fg='midnight blue', bg='mint cream').grid(row=4, column=0,
                                                                                                     sticky='w')

        def footwear():
            rtm.destroy()
            clo = Tk()
            global total
            clo.title("SHOPAHOLIC-MEN-FOOTWEAR")
            clo.configure(bg='dark slate grey')
            Label(clo, text="MEN's CATEGORY", font='arial 25 italic underline bold', fg='green yellow',
                  bg='dark slate grey').grid(row=0, column=0, columnspan=5, sticky='ewns')
            Label(clo, text="FOOTWEAR:", font='arial 20 bold', fg='cyan', bg='dark slate grey').grid(row=3, column=0,
                                                                                                     sticky='w')

            def shoes():
                v4 = IntVar()
                v5 = IntVar()
                v6 = IntVar()

                def casual():
                    Label(clo, text="Rs.2500", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=9, column=2, sticky='e')

                def sneakers():
                    Label(clo, text="Rs.2300", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=9, column=3, sticky='e')

                def formal():
                    Label(clo, text="Rs.5620", font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(
                        row=9, column=4, sticky='e')

                Checkbutton(clo, text="Casual Shoes", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v4, onvalue=2500, command=casual).grid(row=7, column=2, sticky='w')
                Checkbutton(clo, text="Sneakers", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v5, onvalue=2300, command=sneakers).grid(row=7, column=3, sticky='w')
                Checkbutton(clo, text="Formal Shoes", font='arial 10 bold', fg='green yellow', bg='dark slate grey',
                            variable=v6, onvalue=5620, command=formal).grid(row=7, column=4, sticky='w')
                img3 = PhotoImage(file="casualmen.gif")
                Label(clo, image=img3).grid(row=8, column=2, sticky='e')
                img4 = PhotoImage(file="sneakermen.gif")
                Label(clo, image=img4).grid(row=8, column=3, sticky='e')
                img5 = PhotoImage(file="shoes.gif")
                Label(clo, image=img5).grid(row=8, column=4, sticky='e')

                def total2(d, e, f):
                    total2 = (d + e + f)
                    Label(clo, text=total2, font='arial 15 bold', fg='green yellow', bg='dark slate grey').grid(row=7,
                                                                                                                column=6)

                Button(clo, text="Total Amount for Shoes", font='arial 10 bold', fg='black', bg='aquamarine',
                       command=lambda: total2(v4.get(), v5.get(), v6.get())).grid(row=7, column=5, sticky='w')
                mainloop()

            Button(clo, text="SHOES:", font='arial 15 bold', fg='green yellow', bg='dark slate grey',
                   command=shoes).grid(row=4, column=0, sticky='w')
            Label(clo, text="NOTE-To uncheck any option click again on its category.", font='arial 15 bold',
                  fg='green yellow', bg='dark slate grey').grid(row=15, column=0, sticky='w')

            def proceed():
                clo.destroy()
                pro = Tk()
                pro.title("CHECKOUT")
                pro.configure(bg='dark slate grey')
                Label(pro, text="CHECKOUT", font='arial 25 italic underline bold', fg='green yellow',
                      bg='dark slate grey').grid(row=0, column=0, columnspan=5, sticky='ewns')
                Label(pro, text="SHIPPING ADDRESS:", font='arial 20 bold', fg='green yellow',
                      bg='dark slate grey').grid(row=3, column=0, sticky='w')
                Label(pro, text="First Name", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=4,
                                                                                                                  column=0,
                                                                                                                  sticky='w')
                e = Entry(font='arial 15 bold')
                e.grid(row=4, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Last Name:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=6,
                                                                                                                  column=0,
                                                                                                                  sticky='w')
                f = Entry(font='arial 15 bold')
                f.grid(row=6, column=3, columnspan=43, sticky='ewns')
                Label(pro, text="Email:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=8,
                                                                                                              column=0,
                                                                                                              sticky='w')
                g = Entry(font='arial 15 bold')
                g.grid(row=8, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="ADDRESS Line 1:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(
                    row=10, column=0, sticky='w')
                h = Entry(font='arial 15 bold')
                h.grid(row=10, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="City:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=12,
                                                                                                             column=0,
                                                                                                             sticky='w')
                i = Entry(font='arial 15 bold')
                i.grid(row=12, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="State:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=14,
                                                                                                              column=0,
                                                                                                              sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=14, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Pincode:", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=16,
                                                                                                                column=0,
                                                                                                                sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=16, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="DEBIT CARD NUMBER", font='arial 20 bold', fg='green yellow',
                      bg='dark slate grey').grid(row=17, column=0, sticky='w')
                a = Entry(font='arial 15 bold')
                a.grid(row=18, column=0)
                Label(pro, text="CVV", font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=19,
                                                                                                           column=0,
                                                                                                           sticky='w')
                b = Entry(font='arial 15 bold')
                b.grid(row=20, column=0)

                def showinfo():
                    if (
                                                    a.get() == '' or b.get() == '' or e.get() == '' or f.get() == '' or g.get() == '' or h.get() == '' or i.get() == '' or j.get() == ''):
                        c = "Please fill all the columns then proceed"
                        showerror("WARNING", c)
                    else:
                        mess = Tk()
                        mess.title("PAYMENT DONE")
                        mess.configure(bg='dark slate grey')
                        Label(mess, text="Payment Done", font='arial 30 bold', fg='green yellow',
                              bg='dark slate grey').grid()

                        def sub():
                            mess.destroy()
                            sub = Tk()
                            sub.title("RECEIPT")
                            sub.configure(bg='dark slate grey')
                            Label(sub, text="RECEIPT", font='arial 30 bold', fg='green yellow',
                                  bg='dark slate grey').grid(row=0, column=5)
                            Label(sub, text='Name: ' + e.get() + f.get(), font='arial 20 bold', fg='green yellow',
                                  bg='dark slate grey').grid(row=2, column=5)
                            Label(sub, text='Email: ' + g.get(), font='arial 20 bold', fg='green yellow',
                                  bg='dark slate grey').grid(row=3, column=5)
                            Label(sub, text='Address: ' + h.get() + ',' + i.get() + ',' + j.get(), font='arial 20 bold',
                                  fg='green yellow', bg='dark slate grey').grid(row=4, column=5)
                            Label(sub, text="Thanks for Shopping from SHOPAHOLIC", font='arial 20 bold',
                                  fg='green yellow', bg='dark slate grey').grid(row=5, column=5)
                            Label(sub, text="Your Order will be delivered within 7 business days.HAVE A NICE DAY",
                                  font='arial 20 bold', fg='green yellow', bg='dark slate grey').grid(row=6, column=5)

                            def exi():
                                pro.destroy()
                                sub.destroy()

                            Button(sub, text="Exit", font='arial 20 bold', fg='orange red', bg='lawn green',
                                   command=exi).grid(row=7, column=5)

                        Button(mess, text="Proceed to receipt", font='arial 30 bold', fg='orange red', bg='lawn green',
                               command=sub).grid()

                Button(pro, text="PAY", font='arial 20 bold', fg='orange red', bg='lawn green', command=showinfo).grid(
                    row=21, column=5)

            Button(clo, text="Proceed to CheckOut", font='arial 15 bold', fg='orange red', bg='lawn green',
                   command=proceed).grid(row=20, column=5, sticky='ewns')
            Label(clo, text="If don't want to buy anything exit", font='arial 15 bold', fg='green yellow',
                  bg='dark slate grey').grid(row=19, column=0, sticky='w')
            Button(clo, text="EXIT", font='arial 15 bold', fg='orange red', bg='lawn green', command=clo.destroy).grid(
                row=20, column=0, sticky='w')
            mainloop()

        Button(rtm, text="select", font='arial 15 bold', fg='navy blue', bg='black', bd=6, command=footwear).grid(row=4,
                                                                                                                  column=7,
                                                                                                                  sticky='e')

        def accessories():
            rtm.destroy()
            clo = Tk()
            global total
            clo.title("SHOPAHOLIC-MEN-ACCESORIES")
            clo.configure(bg='black')
            Label(clo, text="MEN's CATEGORY", font='arial 25 italic underline bold', fg='deep pink', bg='black').grid(
                row=0, column=0, columnspan=5, sticky='ewns')
            Label(clo, text="ACCESSORIES:", font='arial 20 bold', fg='magenta4', bg='black').grid(row=3, column=0,
                                                                                                  sticky='w')

            def acess():
                v1 = IntVar()
                v2 = IntVar()
                v3 = IntVar()

                def wallet():
                    Label(clo, text="Rs.4501", font='arial 15 bold', fg='deep pink', bg='black').grid(row=9, column=1,
                                                                                                      sticky='e')

                def watch():
                    Label(clo, text="Rs.8452", font='arial 15 bold', fg='deep pink', bg='black').grid(row=9, column=2,
                                                                                                      sticky='e')

                def belts():
                    Label(clo, text="Rs.5600", font='arial 15 bold', fg='deep pink', bg='black').grid(row=9, column=3,
                                                                                                      sticky='e')

                def scarf():
                    Label(clo, text="Rs.1400", font='arial 15 bold', fg='deep pink', bg='black').grid(row=9, column=4,
                                                                                                      sticky='e')

                v4 = IntVar()
                v5 = IntVar()
                v6 = IntVar()
                Checkbutton(clo, text="Wallets", font='arial 10 bold', fg='deep pink', bg='black', variable=v1,
                            onvalue=4501, command=wallet).grid(row=7, column=1, sticky='w')
                Checkbutton(clo, text="Watches", font='arial 10 bold', fg='deep pink', bg='black', variable=v4,
                            onvalue=8452, command=watch).grid(row=7, column=2, sticky='w')
                Checkbutton(clo, text="Belts", font='arial 10 bold', fg='deep pink', bg='black', variable=v5,
                            onvalue=5600, command=belts).grid(row=7, column=3, sticky='w')
                Checkbutton(clo, text="Scarves", font='arial 10 bold', fg='deep pink', bg='black', variable=v6,
                            onvalue=1400, command=scarf).grid(row=7, column=4, sticky='w')
                img2 = PhotoImage(file="wallet.gif")
                Label(clo, image=img2).grid(row=8, column=1)
                img3 = PhotoImage(file="watchmen.gif")
                Label(clo, image=img3).grid(row=8, column=2, sticky='e')
                img4 = PhotoImage(file="beltmen.gif")
                Label(clo, image=img4).grid(row=8, column=3, sticky='e')
                img5 = PhotoImage(file="scarfmen.gif")
                Label(clo, image=img5).grid(row=8, column=4, sticky='e')

                def total1(a, b, c, d):
                    total1 = (a + b + c + d)
                    Label(clo, text=total1, font='arial 15 bold', fg='deep pink', bg='black').grid(row=4, column=6,
                                                                                                   sticky='w')

                Button(clo, text="Total Amount for Accesories", font='arial 10 bold', fg='antique white', bg='magenta4',
                       command=lambda: total1(v1.get(), v2.get(), v3.get(), v4.get())).grid(row=4, column=5, sticky='w')
                mainloop()

            Button(clo, text="ACCESSORIES:", font='arial 15 bold', fg='deep pink', bg='black', command=acess).grid(
                row=4, column=0, sticky='w')
            Label(clo, text="NOTE-To uncheck any option click again on its category.", font='arial 15 bold',
                  fg='deep pink', bg='black').grid(row=15, column=0, sticky='w')

            def proceed():
                clo.destroy()
                pro = Tk()
                pro.title("CHECKOUT")
                pro.configure(bg='black')
                Label(pro, text="CHECKOUT", font='arial 25 italic underline bold', fg='deep pink', bg='black').grid(
                    row=0, column=0, columnspan=5, sticky='ewns')
                Label(pro, text="SHIPPING ADDRESS:", font='arial 20 bold', fg='deep pink', bg='black').grid(row=3,
                                                                                                            column=0,
                                                                                                            sticky='w')
                Label(pro, text="First Name", font='arial 20 bold', fg='deep pink', bg='black').grid(row=4, column=0,
                                                                                                     sticky='w')
                e = Entry(font='arial 15 bold')
                e.grid(row=4, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Last Name:", font='arial 20 bold', fg='deep pink', bg='black').grid(row=6, column=0,
                                                                                                     sticky='w')
                f = Entry(font='arial 15 bold')
                f.grid(row=6, column=3, columnspan=43, sticky='ewns')
                Label(pro, text="Email:", font='arial 20 bold', fg='deep pink', bg='black').grid(row=8, column=0,
                                                                                                 sticky='w')
                g = Entry(font='arial 15 bold')
                g.grid(row=8, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Address Line 1:", font='arial 20 bold', fg='deep pink', bg='black').grid(row=10,
                                                                                                          column=0,
                                                                                                          sticky='w')
                h = Entry(font='arial 15 bold')
                h.grid(row=10, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="City:", font='arial 20 bold', fg='deep pink', bg='black').grid(row=12, column=0,
                                                                                                sticky='w')
                i = Entry(font='arial 15 bold')
                i.grid(row=12, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="State:", font='arial 20 bold', fg='deep pink', bg='black').grid(row=14, column=0,
                                                                                                 sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=14, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="Pincode:", font='arial 20 bold', fg='deep pink', bg='black').grid(row=16, column=0,
                                                                                                   sticky='w')
                j = Entry(font='arial 15 bold')
                j.grid(row=16, column=3, columnspan=4, sticky='ewns')
                Label(pro, text="DEBIT CARD NUMBER", font='arial 20 bold', fg='deep pink', bg='black').grid(row=17,
                                                                                                            column=0,
                                                                                                            sticky='w')
                a = Entry(font='arial 15 bold')
                a.grid(row=18, column=0)
                Label(pro, text="CVV", font='arial 20 bold', fg='deep pink', bg='black').grid(row=19, column=0,
                                                                                              sticky='w')
                b = Entry(font='arial 15 bold')
                b.grid(row=20, column=0)

                def showinfo():
                    if (
                                                    a.get() == '' or b.get() == '' or e.get() == '' or f.get() == '' or g.get() == '' or h.get() == '' or i.get() == '' or j.get() == ''):
                        c = "Please fill all the columns then proceed"
                        showerror("WARNING", c)
                    else:
                        mess = Tk()
                        mess.title("PAYMENT DONE")
                        mess.configure(bg='black')
                        Label(mess, text="Payment Done", font='arial 30 bold', fg='deep pink', bg='black').grid()

                        def sub():
                            mess.destroy()
                            sub = Tk()
                            sub.title("RECEIPT")
                            sub.configure(bg='black')
                            Label(sub, text="RECEIPT", font='arial 30 bold', fg='deep pink', bg='black').grid(row=0,
                                                                                                              column=5)
                            Label(sub, text='Name: ' + e.get() + f.get(), font='arial 20 bold', fg='deep pink',
                                  bg='black').grid(row=2, column=5)
                            Label(sub, text='Email: ' + g.get(), font='arial 20 bold', fg='deep pink', bg='black').grid(
                                row=3, column=5)
                            Label(sub, text='Address: ' + h.get() + ',' + i.get() + ',' + j.get(), font='arial 20 bold',
                                  fg='deep pink', bg='black').grid(row=4, column=5)
                            Label(sub, text="Thanks for Shopping from SHOPAHOLIC", font='arial 20 bold', fg='deep pink',
                                  bg='black').grid(row=5, column=5)
                            Label(sub, text="Your Order will be delivered within 7 business days.HAVE A NICE DAY",
                                  font='arial 20 bold', fg='deep pink', bg='black').grid(row=6, column=5)

                            def exi():
                                pro.destroy()
                                sub.destroy()

                            Button(sub, text="Exit", font='arial 20 bold', fg='orange red', bg='lawn green',
                                   command=exi).grid(row=7, column=5)

                        Button(mess, text="Proceed to receipt", font='arial 30 bold', fg='orange red', bg='lawn green',
                               command=sub).grid()

                Button(pro, text="PAY", font='arial 20 bold', fg='orange red', bg='lawn green', command=showinfo).grid(
                    row=21, column=5)

            Button(clo, text="Proceed to CheckOut", font='arial 15 bold', fg='orange red', bg='lawn green',
                   command=proceed).grid(row=20, column=5, sticky='ewns')
            Label(clo, text="If don't want to buy anything exit", font='arial 15 bold', fg='deep pink',
                  bg='black').grid(row=19, column=0, sticky='w')
            Button(clo, text="EXIT", font='arial 15 bold', fg='orange red', bg='lawn green', command=clo.destroy).grid(
                row=20, column=0, sticky='w')
            mainloop()

        Button(rtm, text="select", font='arial 15 bold', fg='black', bg='red2', bd=6, command=accessories).grid(row=5,
                                                                                                                column=7,
                                                                                                                sticky='e')

        Label(rtm, text="ACCESORIES:", font='arial 15 bold', fg='midnight blue', bg='mint cream').grid(row=5, column=0,
                                                                                                       sticky='w')
        Button(rtm, text="select", font='arial 15 bold', fg='navy blue', bg='black', bd=6, command=accessories).grid(
            row=5, column=7, sticky='e')

    Button(rt, text='Women Category', font='baskerville 30 bold italic', fg='black', bg='magenta', bd='20',
           command=fun1).grid(row=1, column=0, sticky='ewns')
    Button(rt, text='Men Category', font='baskervilee 30 bold italic', fg='black', bg='green', bd='20',
           command=fun2).grid(row=2, column=0, sticky='ewns')
    mainloop()


Button(root, text="PROCEED", bd=7, relief='ridge', compound='center', font='arial 20 bold', foreground='green',
       background='black', command=fun).grid(row=7, column=0, columnspan=5, sticky=E + W + N + S)

root.mainloop()

