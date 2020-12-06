#Matt: this imports the expense tracker .py file
from testAddNode import *
#Matt: december is the monthly expenses




from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry

expense_tracker = expense_tree()
months = {    1:[],
              2:[],
              3:[],
              4:[],
              5:[],
              6:[],
              7:[],
              8:[],
              9:[],
              10:[],
              11:[],
              12:[]}


def Addexpense():

    print('yes2')

    Date = EDate.get()
    ItemName = Title.get()
    ItemPrice = float(Expense.get())
    ItemCategory = item(ItemName, ItemPrice).category

    data = [Date, ItemName, ItemPrice, ItemCategory]

    # sets up the key from the months dictionary
    # example: 1/12/20 --> January (1)

    month_num = Date[:2]
    if '/' in month_num:
        month_num = int(Date[0])
    else:
        month_num = int(Date[:2])
    print("Month num", month_num)
    months[month_num].append(item(ItemName, ItemPrice))
    print("length ", len(months[month_num]))

    for key in months.keys():
        m_l = monthly_expenses(months[key])
        expense_tracker.add_monthly_expense(m_l)

    expense_tracker.printTree(expense_tracker.root)

    # print("Root of the expense tree", expense_tracker.root.l)
    #
    # print("Left Child of the root", expense_tracker.root.left_child)
    #
    # '''decemberMonth = december.monthly_expenses(decemberItem)
    # december.expense_tree.add_monthly_expense(decemberMonth, decemberItem)'''

    TVExpense.insert('', 'end', values=data)


# def New_Month():
#
#     print('yes1')
#     Addexpense()
#     # print(expense_tracker.get_LON_items()[0])




GUI = Tk()
GUI.title('** Expense Recorder **')
GUI.geometry('1000x600')
# Maximize windrow
# GUI. state ('zoomed')

Tab = Notebook(GUI)
F1 = Frame(Tab, width=500, height=500, bg="light grey")
Tab.add(F1, text='Expense')

Tab.pack(fill=BOTH, expand=1)
# Tab 1 (Expense)

# ==========Row 0 ===========================
LDate = ttk.Label(F1, text='Date', font=(None, 18))
LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

EDate = DateEntry(F1, width=19, background='blue', foreground='white', font=(None, 18))
EDate.grid(row=0, column=1, padx=5, pady=5)

# ==========Row 1 ===========================
LTitle = ttk.Label(F1, text='Title', font=(None, 18))
LTitle.grid(row=1, column=0, padx=5, pady=5, sticky='w')
Title = StringVar()
ETitle = ttk.Entry(F1, textvariable= Title,font=(None,18))
ETitle.grid(row=1, column=1, padx=5, pady=5)
# ========== Row 2 =====================
LExpense = ttk.Label(F1, text='Expense', font=(None, 18))
LExpense.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Expense = StringVar()

EExpense = ttk.Entry(F1, textvariable=Expense, font=(None, 18))
EExpense.grid(row=2, column=1, padx=5, pady=5)

# ========== Row 3 =====================
BFIadd = ttk.Button(F1, text='Add', command=Addexpense)
BFIadd.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

# ========== Row 3 =====================
# BFInewMonth = ttk.Button(F1, text='New Month', command=New_Month)
# BFInewMonth.grid(row=3, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)


#========= Row 4 =======================

Category = StringVar() #Matt: allows Category to display a string
CCategory = ttk.Entry(F1, textvariable=Category, font=(None, 18)) #attributes for Category on GUI
CCategory.grid(row=4, column=1, padx=5, pady=5, sticky='w') #Grid features for Category

# ===========tree view===========

TVList = ['Date', 'Title', 'Expense','Category']
TVExpense = ttk.Treeview(F1, column=TVList, show='headings', height=5)
for i in TVList:
    TVExpense.heading(i, text=i.title())
TVExpense.grid(row=4, column=1, padx=5, pady=5, sticky='w', columnspan=3)

GUI.mainloop()
