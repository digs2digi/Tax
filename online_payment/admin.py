from django.contrib import admin
from tax.online_payment.models import Tax_transaction,BackOffice_dummy,Accounts_dummy,Online_Transaction_dummy

class TaxAdmin(admin.ModelAdmin):
	list_display=('customer_id','account_number','transaction_id','date','amount_paid')
	list_filter=['date']
	search_fields=['customer_id','account_number','transaction_id','date',]
    
class BOAdmin(admin.ModelAdmin):
	list_display=('customer_id',)

class AAdmin(admin.ModelAdmin):
	list_display=('account_number',)

class OTAdmin(admin.ModelAdmin):
	list_display=('transaction_id',)
     
admin.site.register(Tax_transaction,TaxAdmin)
admin.site.register(BackOffice_dummy,BOAdmin)
admin.site.register(Accounts_dummy,AAdmin)
admin.site.register(Online_Transaction_dummy,OTAdmin)
