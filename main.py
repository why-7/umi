import tkinter as tk
from tkinter import messagebox
import datetime


def main():
    rodne_cislo = entry.get()

    if len(rodne_cislo) < 10 or len(rodne_cislo) > 11:
        messagebox.showerror("Chyba", "Nesprávná délka. Zadejte rodne cislo ve formatu"
                                         " 123456/1234 nebo 123456/123")
    if rodne_cislo[6] != '/':
        messagebox.showerror("Chyba", "Nespravny format. Pouzijte symbol / ")
    elif rodne_cislo[0:6].isnumeric() == 0:
        messagebox.showerror("Chyba", "Nespravny format. Nepovolené znaky")
    elif rodne_cislo[7:].isnumeric() == 0:
        messagebox.showerror("Chyba", "Nespravny format. Nepovolené znaky")

    if rodne_cislo[2] == '0' or rodne_cislo[2] == '1' or rodne_cislo[2] == '2' or rodne_cislo[2] == '3':
        pohlavi = "Muz"
    elif (rodne_cislo[2] == '5' or rodne_cislo[2] == '6' or rodne_cislo[2] == '7'
          or rodne_cislo[2] == '8'):
        pohlavi = "Zena"

    month = int(find_month(rodne_cislo, pohlavi))

    year = int(find_year(rodne_cislo))
    if year <= 1900 or year >= 2025:
        messagebox.showerror("Chyba",  'Nepovolené datum. Nespravny rok')

    try:
        final_date = datetime.date(year, month, int(rodne_cislo[4:6])).strftime('%d %b %Y')
    except:
        messagebox.showerror("Chyba",  "Nepovolené datum")
        
    divisibility_check = ''
    if int(rodne_cislo[0:6] + rodne_cislo[7:]) % 11 == 0:
        divisibility_check = ''
    elif len(rodne_cislo) == 11:
        divisibility_check = '\nRodne číslo neni dělitelné 11 bezezbytku'

    messagebox.showinfo('Vysledek', 'Vase pohlavi: ' + pohlavi + '\n' + 'Datum narozeni: '
                           + final_date + divisibility_check)


def find_month(rodne_cislo, pohlavi):
    if pohlavi == "Muz":
        if rodne_cislo[2] == '0' or rodne_cislo[2] == '1':
            return rodne_cislo[2:4]
        elif rodne_cislo[2] == '2' or rodne_cislo[2] == '3':
            return str(int(rodne_cislo[2:4]) - 20)
    else:
        if rodne_cislo[2] == '5' or rodne_cislo[2] == '6':
            return str(int(rodne_cislo[2:4]) - 50)
        elif rodne_cislo[2] == '7' or rodne_cislo[2] == '8':
            return str(int(rodne_cislo[2:4]) - 70)


def find_year(rodne_cislo):
    if int(rodne_cislo[0:2]) >= 25:
        return '19' + rodne_cislo[0:2]

    if len(rodne_cislo) == 10:
        return '19' + rodne_cislo[0:2]

    return '20' + rodne_cislo[0:2]


app = tk.Tk()
app.title("RC_Checker")

label = tk.Label(app, text="Napiste rodne cislo:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

check_button = tk.Button(app, text="Odeslat", command=main)
check_button.pack(pady=20)

app.mainloop()
