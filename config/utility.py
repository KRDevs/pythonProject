import re
from rest_framework.exceptions import ValidationError

emailRegex=re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
phoneNumberRegex=re.compile(r"^998[0-9]{9}$")

def check_email_or_phone(emailOrPhone):
	if re.fullmatch(emailRegex,emailOrPhone):
		emailOrPhone="email"
	elif re.fullmatch(phoneNumberRegex,emailOrPhone):
		emailOrPhone="phone"
	else:
		data={
			"success":False,
			"message":"Email yoki telefon raqam kiriting!"
		}