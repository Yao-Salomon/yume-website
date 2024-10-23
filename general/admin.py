from django.contrib import admin
from .models import Activite, TypeFormulaire, Utilisateur, Utilitaire,Temoignage, Valeur,Client
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms


class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Mot de Passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmation du mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Utilisateur
        fields = ('email', 'password','slug','first_name','last_name',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UtilisateurAdmin(BaseUserAdmin):
    
    view_on_site=True
    prepopulated_fields={"slug":("email",)}
     # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_active','is_admin')
    list_filter = ('is_admin','is_active')
    fieldsets = (
        ("Sécurité", {'fields': ('email', 'password','is_client',)}),
        ('Personal info', {'fields': ('slug','numero','about','first_name','last_name',)}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ("Sécurité", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','slug','is_client')}
        ),
        ('Personal info', {'fields': ('slug','numero','about','first_name','last_name',)}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class UtilitaireAdmin(admin.ModelAdmin):
    pass

class TemoignageAdmin(admin.ModelAdmin):
    pass

class ValeurAdmin(admin.ModelAdmin):
    pass
class ActiviteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Temoignage,TemoignageAdmin)
admin.site.register(Utilisateur,UtilisateurAdmin)
admin.site.register(Utilitaire, UtilitaireAdmin)
admin.site.register(Valeur,ValeurAdmin)
admin.site.register(Client)
admin.site.register(Activite,ActiviteAdmin)
admin.site.register(TypeFormulaire)

admin.site.unregister(Group)