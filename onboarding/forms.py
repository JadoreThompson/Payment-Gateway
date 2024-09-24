from django import forms


class SignUpForm(forms.Form):
    business_type_choices = [
        ('', 'Select a Business Type'),
        ('company', 'Company'),
        ('individual', 'Individual'),
        ('non_profit', 'Non Profit'),
    ]

    first_name = forms.CharField(label="First Name", max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-label"}))
    last_name = forms.CharField(label='Last Name', max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-label"}))
    phone = forms.CharField(label="Phone Number", required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-label'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-label'}))
    business_type = forms.ChoiceField(
        label='Business Type', choices=business_type_choices, required=True, widget=forms.SelectMultiple(attrs={'class': 'form-label'}))
