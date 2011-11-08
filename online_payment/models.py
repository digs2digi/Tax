from django.db import models
import datetime

class Taxtype(models.Model):
	tax_type_id=models.IntegerField(primary_key=True)
	tax_type_name=models.CharField(max_length=30)

class BackOffice_dummy(models.Model):
	customer_id=models.IntegerField(primary_key=True)
	customer_name=models.CharField(max_length=50)
	customer_age=models.IntegerField()
	def __unicode__(self):
		return "%s " % self.customer_id
	
class Accounts_dummy(models.Model):
	account_number=models.IntegerField(primary_key=True)
	customer_id=models.ForeignKey(BackOffice_dummy,to_field='customer_id')
	def __unicode__(self):
		return "%s " % self.account_number

class Online_Transaction_dummy(models.Model):
	transaction_id=models.IntegerField(primary_key=True)
	account_number=models.ForeignKey(Accounts_dummy,to_field='account_number')
	def __unicode__(self):
		return "%s " % self.transaction_id

class Tax_transaction(models.Model):
	customer_id=models.ForeignKey(BackOffice_dummy,to_field='customer_id')
	account_number=models.ForeignKey(Accounts_dummy,to_field='account_number')
	tax_type_id=models.ForeignKey(Taxtype,to_field='tax_type_id')
	transaction_id=models.ForeignKey(Online_Transaction_dummy,to_field='transaction_id')
	date=models.DateField()
	amount_paid=models.IntegerField()

