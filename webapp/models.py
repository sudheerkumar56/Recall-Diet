from django.db import models

class users(models.Model):
	name=models.CharField(max_length=149);
	email=models.CharField(max_length=149);
	password=models.CharField(max_length=149);
	phone=models.CharField(max_length=149);
	gender=models.CharField(max_length=149);
	Height=models.CharField(max_length=149);
	weight=models.CharField(max_length=149);
	type_diet=models.CharField(max_length=149);
	age=models.CharField(max_length=149);
	age_cat=models.CharField(max_length=149);

class food_details(models.Model):
	food_name=models.CharField(max_length=149);
	v_a=models.FloatField();
	v_b=models.FloatField();
	v_c=models.FloatField();
	v_b12=models.FloatField();
	carbs=models.FloatField();
	fiber=models.FloatField();
	sugars=models.FloatField();
	calcium=models.FloatField();
	iron=models.FloatField();
	iodine=models.FloatField();

class diary(models.Model):
	email=models.CharField(max_length=149);
	food_name=models.CharField(max_length=149);
	dat_e=models.CharField(max_length=149);
	wee_k=models.CharField(max_length=149);
	mont_h=models.CharField(max_length=149);
	v_a=models.FloatField();
	v_b=models.FloatField();
	v_c=models.FloatField();
	v_b12=models.FloatField();
	carbs=models.FloatField();
	fiber=models.FloatField();
	sugars=models.FloatField();
	calcium=models.FloatField();
	iron=models.FloatField();
	iodine=models.FloatField();
	tim_e=models.CharField(max_length=149);





class dataset(models.Model):
	age=models.CharField(max_length=149);
	gender=models.CharField(max_length=149);
	period=models.CharField(max_length=149);
	typ_e=models.CharField(max_length=149);
	v_a=models.FloatField();
	v_b=models.FloatField();
	v_c=models.FloatField();
	v_b12=models.FloatField();
	carbs=models.FloatField();
	fiber=models.FloatField();
	sugars=models.FloatField();
	calcium=models.FloatField();
	iron=models.FloatField();
	iodine=models.FloatField();



