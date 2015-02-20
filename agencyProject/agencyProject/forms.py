from django import forms


class agencyForm(forms.Form):

    first_name = forms.CharField(label = "First Name")
    last_name = forms.CharField(label = "Last Name")
    email = forms.EmailField(label = "Email")
    phone_number = forms.IntegerField(label = "Phone Number")


class share_form (forms.Form):
    sender_email = forms.EmailField(label = "Your Email")
    receiver_email = forms.EmailField(label = "Friend's Email")
    sender_phone = forms.CharField(label = "Your Phone")
    receiver_phone = forms.CharField(label = "Friend's Phone")


class ReviewForm (forms.Form):
    name = forms.CharField(label="Your Name: ")
    title = forms.CharField(label="Your job title: ")
    business = forms.CharField(label="Your business: ")
    review = forms.CharField(label="Your Review of Hello World Advertising Agency: ", widget=forms.Textarea)