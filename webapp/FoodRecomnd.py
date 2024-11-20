import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import random

def Diet_Control_Breakfast(wl, cols):
    food_dataset = pd.read_csv('food.csv', encoding="utf-8")
    rec_food = food_dataset
    Breakfastdata = food_dataset['Breakfast']
    BreakfastdataNumpy = Breakfastdata.to_numpy()
    Food_itemsdata = food_dataset['Food_items']

    breakfastfoodseparated = []
    breakfastfoodseparatedID = []
 
    for i in range(len(Breakfastdata)):
        if BreakfastdataNumpy[i] == 1:
            breakfastfoodseparated.append(Food_itemsdata[i])
            breakfastfoodseparatedID.append(i)

    # retrieving Breafast data rows by loc method
    breakfastfoodseparatedIDdata = food_dataset.iloc[breakfastfoodseparatedID]
    # print("bk=",breakfastfoodseparatedIDdata)
    # print("breakfastfoodseparatedID=",(breakfastfoodseparatedID))
    fddata = breakfastfoodseparatedIDdata
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    nutritions = [0] + val
    print(nutritions)
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.iloc[nutritions]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T
    # print("brfst=",breakfastfoodseparatedIDdata)

    # converting into numpy array
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.to_numpy()
    # print("bstnumpi=",breakfastfoodseparatedIDdata)

    ## K-Means Based  Breakfast Food
    Datacalorie = breakfastfoodseparatedIDdata[0:, 1:len(breakfastfoodseparatedIDdata)]
    # print("DC=", Datacalorie)
    # print("DClwen=", len(Datacalorie))

    X = np.array(Datacalorie)
    # print("x=", X)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    y_kmeans = kmeans.predict(X)
    # print("y_kmeans=",y_kmeans)

    # retrieving the labels for breakfast food
    brklbl = kmeans.labels_
    # print("brklbl=", brklbl)

    inp = []
    ## Reading of the Dataet
    datafin_nutr = pd.read_csv('nutrition_distriution.csv')
    ## train set
    datafin_nutr = datafin_nutr.T
    # print("datafin_nutr=",datafin_nutr)

    weightcat = datafin_nutr.iloc[wl]
    
    weightcat = weightcat.T

    # Converting numpy array
    weightcatDdata = weightcat.to_numpy()

    weightcat = weightcatDdata[0:, 0:len(weightcatDdata)]

    print("wlcatdata=", weightcat)

    weightcatfin = np.zeros((len(weightcat) * 5, cols), dtype=np.float32)
    # print("weightlossfin=",weightlossfin)
    # print("weightfinlen=", len(weightcatfin))

    t = 0
    r = 0
    s = 0
    yt = []
    yr = []
    ys = []

    # print("weightlosscat=", len(weightcat))

    for zz in range(5):
        # print("zz=", zz)
        for jj in range(len(weightcat)):
            # print("jj=",jj)
            valloc = list(weightcat[jj])
            # print("nval=", np.array(valloc))
            weightcatfin[t] = np.array(valloc)
            # print("brklbl=", brklbl[jj])
            yt.append(brklbl[jj])
            t += 1
    # print("yt=", len(yt))
    X_test = np.zeros((len(weightcat), cols), dtype=np.float32)
    # print("X_test=",X_test)

    # print('####################')

    # randomforest
    for jj in range(len(weightcat)):
        valloc = list(weightcat[jj])

        X_test[jj] = np.array(valloc)

    X_train = weightcatfin  # Features
    y_train = yt  # Labels

    # Create a RF Classifier
    clf = RandomForestClassifier(n_estimators=100)

    # Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    rec = []
    for i in range(len(y_pred)):
        # print("y=",y_pred[i])
        if y_pred[i] == 0:
            rec.append(breakfastfoodseparatedID[i])

    # print("rec=", rec)

    # print(food_dataset.iloc[rec])

    food_dataset = food_dataset.iloc[rec]
    print("Breakfast")
    #print(food_dataset["Food_items"])

    fditems=food_dataset["Food_items"].tolist()
    
    brkst_random_elements = random.sample(fditems, 10)


    
    return brkst_random_elements


