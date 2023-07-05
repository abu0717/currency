import requests
data = requests.get("https://nbu.uz/uz/exchange-rates/json/").json()
c_euro = None
b_euro = None
dollor = None
c_dollor = None
c_funt = None
b_funt = None
c_franc = None
b_franc = None

while True:
    print('''
    1. 'Yevro'
    2. 'AQSh dollari'
    3. 'Angliya funt sterlingi'
    4. 'Shveytsariya franki'
    ''')

    try:
        Option = input('Kurslardan Birini Tanlang\n>>> ')
    except Exception as e:
        print('Faqat 1, 2, 3 va 4 raqamlarini kiriting: ')
        print('Error', e)

    if Option == '1':
        e = input('Sotib Olish yoki Sotishdan Birini Tanlang\n>>> ').title()
        if e == 'Sotib Olish':
            euro = int(input('Qancha Miqdorda Euro Olmoqchisiz ?\n>>> '))
            for i in data:
                if i['code'] == 'EUR':
                    euro_buy_price = float(i['nbu_cell_price'])
                    if b_euro is None:
                        b_euro = euro * euro_buy_price
                        print(f'Siz Beradigan summa {b_euro}') 

        if e == 'Sotish':
            euros = int(input('Qancha Miqdorada Euro Sotmoqchisiz ?\n>>> '))
            for i in data:
                if i['code'] == 'EUR':
                    euro_cell_price = float(i['nbu_buy_price'])
                    if c_euro is None:
                        c_euro = euros * euro_cell_price
                        print(f'Siz Oladigan Summa {c_euro}', )

    if Option == '2':
        d = input('Sotib olish yoki Sotishdan birini tanlang\n>>> ').title()
        if d == 'Sotib Olish':
            usd = int(input('Qancha Miqdorda AQSH Dollori Olmoqchisiz ?\n>>> '))
            for i in data:
                if i['code'] == 'USD':
                    cell_price = float(i['nbu_cell_price'])
                    if dollor is None:
                        dollor = usd * cell_price
                        print('Siz Beradigan Summa ', dollor)

        if d == 'Sotish':
            usd1 = int(input('Qancha Miqdorda AQSH Dollori Sotmoqchisiz ?\n>>> '))
            for i in data:
                if i['code'] == 'USD':
                    buy_price = float(i['nbu_buy_price'])
                    if c_dollor is None:
                        c_dollor = usd1 * buy_price
                        print('Siz Oladigan Summa', c_dollor)

    if Option == '3':
        rubl = input('Sotib Olish yoki Sotishdan birini tanlang\n>>> ').title()
        if rubl == 'Sotib Olish':
            rubles = int(input('Qancha Miqdorda Angliya Funt Sterlingi olmoqchisi\n>>> '))
            for i in data:
                if i['code'] == 'GBP':
                    currency_price = float(i['nbu_cell_price'])
                    if b_funt is None:
                        b_funt = rubles * currency_price
                        print('Siz beradigan Summa', b_funt)

        if rubl == 'Sotish':
            rublis = int(input('Qancha Miqdorda Angliya Funt Sterlingi Sotmoqchisiz ?\n>>> '))
            for i in data:
                if i['code'] == 'GBP':
                    funt_price = float(i['nbu_buy_price'])
                    if c_funt is None:
                        c_funt = rublis * funt_price
                        print('Siz Oladigan UZS', c_funt)

    if Option == '4':
        fr = input('Sotib olish yoki Sotishdan birini tanlang\n>>> ').title()
        if fr == 'Sotib Olish':
            franc = int(input('Qancha Miqdorda Shvetsariya Franki Olmoqchisiz\n>>> '))
            for i in data:
                if i['code'] == 'CHF':
                    franc_price = float(i['nbu_cell_price'])
                    if b_franc is None:
                        b_franc = franc * franc_price
                        print('Siz Beradigan Summa ', b_franc)

        if fr == 'Sotish':
            fr1 = int(input('Qancha Miqdorda Shvetsariya Franki Sotmoqchisiz\n>>> '))
            for i in data:
                if i['code'] == 'CHF':
                    franc1_price = float(i['nbu_buy_price'])
                    if c_franc is None:
                        c_franc = fr1 * franc1_price
                        print('Siz Oladigan Summa', c_franc)

    
    break