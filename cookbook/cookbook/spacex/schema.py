import graphene
from  graphene import ObjectType,  Int, String, Boolean,Field
from graphene import relay
from django.test import TestCase, Client
import json 
import http.client

class RocketType(ObjectType):
    rocket_id = String()
    rocket_name = String()
    rocket_type = String()

class LaunchType(ObjectType):
    flight_number = Int()
    mission_name = String()
    launch_year = String()
    launch_date_local = String()
    launch_success = Boolean()
    rocket = Field( RocketType)

class SpacexQuery(graphene.ObjectType):
    launch = Field(LaunchType, flightNumber=Int(required=True))
    launches = graphene.List(LaunchType)
    def resolve_launches(parent, info):
        connection = http.client.HTTPSConnection("api.spacexdata.com")
        connection.request("GET", "/v3/launches")
        response = connection.getresponse()
        data = response.read()
        connection.close()
        return json.loads(data)[:10]

   
    def resolve_launch(parent, info,flightNumber):
        connection = http.client.HTTPSConnection("api.spacexdata.com")
        connection.request("GET", "/v3/launches/{}".format(flightNumber))
        response = connection.getresponse()
        data = response.read()
        connection.close()
        return json.loads(data)
        '''
        return [{'flight_number':1,'mission_name':'miss',
            'launch_year':'1990','launch_date_local':'2010/1/1',
            'launch_success':True,'rock':None}]
        '''