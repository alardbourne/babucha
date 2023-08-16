class TownSerializer(serializers.ModelSerializer):
   name = serializers.CharField(allow_blank=True)

   class Meta:
      model = Town
      fields = ['id', 'writers', 'name']


class Writer(models.Model):
    firstname = models.CharField(max_length=100...)
    lastname = models.CharField(max_length=100...)
    patronymic = models.CharField(max_length=100...)
    birth_place = models.ForeignKey(to=Town...)
    birth_date = models.DateField(...)

Сериалайзер, который будет обслуживать все поля модели:


class WriterModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Writer
        fields = '__all__'

Сериалайзер, который будет обслуживать только поля firstname и lastname:


class WriterModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Writer
        fields = ['firstname', 'lastname']
