"""
Creators: Pedro Victor and Beatriz Soares
Date: 23 May 2022
Create API
"""
from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with accident_severity equal to 0
'''
def test_get_accident_severity_low():

    person = {
        "Age_band_of_driver": '18-30',
        "Sex_of_driver": 'Male',
        "Educational_level": 'Unknown',
        "Vehicle_driver_relation": 'Unknown',
        "Driving_experience": 'Unknown',
        "Lanes_or_Medians": 'Two-way (divided with broken lines road marking)',
        "Types_of_Junction": 'Y Shape',
        "Road_surface_type": 'Asphalt roads',
        "Light_conditions": 'Darkness - lights lit',
        "Weather_conditions": 'Raining',
        "Type_of_collision": 'Collision with pedestrians',
        "Vehicle_movement": 'Going straight',
        "Pedestrian_movement": 'Not a Pedestrian',
        "Cause_of_accident": 'Driving under the influence of drugs'
    }

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "Accident_severity: 0"
'''
# a unit test that tests the status code and response 
# for an instance with accident_severity equal to 1
'''
def test_get_accident_severity_medium():

    person = {
        "Age_band_of_driver": '18-30',
        "Sex_of_driver": 'Male',
        "Educational_level": 'Junior high school',
        "Vehicle_driver_relation": 'Employee',
        "Driving_experience":  '1-2yr',
        "Lanes_or_Medians": 'other',
        "Types_of_Junction": 'No junction',
        "Road_surface_type": 'Asphalt roads',
        "Light_conditions": 'Daylight',
        "Weather_conditions": 'Normal',
        "Type_of_collision": 'Collision with roadside objects',
        "Vehicle_movement": 'Going straight',
        "Pedestrian_movement": 'Not a Pedestrian',
        "Cause_of_accident": 'Changing lane to the left'
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Accident_severity: 1"
'''    
# a unit test that tests the status code and response 
# for an instance with accident_severity equal to 2
client1 = TestClient(app)
def test_accident_severity_high():
    
    person = {
        "Age_band_of_driver": '18-30',
        "Sex_of_driver": 'Male',
        "Educational_level": 'Above high school',
        "Vehicle_driver_relation": 'Employee',
        "Driving_experience": '1-2yr',
        "Lanes_or_Medians": 'Unknown',
        "Types_of_Junction": 'No junction',
        "Road_surface_type": 'Asphalt roads',
        "Light_conditions": 'Daylight',
        "Weather_conditions": 'Normal',
        "Type_of_collision": 'Collision with roadside-parked vehicles',
        "Vehicle_movement": 'Going straight',
        "Pedestrian_movement": 'Not a Pedestrian',
        "Cause_of_accident": 'Moving Backward'
    }

    r = client1.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Accident_severity: 2"
    

