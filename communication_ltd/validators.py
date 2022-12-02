import re

from django.core.exceptions import ValidationError
from django.utils.translation import ngettext as _

from . import configReadingHelper


config = configReadingHelper.read_config()


passwordLength = int(config['Password Management']['Password Length'])
#allowUpperCase = config['Password Management']['Allow Upper-case Letters in Password (y/n)']
#allowLowerCase = config['Password Management']['Allow Lower-case Letters in Password (y/n)']
#allowNumbers = config['Password Management']['Allow numbers in Password (y/n)']
#allowSpecialCharacters = config['Password Management']['Allow Special Characters in Password (y/n)']
passwordComplexity = config['Password Management']['Password Complexity']
passwordHistory = config['Password Management']['Password History']
passwordBlackList = config['Password Management']['Password Black List']
maxTryToLogin = int(config['Password Management']['Max Try to Login'])

class passwordComplexityValidator(object):
    def validate(self, password, user=None):
        if re.search("upperCase", passwordComplexity):
            UppercaseValidator(object)

        if re.search("lowerCase", passwordComplexity):
            LowercaseValidator(object)

        if re.search("numbers", passwordComplexity):
            NumberValidator(object)

        if re.search("specialCharacters", passwordComplexity):
            SymbolValidator(object)



class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )