from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from core.models import PhonePrefix


def custom_sequence():
    '''
    Returns the next default value for the `client_code` field,
    starts from 1000
    '''
    # Retrieve a list of `User` instances, sort them by
    # the `client_code` field and get the largest entry
    largest = User.objects.all().order_by('client_code').last()
    if not largest:
        # largest is `None` if `User` has no instances
        # in which case we return the start value of 500
        return 1000
    # If an instance of `User` is returned, we get it's
    # `client_code` attribute and increment it by 1
    return largest.client_code + 1

class User(models.Model):

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email address!")])

    gender = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)]) # 1-male, 0-female
    phone_prefix = models.IntegerField(models.ForeignKey(PhonePrefix, on_delete=models.CASCADE))

    phone_regex = RegexValidator(
        regex=r'^[3-9]\d{6}$', 
        message="Phone number must be 7 digits and cannot start with 0, 1, or 2."
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=7,
        help_text="Enter a 7-digit phone number."
    )

    GOV_PREFIX_CHOICES = [
    (1, "AZE"),
    (2, "AA"),
    (3, "MYI"),
    (4, "DYI"),
]

    gov_prefix_id = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(4)], choices=GOV_PREFIX_CHOICES)
    
    
    def validate_gov_id(self, value):
        if self.gov_prefix_id == 1 and not (999999 < value <= 99999999):
            raise ValidationError(_('For AZE prefix, gov_id should have 8 digits.'))
        elif self.gov_prefix_id == 2 and not (99999 < value <= 9999999):
            raise ValidationError(_('For AA prefix, gov_id should have 7 digits.'))
        elif self.gov_prefix_id in [3, 4] and not (9999 < value <= 999999):
            raise ValidationError(_('For MYI/DYI prefix, gov_id should have 5 or 6 digits.'))

    gov_id = models.IntegerField(
        validators=[validate_gov_id],
        verbose_name=_("Government ID"),
        help_text=_("Enter your government ID."),
    )

    fin_code = models.CharField(max_length=7, unique=True, validators=[MinLengthValidator(7)])

    client_code = models.IntegerField(default = custom_sequence)
    monthyly_expenses = models.IntegerField()
    birth_date = models.DateField()
    is_active = models.IntegerField(default = 1)
    is_blocked = models.IntegerField(default = 0)

    selected_local_warehouse_id = models.IntegerField()

    