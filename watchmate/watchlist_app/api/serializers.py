from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatforms
from django.utils.timezone import now


# ************************************** model serializer **************************************

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'
        # fields = ['id', 'title', 'storyline']        #you can try any of them
        # exclude = ['active']

class StreamPlatformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatforms
        fields = '__all__'

# ********************************  filed level validations ****************************************************

    # def validate_title(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("title is too short")
    #     else:
    #         return value
        
# ********************************* object level validation ************************************************

    # def validate(self, data):
    #     if data['title'] == data['storyline']:
    #         raise serializers.ValidationError("title and storyline should be different")
    #     return data

    # def validate(self, data):
    #     if data['title'].isdigit():
    #         raise serializers.ValidationError("title should be string")
    #     return data

# ************************************** end model serializer **************************************

# ************************ validator ************************
# def title_validator(value):
#     if len(value) > 10:
#         raise serializers.ValidationError("title should be less than 10 charachters")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(validators=[title_validator]) #here we passed above title_validate function for validation
#     storyline = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Watchlist.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
    
# ********************************  filed level validations ****************************************************

    # def validate_title(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("title is too short")
    #     else:
    #         return value
        
# ********************************* object level validation ************************************************

    # def validate(self, data):
    #     if data['title'] == data['storyline']:
    #         raise serializers.ValidationError("title and storyline should be different")
    #     return data

    # def validate(self, data):
    #     if data['title'].isdigit():
    #         raise serializers.ValidationError("title should be string")
    #     return data