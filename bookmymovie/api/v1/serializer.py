from rest_framework import serializers

from theaters.models import Seat, Row


class SeatSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.number

    class Meta:
        model = Seat
        fields = ["number"]


class RowSerializer(serializers.ModelSerializer):
    seat_set = SeatSerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation[representation["serial"]] = representation["seat_set"]
        representation.pop("serial")
        representation.pop("seat_set")
        return representation

    class Meta:
        model = Row
        fields = ["serial", "seat_set"]


class ScreenSeatSerializer(serializers.Serializer):
    seats = RowSerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # iter_repr = iter(representation["seats"])
        # dict_representation = dict(zip(iter_repr, iter_repr))
        print(representation)
        return representation

    class Meta:
        fields = ["seats"]

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
