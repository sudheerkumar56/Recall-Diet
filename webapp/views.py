import os
import pickle

from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *

import matplotlib.pyplot as plt;
import numpy as np
import numpy
from django.shortcuts import render, redirect




def homepage(request):
    return render(request, 'index.html')

def signuppage(request):
    if request.method == 'POST':
        email = request.POST['email']

        d = users.objects.filter(email__exact=email).count()
        if d > 0:
            return render(request, 'signup.html', {'msg': "Email Already Registered"})

        else:

            password = request.POST['password']
            phone = request.POST['phone']
            name = request.POST['name']
            type_ = request.POST['type_']
            height = request.POST['height']
            weight = request.POST['weight']
            age = request.POST['age']
            age_cat = categorize_age(int(age))
            gen = request.POST['gen']

            
            d = users(name=name, email=email, password=password, phone=phone,  gender=gen, Height=height, weight=weight, age=age, age_cat=age_cat, type_diet=type_ )
            d.save()


            return render(request, 'signup.html', {'msg': "Register Success, You can Login.."})

    else:

        return render(request, 'signup.html')


def userloginaction(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pass_word = request.POST['pwd']
        if uid == 'admin' and pass_word == 'admin':
            request.session['adminid'] = 'admin'
            return render(request, 'admin_home.html')
        else:
    
            d = users.objects.filter(email__exact=uid).filter(password__exact=pass_word).count()
    
            if d > 0:
                d = users.objects.filter(email__exact=uid)
                request.session['email'] = uid
                request.session['name'] = d[0].name
                request.session['age'] = d[0].age_cat
                request.session['gen'] = d[0].gender
                request.session['typ_e'] = d[0].type_diet
                return render(request, 'user_home.html', {'data': d[0]})
            else:
                return render(request, 'index.html', {'msg': "Login Fail"})

    else:
        return render(request, 'user.html')



def adminhomedef(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'admin_home.html')

    else:
        return render(request, 'admin.html')

def adminlogoutdef(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'index.html')



def userlogoutdef(request):
    email= request.session["email"]
    del request.session['email']
    return render(request, 'index.html')


def userhomedef(request):
	if "email" in request.session:
		email=request.session["email"]
		d=users.objects.filter(email__exact=email)
	
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return redirect('n_userlogout')




def datasetupload(request):
    if request.method == 'POST':
        file = request.POST['file']
        import xlrd
        book = xlrd.open_workbook(file)
        sheet = book.sheet_by_index(0)
        d=dataset.objects.all()
        d.delete()
        #return prod_name, description, img, cnames, prices
        for r in range(1, sheet.nrows):
            v_a = int(sheet.cell(r, 0).value)
            v_b = int(sheet.cell(r, 1).value)
            v_c = int(sheet.cell(r, 2).value)
            v_b12 = int(sheet.cell(r, 3).value)
            carbs = int(sheet.cell(r, 4).value)
            fiber = int(sheet.cell(r, 5).value)
            sugars = int(sheet.cell(r, 6).value)
            calcium = int(sheet.cell(r, 7).value)
            iron = int(sheet.cell(r, 8).value)
            iodine = int(sheet.cell(r, 9).value)
            gen = sheet.cell(r, 10).value
            age_group = sheet.cell(r, 11).value
            typ_e = sheet.cell(r, 12).value

            d = dataset(v_a=v_a, v_b=v_b,v_c=v_c,v_b12=v_b12,\
             carbs=carbs, sugars=sugars, calcium=calcium, iron=iron, iodine=iodine, fiber=fiber,\
             age=age_group, gender=gen, typ_e=typ_e, period='Daily')
            d.save()

            d = dataset(v_a=v_a*7, v_b=v_b*7,v_c=v_c*7,v_b12=v_b12*7,\
             carbs=carbs*7, sugars=sugars*7, calcium=calcium*7, iron=iron*7, iodine=iodine*7, fiber=fiber*7,\
             age=age_group, gender=gen, typ_e=typ_e, period='Weekly')
            d.save()
            d = dataset(v_a=v_a*30, v_b=v_b*30,v_c=v_c*30,v_b12=v_b12*30,\
             carbs=carbs*30, sugars=sugars*30, calcium=calcium*30, iron=iron*30, iodine=iodine*30, fiber=fiber*30,\
             age=age_group, gender=gen, typ_e=typ_e, period='Monthly')
            d.save()
                                    
            
            


                
        return render(request, 'dataset.html', {'msg':'Dataset uploaded and data crawled !!'})
      
    else:
        return render(request, 'dataset.html')



def viewdataset(request):
    if "adminid" in request.session:
        d = food_details.objects.all()
        

        return render(request, 'viewdataset.html', {'data': d})

    else:
        return render(request, 'index.html')

                   
def addfood(request):
    return render(request, 'add_food.html')



def addfoodaction(request):
    if request.method == 'POST':
        name = request.POST['name']

        d = food_details.objects.filter(food_name__exact=name).count()
        if d > 0:
            return render(request, 'add_food.html', {'msg': "This food already added"})

        else:

            v_a = request.POST['v_a']
            v_b = request.POST['v_b']
            v_c = request.POST['v_c']
            v_b12 = request.POST['v_b12']
            
            carbs = request.POST['carbs']
            sugars = request.POST['sugars']
            calcium = request.POST['calcium']
            iron = request.POST['iron']
            iodine = request.POST['iodine']
            fiber = request.POST['fiber']

            
            d = food_details(food_name=name, v_a=v_a, v_b=v_b,v_c=v_c,v_b12=v_b12,\
             carbs=carbs, sugars=sugars, calcium=calcium, iron=iron, iodine=iodine, fiber=fiber)
            d.save()


            return render(request, 'add_food.html', {'msg': "Food Added Successfully!!"})

    else:

        return render(request, 'add_food.html')




def diarydef(request):
    if request.method == 'POST':

        email=request.session['email']

        from .DateDetails import main
        d_ate=main()                        
        fid=request.POST['fid']
        tim_e=request.POST['tim_e']
        d=food_details.objects.filter(id=fid)
        d=d[0]

        c=diary.objects.filter(email=email).filter(dat_e=d_ate['date']).filter(tim_e=tim_e).count()
        if c>0:
            d=food_details.objects.all()

            return render(request, 'diary.html', {'msg':'Duplicate data detected !! ', 'data':d})
        else:
            s=diary(email=email,food_name=d.food_name, dat_e=d_ate['date'],wee_k=d_ate['week'],\
            mont_h=d_ate['month'], v_a=d.v_a, v_b=d.v_b, v_c=d.v_c, v_b12=d.v_b12, carbs=d.carbs,\
            fiber=d.fiber, sugars=d.sugars, calcium=d.calcium, iron=d.iron, iodine=d.iodine, tim_e=tim_e)
            
            s.save()
     
        d=food_details.objects.all()
        return render(request, 'diary.html', {'msg':'Diary Updated!!', 'data':d})
      
    else:

        d=food_details.objects.all()
        return render(request, 'diary.html', {'data':d})



def categorize_age(age):
    res='';
    if age >= 1 and age <= 5:res='1_5'
    elif age >= 6 and age <= 10:res='6_10'
    elif age > 10 and age <= 20:res='11_20'
    elif age > 21 and age <= 30:res='21_30'
    elif age > 31 and age <= 45:
        res='30_45'
    elif age > 46 and age <= 60:
        res='46_60'
    else:res='61+'
    return res



import matplotlib.pyplot as plt
from io import BytesIO
import base64
import random

def generate_bar_graph(categories, values, yl, tit):
    # Sample data for the bar graph
    categories = categories
    values = values

    # Create the bar graph

    colors = ['#{:06x}'.format(random.randint(0, 0xFFFFFF)) for _ in range(len(categories))]
    plt.bar(categories, values, color=colors)
    plt.xlabel('')
    plt.ylabel(yl)
    plt.title(tit)

    # Save the plot to a bytes object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convert the plot to base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return image_base64


def food_rec(request):
    if request.method == 'POST':
        #age = int(request.POST['age'])
        #vn = int(request.POST['vn'])
        #typ_e = request.POST['typ_e']
        weight= int(request.POST['w'])
        height= int(request.POST['h'])

        from .FoodRecomnd import Diet_Control_Breakfast,Diet_Control_Lunch,Diet_Control_Dinner
        #weight =30

        #height = 75

        bmi = weight / ((height / 100) ** 2)

        print("Your body mass index is: ", bmi)
        # BMI class
        if (bmi < 16):
            print("Acoording to your BMI, you are Severely Underweight")
            clbmi = 4

        elif (bmi >= 16 and bmi < 18.5):
            print("Acoording to your BMI, you are Underweight")
            clbmi = 3

        elif (bmi >= 18.5 and bmi < 25):
            print("Acoording to your BMI, you are Healthy")
            clbmi = 2

        elif (bmi >= 25 and bmi < 30):
            print("Acoording to your BMI, you are Overweight")
            clbmi = 1

        elif (bmi >= 30):
            print("Acoording to your BMI, you are Severely Overweight")
            clbmi = 0


        if clbmi==1 or clbmi==0 :
            print("Weight Loss")
            catgry="Weight Loss"
            wl=[1, 2, 7, 8]
            cols=4
            break_fast=Diet_Control_Breakfast(wl,cols)
            lunch=Diet_Control_Lunch(wl, cols)
            dinner=Diet_Control_Dinner(wl, cols)
            
        elif clbmi==4 or clbmi==3 :
            print("Weight Gain")
            catgry="Weight Gain"
            wl = [0,1,2,3,4,7,9,10]
            cols = 8
            break_fast=Diet_Control_Breakfast(wl,cols)
            lunch=Diet_Control_Lunch(wl, cols)
            dinner=Diet_Control_Dinner(wl, cols)
        else:
            print("Healthy")
            catgry="Healthy"
            
            wl = [1,2,3,4,6,7,9]
            cols = 7
            break_fast=Diet_Control_Breakfast(wl,cols)
            lunch=Diet_Control_Lunch(wl, cols)
            dinner=Diet_Control_Dinner(wl, cols)

        

        


        return render(request, 'foodrecdisplay.html', {'break_fast': break_fast, 'lunch': lunch,'dinner': dinner,'catgry':catgry})

    else:

        email=request.session['email']

        d=users.objects.filter(email=email)
              
        
        return render(request, 'foodrec.html', {'d':d[0]})


def rda(request):
    if request.method == 'POST':
        mode= request.POST['mode']
        request.session['mode']=mode
        
        return render(request, 'rda2.html')

    else:

        email=request.session['email']
        d=users.objects.filter(email=email)
        return render(request, 'rda.html', {'d':d[0]})



def rda2(request):
    if request.method == 'POST':
        from .DateDetails import main
        dat_e=main()
        dt=dat_e['date']
        wk=dat_e['week']
        mth=dat_e['month']

        reportof= request.POST['reportof']
        name=reportof.upper()
        name=name.replace('V_', 'Vitamin ')
        mode=request.session['mode']
        email=request.session['email']
        age=request.session['age']
        gen=request.session['gen']
        typ_e=request.session['typ_e']

        if mode=='today':
            d=diary.objects.filter(email=email).filter(dat_e=dt)
            data = d.values(reportof) 
            user_res=0
            for d1 in data:
                user_res=d1[reportof]
            
            print(user_res,'<<<<<<<<<<<<<<<<', name)
            d=dataset.objects.filter(age=age).filter(gender=gen).filter(period='Daily').filter(typ_e=typ_e)
            data = d.values(reportof) 
            data_res=0
            for d1 in data:
                data_res=d1[reportof]
            print(data_res,'<<<<<<<<<<<<<<<<')
            graph=generate_bar_graph(['Intake', 'Recommend to intake'], [user_res, data_res], 'mg', name+" "+mode+"' report")#(categories, values, xl, tit):
        
        elif mode=='weekly':
            d=diary.objects.filter(email=email).filter(wee_k=wk)
            data = d.values(reportof) 
            user_res=0
            for d1 in data:
                user_res=user_res+d1[reportof]
            
            print(user_res,'<<<<<<<<<<<<<<<<', name)
            d=dataset.objects.filter(age=age).filter(gender=gen).filter(period='Weekly').filter(typ_e=typ_e)
            data = d.values(reportof) 
            data_res=0
            for d1 in data:
                data_res=d1[reportof]
            print(data_res,'<<<<<<<<<<<<<<<<')
            graph=generate_bar_graph(['Intake', 'Recommend to intake'], [user_res, data_res], 'mg', name+" "+mode+"' report")#(categories, values, xl, tit):
        
        elif mode=='monthly':
            d=diary.objects.filter(email=email).filter(mont_h=mth)
            data = d.values(reportof) 
            user_res=0
            for d1 in data:
                user_res=user_res+d1[reportof]
            
            print(user_res,'<<<<<<<<<<<<<<<<', name)
            d=dataset.objects.filter(age=age).filter(gender=gen).filter(period='Monthly').filter(typ_e=typ_e)
            data = d.values(reportof) 
            data_res=0
            for d1 in data:
                data_res=d1[reportof]
            print(data_res,'<<<<<<<<<<<<<<<<')
            graph=generate_bar_graph(['Intake', 'Recommend to intake'], [user_res, data_res], 'mg', name+" "+mode+"' report")#(categories, values, xl, tit):
        

            


        
        return render(request, 'rda2.html', {'image_base64': graph, 'b':True})

    else:
        pass


		
def viewprofilepage(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=users.objects.filter(email__exact=uid)
		
		return render(request, 'viewpprofile.html',{'data': d[0]})

	else:
		return render(request, 'user.html')




def updateprofile(request):
    if request.method == 'POST':
        name = request.POST["name"] 
        phone = request.POST['phone']
        email = request.session["email"]
        age = request.POST['age']
        height = request.POST['height']
        weight = request.POST['weight']
        typ_e = request.POST['typ_e']

        users.objects.filter(email=email).update(name=name,age=age, Height=height, weight=weight, type_diet=typ_e, phone=phone)
        return render(request, 'user_home.html',{'msg':'Profile Updated !!'} )
       
    else:
        email = request.session["email"]
        d = users.objects.filter(email=email)
          
        return render(request, 'updateprofile.html', {'data': d[0]})


