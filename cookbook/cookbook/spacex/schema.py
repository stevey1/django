import graphene
from  graphene import ObjectType,  Int, String, Boolean
from graphene import relay
from django.test import TestCase, Client
class RocketType(ObjectType):
    rocket_id = Int()
    rocket_name = String()
    rocket_type = String()
    launch_year = String()

class LaunchType(ObjectType):
    flight_number = Int()
    mission_name = String()
    launch_year = String()
    launch_date_local = String()
    launch_success = Boolean()
    rock = RocketType()
    def resolve_flight_number(parent, info):
        return f"{parent.first_name} {parent.last_name}"

class SpacexQuery(graphene.ObjectType):
    launches = graphene.List(LaunchType)
    def resolve_launches(parent, info):
        client = Client()
        res = client.get(
            'https://api.spacexdata.com/v3/launches',
            format='json')
        print(res.context)
        return res.context