def Diet_Control_Lunch(wl, cols):
    food_dataset = pd.read_csv('food.csv', encoding="utf-8")
    rec_food = food_dataset
    Lunchdata = food_dataset['Lunch']
    LunchdataNumpy = Lunchdata.to_numpy()

    Food_itemsdata = food_dataset['Food_items']

    Lunchfoodseparated = []
    LunchfoodseparatedID = []

    for i in range(len(Lunchdata)):
        if LunchdataNumpy[i] == 1:
            Lunchfoodseparated.append(Food_itemsdata[i])
            LunchfoodseparatedID.append(i)

    # retrieving Lunch data rows by loc method |
    LunchfoodseparatedIDdata = food_dataset.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    nutritions = [0] + val
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.iloc[nutritions]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T

    # converting into numpy array
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.to_numpy()

    ## K-Means Based  lunch Food
    Datacalorie = LunchfoodseparatedIDdata[0:, 1:len(LunchfoodseparatedIDdata)]

    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

    XValu = np.arange(0, len(kmeans.labels_))

    # retrieving the labels for lunch food
    lnchlbl = kmeans.labels_
    # print("lunchlbl=", lnchlbl)

    ## Reading of the Dataet
    datafin_nutr = pd.read_csv('nutrition_distriution.csv')
    ## train set
    datafin_nutr = datafin_nutr.T
    # print("datafin_nutr=",datafin_nutr)

    weightcat = datafin_nutr.iloc[wl]
    # print("wlcat=", weightlosscat)
    weightcat = weightcat.T

    # Converting numpy array
    weightcatDdata = weightcat.to_numpy()

    weightcat = weightcatDdata[0:, 0:len(weightcatDdata)]

    # print("wlcatdata=", weightlosscat)

    weightcatfin = np.zeros((len(weightcat) * 5, cols), dtype=np.float32)
    # print("weightlossfin=",weightlossfin)
    # print("weightlossfinlen=", len(weightlossfin))

    t = 0
    r = 0
    s = 0
    yt = []
    yr = []
    ys = []
    for zz in range(5):
        # print("zz=", zz)
        for jj in range(len(weightcat)):
            valloc = list(weightcat[jj])

            weightcatfin[t] = np.array(valloc)

            yt.append(lnchlbl[jj])
            t += 1

    X_test = np.zeros((len(weightcat), cols), dtype=np.float32)
    # print("X_test=",X_test)

    # print('####################')

    # randomforest
    for jj in range(len(weightcat)):
        valloc = list(weightcat[jj])
        X_test[jj] = np.array(valloc)

    X_train = weightcatfin  # Features
    y_train = yt  # Labels

    # Create a RF Classifier
    clf = RandomForestClassifier(n_estimators=100)

    # Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # print("y_pred=",y_pred)

    rec = []
    for i in range(len(y_pred)):
        # print("y=",y_pred[i])
        # print(LunchfoodseparatedID[i])
        if y_pred[i] == 2:
            rec.append(LunchfoodseparatedID[i])

    food_dataset = food_dataset.iloc[rec]
    print("Lunch")
    #print(food_dataset["Food_items"])

    fditems=food_dataset["Food_items"].tolist()
    
    lnchkst_random_elements = random.sample(fditems, 10)

    
    return lnchkst_random_elements


def Diet_Control_Dinner(wl, cols):
    food_dataset = pd.read_csv('food.csv', encoding="utf-8")
    rec_food = food_dataset

    Dinnerdata = food_dataset['Dinner']
    DinnerdataNumpy = Dinnerdata.to_numpy()

    Food_itemsdata = food_dataset['Food_items']

    Dinnerfoodseparated = []
    DinnerfoodseparatedID = []

    for i in range(len(Dinnerdata)):
        if DinnerdataNumpy[i] == 1:
            Dinnerfoodseparated.append(Food_itemsdata[i])
            DinnerfoodseparatedID.append(i)

    DinnerfoodseparatedIDdata = food_dataset.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    nutritions = [0] + val
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.iloc[nutritions]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T

    # converting into numpy array
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.to_numpy()

    # print("ti=", ti)

    ## K-Means Based  Dinner Food
    Datacalorie = DinnerfoodseparatedIDdata[0:, 1:len(DinnerfoodseparatedIDdata)]

    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

    XValu = np.arange(0, len(kmeans.labels_))

    # retrieving the labels for dinner food
    dnrlbl = kmeans.labels_

    ## Reading of the Dataet
    datafin_nutr = pd.read_csv('nutrition_distriution.csv')
    ## train set
    datafin_nutr = datafin_nutr.T
    # print("datafin_nutr=",datafin_nutr)

    weightcat = datafin_nutr.iloc[wl]
    # print("wlcat=", weightlosscat)
    weightcat = weightcat.T

    # Converting numpy array
    weightcatDdata = weightcat.to_numpy()

    weightcat = weightcatDdata[0:, 0:len(weightcatDdata)]

    # print("wlcatdata=", weightlosscat)

    weightcatfin = np.zeros((len(weightcat) * 5, cols), dtype=np.float32)
    # print("weightlossfin=",weightlossfin)
    # print("weightlossfinlen=", len(weightlossfin))

    t = 0
    r = 0
    s = 0
    yt = []
    yr = []
    ys = []
    print(len(dnrlbl))
    for zz in range(5):
        # print("zz=", zz)
        for jj in range(len(weightcat)):
            valloc = list(weightcat[jj])
            weightcatfin[t] = np.array(valloc)
            yt.append(dnrlbl[jj])
            t += 1

    X_test = np.zeros((len(weightcat), cols), dtype=np.float32)
    # print("X_test=",X_test)

    # print('####################')

    # randomforest
    for jj in range(len(weightcat)):
        valloc = list(weightcat[jj])
        X_test[jj] = np.array(valloc)

    X_train = weightcatfin  # Features
    y_train = yt  # Labels

    # print("x_train=",X_train)

    # print("y_train=", y_train)
    # print("y_trainlen=", len(y_train))

    # print("X_test=", X_test)

    # Create a RF Classifier
    clf = RandomForestClassifier(n_estimators=100)

    # Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # print("y_pred=",y_pred)

    rec = []
    for i in range(len(y_pred)):
        if y_pred[i] == 2:
            rec.append(DinnerfoodseparatedID[i])

    food_dataset = food_dataset.iloc[rec]
    print("Dinner")
    #print(food_dataset["Food_items"])

    fditems=food_dataset["Food_items"].tolist()
    
    dinr_random_elements = random.sample(fditems, 10)

    return dinr_random_elements
