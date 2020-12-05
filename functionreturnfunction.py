def MallInfo():
    def Electronics():

        def Mobiles():
            return "Samsung SmartPhones Available."
        def SmartTvs():
            return "TV Range=20000-100000"
        def WashingMachine():
            return "WM Range=5000-20000"
        def Refrigerators():
            return "RF Range=10000-200000"
        mob=Mobiles()
        stv=SmartTvs()
        wm=WashingMachine()
        rf=Refrigerators()

        return mob,stv,wm,rf
    def Fashion():
        def Tshirts():
            return "February New Collection of Tshirts."
        def PartyWears():
            return "Range=1000-5000"
        def FootWears():
            return "NIke,Puma,Air,Sparks"
        def Suits():
             return "Raymonds,Manyavar,BlackBerry."

        tshirt=Tshirts()
        pwear=PartyWears()
        fwear=FootWears()
        suit=Suits()

        return tshirt,pwear,fwear,suit
    def Cinema():
        def CinemaName():
            return "Fast And Furious 9."
        def Timings():
            return "9am-12pm"
        def Bookings():
            return "Housefull."
        def ScreenSize():
            return "Larger."
        Cname=CinemaName()
        time=Timings()
        book=Bookings()
        ssize=ScreenSize()
     
        return Cname,time,book,ssize
    def FoodStuffs():
        def Popcorn():
            return "Price:350"
        def Vegetarian():
            return "20Options Availale"
        def Nonvegetarian():
            return "15Options Available"
        def Snacks():
            return "10 Options Available"

        pop=Popcorn()
        veg=Vegetarian()
        Nveg=Nonvegetarian()
        snack=Snacks()
        return pop,veg,Nveg,snack


    elect=Electronics()
    fs=Fashion()
    ci=Cinema()
    fstuff=FoodStuffs()
    return elect,fs,ci,fstuff



ret=MallInfo()
for i in ret:
    print(i)
