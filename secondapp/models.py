from django.db import models
from django.core  import validators
# Create your models here.

class User2(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    auto_feild = models.AutoField(primary_key=True)
    big_integer_feild = models.BigIntegerField()
    binary_feild =  models.BinaryField()
    boolean_feild = models.BooleanField()
    char_feild = models.CharField(max_length=255)
    email_feild = models.EmailField()
    # comma_separated_field = models.CharField(
    #     validators = [comma_separated_validator],
    #     max_length=255
    # ) 
    date_feild = models.DateField()
    date_time_feild = models.DateTimeField()
    decimal_feild = models.DecimalField(max_digits=5,decimal_places=2)
    duration_feild = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    # file_path_field = models.FilePathField(path='/path/to/files/')
    img = models.ImageField(unique="images/")
    float_field = models.FloatField()
    # foreign_key = models.ForeignKey(OtherModel)
    generic_ip_address_field = models.GenericIPAddressField()
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    slug_feild = models.SlugField()
    small_integer_field = models.SmallIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    positive_big_integer_field= models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()

    def __str__(self):
        return self.name
    
