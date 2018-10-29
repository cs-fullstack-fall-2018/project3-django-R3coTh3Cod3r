from django import forms
from .models import ExpenseModel, setupUser


class FormsForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = {'username', 'foreign_expense_user','balance','emergency_fund_status','withdrawls','deposit','amount','statedDate' }
        order_fields = {'username','balance','emergency_fund_status','widthdrawls','deposit','amount','statedDate'}
        widgets = {
            'foreign_expense_user': forms.HiddenInput()
        }
class UserForm(forms.ModelForm):
    class Meta:
        model= setupUser
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()

        }
