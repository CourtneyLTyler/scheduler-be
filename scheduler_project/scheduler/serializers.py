from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # section_red = serializers.HyperlinkedRelatedField(
    #     view_name='section_red_detail',
    #     many=True,
    #     read_only=True
    # )
    # section_orange = serializers.HyperlinkedRelatedField(
    #     view_name='section_orange_detail',
    #     many=True,
    #     read_only=True
    # )
    # section_yellow = serializers.HyperlinkedRelatedField(
    #     view_name='section_yellow_detail',
    #     many=True,
    #     read_only=True
    # )
    # section_green = serializers.HyperlinkedRelatedField(
    #     view_name='section_green_detail',
    #     many=True,
    #     read_only=True
    # )
    # section_blue = serializers.HyperlinkedRelatedField(
    #     view_name='section_blue_detail',
    #     many=True,
    #     read_only=True
    # )
    # section_purple = serializers.HyperlinkedRelatedField(
    #     view_name='section_purple_detail',
    #     many=True,
    #     read_only=True
    # )
    # employee = serializers.HyperlinkedRelatedField(
    #     view_name='employee_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'position', 'photo_url', 'sales', 'rating')

