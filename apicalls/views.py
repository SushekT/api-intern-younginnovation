from django.shortcuts import render
import requests
from .models import *
import json
from django.db.models import Min
# Create your views here.
def test(request):
    response = requests.get('https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json')
    data = json.loads(response.content.decode('utf-8'))
    
    for d in data:
        year = (d['year'])
        sale = d['sale']
        petroleum = d['petroleum_product']
        country = d['country']
        obj1, created1 = Year.objects.get_or_create(number=year)
        obj2, created2 = Petroleum.objects.get_or_create(name=petroleum)
        obj3, created3 = Country.objects.get_or_create(name=country)
        
        obj4, created4= Main.objects.get_or_create(sale=sale, year=obj1, petroleum=obj2, country=obj3)

    datas = Main.objects.all()

    context = {
        'datas': datas,

    }

    return render(request,'test.html', context)

def product_sales_by_country(request):
    country = Country.objects.all()
    petroleum = Petroleum.objects.all()
    sales = 0
    count=0
    for c in country:
        for p in petroleum:
            all = Main.objects.filter(country=c, petroleum=p)
            for a in all:
                if a.sale!= 0:
                    count= count+1
                    sales = sales + a.sale
            total = sales/count
            try:
                obj5= AverageSale.objects.get(product=p, countr=c)
                obj5.average = total
                obj5.save()
            except:
                create = AverageSale.objects.create(product=p, countr=c, average=total)
                print('New Average created')   


    data = AverageSale.objects.all()
    context = {'data': data,}



    return render(request,'product_sales_by_country.html', context)


def two_years(request):
    year = Year.objects.all().order_by("number")
    product = Petroleum.objects.all()
    
    for p in product:
        c=0
        sales = 0
        ganne=0
        for y in year:
            main = Main.objects.filter(year=y, petroleum=p)# 1 Barsa ko
            count=main.count()
            ganne = ganne+count
            for m in main:
                sales=sales+m.sale
            c= c+1
            if c == 2:
                total = sales/ganne
                obj6, create = TwoYearInterval.objects.get_or_create(product=p,average=total, date=str(y.number-1)+'-'+str(y.number))
                c=0
                sales = 0
                ganne=0

    data = TwoYearInterval.objects.all()
            
                  
    context={
        'data': data,
        'year': year,

    }
    return render(request,'two_years.html', context)

def leastsale(request):
    petrol = Petroleum.objects.all()
    main = Main.objects.all()
    i=0
    for p in petrol:
        momo = Main.objects.filter(petroleum=p).annotate(Min('sale')).order_by('sale')[i]
        while momo.sale == 0:
            i = i+1
            momo = Main.objects.filter(petroleum=p).annotate(Min('sale')).order_by('sale')[i]

        i=0
        obj6, create = Leastyear.objects.get_or_create(product=momo.petroleum, year=momo.year, leastsale=momo.sale)
    
    #for p in petrol:
        #momo = Main.objects.filter(petroleum=p)

        #for m in momo:
            #sale1 = m.sale
            #sale2=1
            #if sale1>sale2:
                #sale2=sale1
    data = Leastyear.objects.all()
    context = {
        'data': data,
        

    }
    return render(request, 'leastsale.html', context)