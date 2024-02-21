from rest_framework import serializers
from Users.models import User,UserConfirmation

class SignUpSerializer(serializers.ModelSerializer):
	guid=serializers.UUIDField(read_only=True)

	def __init__(self,*args,**kwargs):
		super(SignUpSerializer,self).__init__(*args,**kwargs)
		self.fields["emailPhonenumber"]=serializers.CharField(required=False)

		class Meta:
			model=User
			fields=(
				"guid",
				"authType",
				"authStatus")
			extra_kwars={
				'authType':{'read_only':True,'required':False},
				'authStatus':{'read_only':True,'required':False}
			}
	@staticmethod
	def auth_validate(attrs):
		userInput=str(attrs.get('emailPhonenumber'))