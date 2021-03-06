from queue import Empty
from tkinter import *
from tkinter import ttk
from database import *
from database import *
from system import *
from new import *
from datetime import datetime

# >>> global var <<<
goto_home = True


class user:
    def welcome():
        def detailed_view(root):

            detailed = Toplevel(root)
            detailed.geometry(f"700x520")
            detailed.title("Detailed Logs")
            detailed.resizable(False, False)
            # detailed.configure(bg=f"#4152B3")

            scrollbarx = Scrollbar(detailed, orient=HORIZONTAL)
            scrollbary = Scrollbar(detailed, orient=VERTICAL)

            tree = ttk.Treeview(detailed)
            tree.place(relx=0.01, rely=0.128, width=640, height=410)

            tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            tree.configure(selectmode="extended")

            scrollbarx.configure(command=tree.xview)
            scrollbary.configure(command=tree.yview)

            scrollbary.place(relx=0.934, rely=0.128, width=22, height=432)
            scrollbarx.place(relx=0.002, rely=0.922, width=651, height=22)

            tree.configure(
                columns=(
                    "Date",
                    "Time",
                    "Note",
                    "Account Used",
                    "Cash In",
                    "Cash Out",
                    "Account Balance Before",
                    "Account Balance After",
                    "Total Funds Before",
                    "Total Funds After",
                )
            )

            tree.heading("#0", text="ID", anchor=W)
            tree.heading("#1", text="Date", anchor=W)
            tree.heading("#2", text="Time", anchor=W)
            tree.heading("#3", text="Note", anchor=W)
            tree.heading("#4", text="Account Used", anchor=W)
            tree.heading("#5", text="Cash In", anchor=W)
            tree.heading("#6", text="Cash Out", anchor=W)
            tree.heading("#7", text="Account Balance Before", anchor=W)
            tree.heading("#8", text="Account Balance After", anchor=W)
            tree.heading("#9", text="Total Funds Before", anchor=W)
            tree.heading("#10", text="Total Funds After", anchor=W)

            tree.column("#0", stretch=NO, minwidth=25, width=50)
            tree.column("#1", stretch=NO, minwidth=0, width=100)
            tree.column("#2", stretch=NO, minwidth=0, width=100)
            tree.column("#3", stretch=NO, minwidth=0, width=200)
            tree.column("#4", stretch=NO, minwidth=0, width=150)
            tree.column("#5", stretch=NO, minwidth=0, width=100)
            tree.column("#6", stretch=NO, minwidth=0, width=100)
            tree.column("#7", stretch=NO, minwidth=0, width=180)
            tree.column("#8", stretch=NO, minwidth=0, width=180)
            tree.column("#9", stretch=NO, minwidth=0, width=150)
            tree.column("#10", stretch=NO, minwidth=0, width=150)

            if dblogs.get(Q.get_active()) > 0:
                get_id = dblogs.id(Q.get_active())
                entry_id = 0
                for x in get_id:
                    entry_id = entry_id + 1
                    tree.insert(
                        parent="",
                        index=0,
                        text=entry_id,
                        values=(
                            f"{dblogs.date(x)}",
                            f"{dblogs.time(x)}",
                            f"{dblogs.note(x)}",
                            f"{dblogs.type(x)}",
                            f"{dblogs.cash_in(x)}",
                            f"{dblogs.cash_out(x)}",
                            f"{dblogs.before_bal(x)}",
                            f"{dblogs.after_bal(x)}",
                            f"{dblogs.funds_before(x)}",
                            f"{dblogs.funds_after(x)}",
                        ),
                    )
            else:
                tree.insert(
                    parent="", index=0, text="No", values=("Records", "to be", "shown.")
                )

            detailed.mainloop()

        def view():
            w = 450
            h = 600

            customtkinter.set_appearance_mode(
                "Dark"
            )  # Modes: "System" (standard), "Dark", "Light"
            customtkinter.set_default_color_theme(
                "blue"
            )  # Themes: "blue" (standard), "green", "dark-blue"

            view = customtkinter.CTk()
            view.geometry(f"{w}x{h}")
            view.title("Personal Info")
            view.resizable(False, False)

            # main frame
            main = customtkinter.CTkFrame(
                view, width=450, height=600, corner_radius=0, fg_color=f"#4152B3"
            )

            # center frame

            center = customtkinter.CTkFrame(
                main, width=350, height=500, corner_radius=25, fg_color="white"
            )

            # config
            # labels
            lfont = ("Calibri", 14, "bold")
            lbg = f"#FFFFFF"
            lfg = f"black"
            # entry
            efont = ("Calibri", 15)
            ebg = f"white"
            efg = f"black"
            ewidth = 200
            eborder = 2
            ebordercolor = f"#4152B3"
            eradius = 10
            egfcolor = ebg

            space1 = Label(center, text="", bg=lbg).pack(side=TOP, pady=1)
            lfn = Label(center, text="Account Name", bg=lbg, fg=lfg, font=lfont)
            lfn.pack(side=TOP)
            efn = customtkinter.CTkLabel(
                center,
                width=ewidth,
                text=Q.get_user(Q.get_active()),
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            efn.pack(side=TOP, pady=5)

            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lmi = Label(center, text="Email", bg=lbg, fg=lfg, font=lfont)
            lmi.pack(side=TOP)
            emi = customtkinter.CTkLabel(
                center,
                width=ewidth,
                text=Q.get_active(),
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            emi.pack(side=TOP, pady=5)

            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lln = Label(center, text="Full Name", bg=lbg, fg=lfg, font=lfont)
            lln.pack(side=TOP)
            eln = customtkinter.CTkLabel(
                center,
                width=ewidth,
                text=f"{Q.get_fn(Q.get_active())} {Q.get_mi(Q.get_active())} {Q.get_ln(Q.get_active())}",
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            eln.pack(side=TOP, pady=5)

            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            ldob = Label(center, text="Age", bg=lbg, fg=lfg, font=lfont)
            ldob.pack(side=TOP)
            edob = customtkinter.CTkLabel(
                center,
                width=ewidth,
                text=Q.get_age(Q.get_active()),
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            edob.pack(side=TOP, pady=5)

            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lsq = Label(
                center, text="Date of Birth (MM-DD-YYYY)", bg=lbg, fg=lfg, font=lfont
            )
            lsq.pack(side=TOP)
            esq = customtkinter.CTkLabel(
                center,
                width=ewidth,
                text=Q.get_dob(Q.get_active()),
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            esq.pack(side=TOP, pady=5)
            # ========= >>> answer question label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            laq = Label(center, text="Security Question", bg=lbg, fg=lfg, font=lfont)
            laq.pack(side=TOP)
            # ========= >>> field for answer entry <<< =========
            eaq = customtkinter.CTkLabel(
                center,
                width=ewidth,
                text=Q.get_sq(Q.get_active()),
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            eaq.pack(side=TOP, pady=5)

            center.pack(side=TOP, pady=45)
            center.pack_propagate(False)

            main.pack()
            main.pack_propagate(False)

            view.mainloop()

        def make_transac():

            w = 450
            h = 420

            customtkinter.set_appearance_mode(
                "Dark"
            )  # Modes: "System" (standard), "Dark", "Light"
            customtkinter.set_default_color_theme(
                "blue"
            )  # Themes: "blue" (standard), "green", "dark-blue"

            root = customtkinter.CTk()
            root.geometry(f"{w}x{h}")
            root.title("Personal Info")
            root.resizable(False, False)

            # main frame
            main = customtkinter.CTkFrame(
                root, width=450, height=420, corner_radius=0, fg_color=f"#4152B3"
            )

            # center frame

            center = customtkinter.CTkFrame(
                main, width=350, height=320, corner_radius=25, fg_color="white"
            )

            # config
            # labels
            lfont = ("Calibri", 14, "bold")
            lbg = f"#FFFFFF"
            lfg = f"black"
            # entry
            efont = ("Calibri", 15)
            ebg = f"white"
            efg = f"black"
            ewidth = 200
            eborder = 2
            ebordercolor = f"#4152B3"
            eradius = 10
            egfcolor = ebg

            label1 = Label(center, text="", bg=lbg).pack(side=TOP, pady=1)
            label2 = Label(
                center, text="Select an account to use", bg=lbg, fg=lfg, font=lfont
            )
            label2.pack(side=TOP)

            options = []

            get_bank = bank.get(Q.get_active())
            if get_bank > 0:
                get_id = bank.id(Q.get_active())
                for x in get_id:
                    options.append(str(x[0]) + " - " + bank.type(x))

            opts = StringVar()

            combo = ttk.Combobox(
                master=center,
                textvariable=opts,
                width=30,
            )
            combo["values"] = options
            combo.pack(side=TOP)
            combo.current(0)
            combo.bind("<<ComboboxSelected>>")

            # ========= >>> Account details label <<< =========
            space1 = Label(center, text="", bg=lbg).pack(side=TOP, pady=1)
            lfn = Label(center, text="Transaction Details", bg=lbg, fg=lfg, font=lfont)
            lfn.pack(side=TOP)
            # ========= >>> Account name entry <<< =========
            efn = customtkinter.CTkEntry(
                center,
                width=ewidth,
                placeholder_text=f"Amount to add",
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            efn.pack(side=TOP, pady=5)
            # ========= >>> Account balance entry <<< =========
            efn2 = customtkinter.CTkEntry(
                center,
                width=ewidth,
                placeholder_text=f"Amount to deduct",
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            efn2.pack(side=TOP, pady=5)

            # ========= >>> confirm password label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lmi = Label(center, text="Note", bg=lbg, fg=lfg, font=lfont)
            lmi.pack(side=TOP)
            # ========= >>> field for comfirm password entry <<< =========
            emi = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            emi.pack(side=TOP, pady=5)

            def confirm():
                option = combo.get()
                bid = option.split("-")[0]
                if transac.make(
                    Q.get_active(),
                    bank.type(bid),
                    efn.get(),
                    bank.bal(bid),
                    bank.total(Q.get_active()),
                    emi.get(),
                    efn2.get(),
                ):
                    if success.transac():
                        root.destroy()
                        global goto_home
                        goto_home = True

            def cancel():
                root.destroy()
                global goto_home
                goto_home = True

            btn = customtkinter.CTkButton(
                center,
                text="CONFIRM",
                corner_radius=10,
                border_width=0,
                text_font=(f"Calibri", 11, f"bold"),
                text_color=f"white",
                hover_color=f"#5AC658",
                bg_color=f"white",
                fg_color=f"#3084DD",
                command=lambda: confirm(),
                width=80,
            )
            btn.place(x=140, y=280)

            btn2 = customtkinter.CTkButton(
                center,
                text="CANCEL",
                corner_radius=10,
                border_width=0,
                text_font=(f"Calibri", 11, f"bold"),
                text_color=f"white",
                hover_color=f"#FF4545",
                bg_color=f"white",
                fg_color=f"#3084DD",
                command=lambda: cancel(),
                width=80,
            )
            btn2.place(x=240, y=280)

            center.pack(side=TOP, pady=45)
            center.pack_propagate(False)

            main.pack()
            main.pack_propagate(False)

            root.mainloop()

        def delete():

            w = 450
            h = 420

            customtkinter.set_appearance_mode(
                "Dark"
            )  # Modes: "System" (standard), "Dark", "Light"
            customtkinter.set_default_color_theme(
                "blue"
            )  # Themes: "blue" (standard), "green", "dark-blue"

            root = customtkinter.CTk()
            root.geometry(f"{w}x{h}")
            root.title("Personal Info")
            root.resizable(False, False)

            # main frame
            main = customtkinter.CTkFrame(
                root, width=450, height=420, corner_radius=0, fg_color=f"#4152B3"
            )

            # center frame

            center = customtkinter.CTkFrame(
                main, width=350, height=320, corner_radius=25, fg_color="white"
            )

            # config
            # labels
            lfont = ("Calibri", 14, "bold")
            lbg = f"#FFFFFF"
            lfg = f"black"
            # entry
            efont = ("Calibri", 15)
            ebg = f"white"
            efg = f"black"
            ewidth = 200
            eborder = 2
            ebordercolor = f"#4152B3"
            eradius = 10
            egfcolor = ebg

            label1 = Label(center, text="", bg=lbg).pack(side=TOP, pady=1)
            label2 = Label(
                center, text="Select an account to remove", bg=lbg, fg=lfg, font=lfont
            )
            label2.pack(side=TOP)

            options = []

            get_bank = bank.get(Q.get_active())
            if get_bank > 0:
                get_id = bank.id(Q.get_active())
                for x in get_id:
                    options.append(str(x[0]) + " - " + bank.type(x))

            opts = StringVar()

            cash_type = StringVar()
            cash_bal = StringVar()

            def lookup(event):
                option = combo.get()
                bid = option.split("-")[0]

                cash_type.set(bank.type(bid))
                cash_bal.set(bank.bal(bid))

            combo = ttk.Combobox(
                master=center,
                textvariable=opts,
                width=30,
            )
            combo["values"] = options
            combo.pack(side=TOP)
            combo.current(0)
            combo.bind("<<ComboboxSelected>>", lookup)

            # ========= >>> Account details label <<< =========
            space1 = Label(center, text="", bg=lbg).pack(side=TOP, pady=1)
            lfn = Label(center, text="Account Details", bg=lbg, fg=lfg, font=lfont)
            lfn.pack(side=TOP)
            # ========= >>> Account name entry <<< =========
            efn = customtkinter.CTkEntry(
                center,
                width=ewidth,
                textvariable=cash_type,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            efn.pack(side=TOP, pady=5)
            # ========= >>> Account balance entry <<< =========
            efn2 = customtkinter.CTkEntry(
                center,
                width=ewidth,
                textvariable=cash_bal,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            efn2.pack(side=TOP, pady=5)

            # ========= >>> confirm password label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lmi = Label(center, text="Confirm password", bg=lbg, fg=lfg, font=lfont)
            lmi.pack(side=TOP)
            # ========= >>> field for comfirm password entry <<< =========
            emi = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
                show="*",
            )
            emi.pack(side=TOP, pady=5)

            def confirm():
                if Q.verify_pw(Q.get_user(Q.get_active()), emi.get()):
                    option = combo.get()
                    bid = option.split("-")[0]
                    if bank.delete(
                        bank.type(bid),
                        Q.get_active(),
                        bid,
                        bank.bal(bid),
                        bank.total(Q.get_active()),
                    ):
                        if success.del_acc():
                            root.destroy()
                            global goto_home
                            goto_home = True
                else:
                    error.password()

            def cancel():
                root.destroy()
                global goto_home
                goto_home = True

            btn = customtkinter.CTkButton(
                center,
                text="CONFIRM",
                corner_radius=10,
                border_width=0,
                text_font=(f"Calibri", 11, f"bold"),
                text_color=f"white",
                hover_color=f"#5AC658",
                bg_color=f"white",
                fg_color=f"#3084DD",
                command=lambda: confirm(),
                width=80,
            )
            btn.place(x=140, y=280)

            btn2 = customtkinter.CTkButton(
                center,
                text="CANCEL",
                corner_radius=10,
                border_width=0,
                text_font=(f"Calibri", 11, f"bold"),
                text_color=f"white",
                hover_color=f"#FF4545",
                bg_color=f"white",
                fg_color=f"#3084DD",
                command=lambda: cancel(),
                width=80,
            )
            btn2.place(x=240, y=280)

            center.pack(side=TOP, pady=45)
            center.pack_propagate(False)

            main.pack()
            main.pack_propagate(False)

            root.mainloop()

        def add():
            w = 450
            h = 320

            customtkinter.set_appearance_mode(
                "Dark"
            )  # Modes: "System" (standard), "Dark", "Light"
            customtkinter.set_default_color_theme(
                "blue"
            )  # Themes: "blue" (standard), "green", "dark-blue"

            root = customtkinter.CTk()
            root.geometry(f"{w}x{h}")
            root.title("Personal Info")
            root.resizable(False, False)

            # main frame
            main = customtkinter.CTkFrame(
                root, width=450, height=320, corner_radius=0, fg_color=f"#4152B3"
            )

            # center frame

            center = customtkinter.CTkFrame(
                main, width=350, height=220, corner_radius=25, fg_color="white"
            )

            # config
            # labels
            lfont = ("Calibri", 14, "bold")
            lbg = f"#FFFFFF"
            lfg = f"black"
            # entry
            efont = ("Calibri", 15)
            ebg = f"white"
            efg = f"black"
            ewidth = 200
            eborder = 2
            ebordercolor = f"#4152B3"
            eradius = 10
            egfcolor = ebg

            # ========= >>> Account name label <<< =========
            space1 = Label(center, text="", bg=lbg).pack(side=TOP, pady=1)
            lfn = Label(center, text="Account Name", bg=lbg, fg=lfg, font=lfont)
            lfn.pack(side=TOP)
            # ========= >>> Account name entry <<< =========
            efn = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            efn.pack(side=TOP, pady=5)

            # ========= >>> account balance label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lmi = Label(
                center, text="Account balance in PHP", bg=lbg, fg=lfg, font=lfont
            )
            lmi.pack(side=TOP)
            # ========= >>> field for account balance entry <<< =========
            emi = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            emi.pack(side=TOP, pady=5)

            def confirm():
                if validate.fields(efn.get()) or validate.fields(emi.get()):
                    error.empty()
                else:
                    if bank.get(Q.get_active()) == 0:
                        total = float(0.00)
                    else:
                        total = bank.total(Q.get_active())
                    if bank.write(Q.get_active(), efn.get(), emi.get(), total):
                        if success.add_acc():
                            root.destroy()
                            global goto_home
                            goto_home = True

            def cancel():
                root.destroy()
                global goto_home
                goto_home = True

            btn = customtkinter.CTkButton(
                center,
                text="CONFIRM",
                corner_radius=10,
                border_width=0,
                text_font=(f"Calibri", 11, f"bold"),
                text_color=f"white",
                hover_color=f"#5AC658",
                bg_color=f"white",
                fg_color=f"#3084DD",
                command=lambda: confirm(),
                width=80,
            )
            btn.place(x=140, y=180)

            btn2 = customtkinter.CTkButton(
                center,
                text="CANCEL",
                corner_radius=10,
                border_width=0,
                text_font=(f"Calibri", 11, f"bold"),
                text_color=f"white",
                hover_color=f"#FF4545",
                bg_color=f"white",
                fg_color=f"#3084DD",
                command=lambda: cancel(),
                width=80,
            )
            btn2.place(x=240, y=180)

            center.pack(side=TOP, pady=45)
            center.pack_propagate(False)

            main.pack()
            main.pack_propagate(False)

            root.mainloop()

        def home():

            dark_blue = f"#4152B3"
            green = f"#5AC658"
            light_blue = f"#3084DD"
            default_text_color = f"black"
            red = f"#FF4545"

            root = customtkinter.CTk()
            root.title(f"Hi, {Q.get_user(Q.get_active())}!")
            root.geometry("780x520")
            root.resizable(False, False)
            root.configure(background=dark_blue)  #! -to change

            # ============ create two frames ============

            # configure grid layout (2x1)
            root.grid_columnconfigure(1, weight=1)
            root.grid_rowconfigure(0, weight=1)

            frame_left = customtkinter.CTkFrame(
                master=root, width=180, corner_radius=0, fg_color=dark_blue
            )  #! -tochange
            frame_left.grid(row=0, column=0, sticky="nswe")

            frame_right = customtkinter.CTkFrame(
                master=root, fg_color=f"white"
            )  #! -to change
            frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

            # ============ frame_left ============

            empty = label_1 = customtkinter.CTkLabel(master=frame_left, text="")
            empty.pack(side=TOP, pady=10, padx=10)

            label_1 = customtkinter.CTkLabel(
                master=frame_left,
                text=f"{Q.get_user(Q.get_active())}",
                text_font=("Roboto Medium", 25),  # font name and size in px
                text_color="white",
            )
            label_1.pack(side=TOP, pady=10, padx=10)

            button_1 = customtkinter.CTkButton(
                master=frame_left,
                text="VIEW PROFILE",
                border_width=1,
                border_color=f"white",
                text_color="white",
                fg_color=None,
                hover_color=f"#6595D4",
                bg_color=dark_blue,
                corner_radius=5,
                command=lambda: view(),
            )
            # button_1.grid(row=2, column=0, pady=10, padx=20)
            button_1.pack(side=TOP, pady=10, padx=20)

            button_2 = customtkinter.CTkButton(
                master=frame_left,
                text="SETTINGS",
                border_width=1,
                border_color=f"white",
                text_color="white",
                fg_color=None,
                hover_color=f"#6595D4",
                bg_color=dark_blue,
                corner_radius=5,
            )
            # command=root.button_event)
            # button_2.grid(row=3, column=0, pady=10, padx=20)
            button_2.pack(side=TOP, pady=10, padx=20)

            button_3 = customtkinter.CTkButton(
                master=frame_left,
                text="ABOUT",
                border_width=1,
                border_color=f"white",
                text_color="white",
                fg_color=None,
                hover_color=f"#6595D4",
                bg_color=dark_blue,
                corner_radius=5,
            )  # <- custom tuple-color
            # command=root.button_event)
            # button_3.grid(row=4, column=0, pady=10, padx=20)
            button_3.pack(side=TOP, pady=10, padx=20)

            # ============ frame_right ============

            # configure grid layout (3x7)
            frame_right.rowconfigure((0, 1, 2, 3), weight=1)
            frame_right.rowconfigure(7, weight=10)
            frame_right.columnconfigure((0, 1), weight=1)
            frame_right.columnconfigure(2, weight=0)

            frame_info = customtkinter.CTkFrame(
                master=frame_right,
                fg_color=green,
            )
            frame_info.grid(
                row=0,
                column=0,
                columnspan=2,
                rowspan=4,
                pady=20,
                padx=20,
                sticky="nsew",
            )

            # ============ frame_info ============

            # configure grid layout (1x1)
            frame_info.rowconfigure(0, weight=1)
            frame_info.columnconfigure(0, weight=1)

            label_info_1 = customtkinter.CTkLabel(
                master=frame_info,
                text="Current Total Balance",
                text_font=("Roboto Medium", 12),
                text_color="white",
                justify=tkinter.LEFT,
            )
            label_info_1.grid(column=0, row=0, sticky="w", padx=15, pady=5)

            if bank.get(Q.get_active()) == 0:
                current_total = f"0.00"
            else:
                current_total = bank.total(Q.get_active())

            label_info_2 = customtkinter.CTkLabel(
                master=frame_info,
                text=current_total,
                text_font=("Roboto Medium", 30),
                # "Current balance:" ,
                height=100,
                # border_width=1,
                # border_color=f"white",
                text_color=green,
                fg_color=f"white",
                justify=tkinter.LEFT,
            )
            label_info_2.grid(column=0, row=1, sticky="nwe", padx=15, pady=0)

            get_date = datetime.now()
            dt_string = get_date.strftime("%B %d, %Y")

            date = customtkinter.CTkLabel(
                master=frame_info,
                text=f"as of {dt_string}",
                text_font=("Roboto Medium", 12),
                text_color="white",
            )
            date.grid(row=3, column=0, sticky="ew", padx=15, pady=15)

            # ============ frame_right ============

            logs = Listbox(
                master=frame_right,
                width=500,
                fg=default_text_color,
                borderwidth=0,
            )
            logs.grid(row=7, column=0, pady=0, padx=20, sticky="w")

            get_logs = dblogs.get(Q.get_active())
            if get_logs > 0:
                get_id = dblogs.id(Q.get_active())
                for x in get_id:
                    if dblogs.note(x) == f"Unbinded an account.":
                        str_list = f"  {dblogs.date(x)}  {dblogs.time(x)}  {dblogs.note(x)} | Account name: {dblogs.type(x)} | Total funds before: {dblogs.funds_before(x)} | Total funds after: {dblogs.funds_after(x)}"
                    elif dblogs.note(x) == f"Registered a new account.":
                        str_list = f"  {dblogs.date(x)}  {dblogs.time(x)}  {dblogs.note(x)} | Account name: {dblogs.type(x)} with balance of PHP {dblogs.cash_in(x)} | Total funds before: {dblogs.funds_before(x)} | Total funds after: {dblogs.funds_after(x)}"
                    else:
                        str_list = f"  {dblogs.date(x)}  {dblogs.time(x)}  {dblogs.note(x)} | Account used: {dblogs.type(x)} | PHP {dblogs.before_bal(x)} + {dblogs.cash_in(x)} - {dblogs.cash_out(x)} | Total funds before: {dblogs.funds_before(x)} | Total funds after: {dblogs.funds_after(x)}"
                    logs.insert(0, str_list)
            else:
                logs.insert(END, "No transactions made.")

            accs = Listbox(
                master=frame_right,
                # width=50,
                # height=50,
                fg=default_text_color,
                borderwidth=0,
            )
            accs.grid(row=2, column=2, columnspan=1, pady=5, padx=20, sticky="we")

            get_bank = bank.get(Q.get_active())
            if get_bank > 0:
                get_id = bank.id(Q.get_active())
                for x in get_id:
                    str_list = f"   {bank.type(x)}  :  PHP {bank.bal(x)}"
                    accs.insert(END, str_list)
            else:
                accs.insert(END, "No accounts found.")

            label_2 = customtkinter.CTkLabel(
                master=frame_right,
                height=25,
                text="Registered Accounts",
                text_color=f"white",
                fg_color=light_blue,
                bg_color=f"white",
                justify=tkinter.LEFT,
                text_font=("Roboto Medium", 12),
            )
            label_2.grid(row=1, column=2, columnspan=1, pady=10, padx=20, sticky="we")

            label_3 = customtkinter.CTkLabel(
                master=frame_right,
                height=25,
                text="Recent Logs",
                text_color=f"white",
                fg_color=light_blue,
                bg_color=f"white",
                justify=tkinter.LEFT,
                width=200,
                text_font=("Roboto Medium", 12),
            )
            label_3.grid(row=6, column=0, pady=10, padx=20, sticky="w")

            def click_add():
                root.destroy()
                add()

            def click_del():
                if bank.get(Q.get_active()) == 0:
                    error.delete()
                else:
                    root.destroy()
                    delete()

            def click_transac():
                if bank.get(Q.get_active()) == 0:
                    error.no_account()
                else:
                    root.destroy()
                    make_transac()

            add_account = customtkinter.CTkButton(
                master=frame_right,
                height=25,
                text="Add Account",
                text_color=f"white",
                fg_color=light_blue,
                hover_color=f"#6595D4",
                corner_radius=5,
                text_font=("Roboto Medium", 11),
                command=lambda: click_add(),
            )
            add_account.grid(
                row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we"
            )

            rem_account = customtkinter.CTkButton(
                master=root,
                height=25,
                text="Remove Account",
                # border_width=2,
                # border_color=red,
                text_color=f"white",
                # text_color=red,
                # fg_color=f"white",
                fg_color=red,
                bg_color=f"white",
                hover_color=f"#6595D4",
                corner_radius=5,
                text_font=("Roboto Medium", 11),
                command=lambda: click_del(),
            )
            rem_account.place(y=290, x=600)

            transac = customtkinter.CTkButton(
                master=root,
                height=25,
                text="Make Transaction",
                # border_width=2,
                # border_color=green,
                # text_color=green,
                text_color=f"white",
                # fg_color=f"white",
                fg_color=green,
                bg_color=f"white",
                hover_color=f"#6595D4",
                corner_radius=5,
                text_font=("Roboto Medium", 11),
                command=lambda: click_transac(),
            )
            transac.place(y=326, x=600)

            def click_detailed(root):
                detailed_view(root)

            detailed = customtkinter.CTkButton(
                master=root,
                height=25,
                text="Detailed Logs",
                # border_width=2,
                # border_color=green,
                # text_color=green,
                text_color=f"white",
                # fg_color=f"white",
                fg_color=f"#0c0c04",
                bg_color=f"white",
                hover_color=f"#6595D4",
                corner_radius=5,
                text_font=("Roboto Medium", 11),
                command=lambda: click_detailed(root),
            )
            detailed.place(y=362, x=600)

            entry = customtkinter.CTkEntry(
                master=frame_right,
                width=120,
                placeholder_text="search for available log",
                text_font=(f"Roboto Medium", 10),
                text_color=light_blue,
                border_color=light_blue,
                border_width=2,
                fg_color=None,
                corner_radius=10,
            )
            entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

            button_5 = customtkinter.CTkButton(
                master=frame_right,
                text="EXIT",
                corner_radius=10,
                border_width=0,
                text_font=(f"Roboto Medium", 14),
                text_color=f"white",
                fg_color=f"#4152B3",
                # bg_color=f"white",
                hover_color=f"#FF4545",
                command=lambda: root.destroy(),
            )
            button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

            root.mainloop()

        global goto_home
        while goto_home:
            goto_home = False
            home()

    # welcome()
