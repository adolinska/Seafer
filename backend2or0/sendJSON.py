import requests
import json

oldMockupData = {
  "ships": [
    {
      "name": "Evergreen",
      "registration_id": "EGR-123",
      "position": {
        "x": 25.032964,
        "y": 121.565427
      },
      "course": 250,
      "speed": 20,
      "start_port": "Port of Shanghai",
      "end_port": "Port of Los Angeles",
      "last_update": "2023-03-25T08:30:15"
    },
    {
      "name": "Emma Maersk",
      "registration_id": "MAE-456",
      "position": {
        "x": 56.158515,
        "y": 10.210854
      },
      "course": 180,
      "speed": 18,
      "start_port": "Port of Rotterdam",
      "end_port": "Port of Singapore",
      "last_update": "2023-03-25T08:30:20"
    },
    {
      "name": "MSC Oscar",
      "registration_id": "MSC-789",
      "position": {
        "x": 51.507222,
        "y": -0.127758
      },
      "course": 90,
      "speed": 22,
      "start_port": "Port of Hong Kong",
      "end_port": "Port of Hamburg",
      "last_update": "2023-03-25T08:30:25"
    },
    {
      "name": "CMA CGM Marco",
      "registration_id": "CMA-321",
      "position": {
        "x": 35.689487,
        "y": 139.691711
      },
      "course": 270,
      "speed": 15,
      "start_port": "Port of Tokyo",
      "end_port": "Port of Le Havre",
      "last_update": "2023-03-25T08:30:30"
    },
    {
      "name": "Maersk Mc-Kinney",
      "registration_id": "MAE-654",
      "position": {
        "x": 37.77493,
        "y": -122.41942
      },
      "course": 120,
      "speed": 12,
      "start_port": "Port of LA",
      "end_port": "Port of Tokyo",
      "last_update": "2023-03-25T08:30:35"
    },
    {
      "name": "Cosco Shipping",
      "registration_id": "COS-987",
      "position": {
        "x": 31.224361,
        "y": 121.475104
      },
      "course": 300,
      "speed": 18,
      "start_port": "Port of Ningbo",
      "end_port": "Port of Felixstowe",
      "last_update": "2023-03-25T08:30:40"
    },
    {
      "name": "Maersk Mc-Kinney",
      "registration_id": "MAE-654",
      "position": {
        "x": 37.77493,
        "y": -122.41942
      },
      "course": 120,
      "speed": 12,
      "start_port": "Port of LA",
      "end_port": "Port of Tokyo",
      "last_update": "2023-03-25T08:30:35"
    },
    {
      "name": "Cosco Shipping",
      "registration_id": "COS-987",
      "position": {
        "x": 31.224361,
        "y": 121.475104
      },
      "course": 300,
      "speed": 18,
      "start_port": "Port of Ningbo",
      "end_port": "Port of Felixstowe",
      "last_update": "2023-03-25T08:30:40"
    },
    {
      "name": "MSC Zoe",
      "registration_id": "MSC-852",
      "position": {
        "x": 53.551086,
        "y": 9.993682
      },
      "course": 180,
      "speed": 10,
      "start_port": "Port of Algeciras",
      "end_port": "Port of Rotterdam",
      "last_update": "2023-03-25T08:30:45"
    },
    {
      "name": "OOCL Hong Kong",
      "registration_id": "OOCL-159",
      "position": {
        "x": 22.319303,
        "y": 114.169361
      },
      "course": 0,
      "speed": 16,
      "start_port": "Port of Shenzhen",
      "end_port": "Port of Rotterdam",
      "last_update": "2023-03-25T08:30:50"
    }
  ]
}

newMockupData = {
  "ships": [
    {
      "name": "Evergreen",
      "registration_id": "EGR-123",
      "position": {
        "x": 25.032964,
        "y": 121.565427
      },
      "course": 250,
      "speed": 20,
      "start_port": "Port of Shanghai",
      "end_port": "Port of Los Angeles",
      "last_update": "2023-03-25T08:30:15"
    },
    {
      "name": "Emma Maersk",
      "registration_id": "MAE-456",
      "position": {
        "x": 56.158515,
        "y": 10.210854
      },
      "course": 180,
      "speed": 18,
      "start_port": "Port of Rotterdam",
      "end_port": "Port of Singapore",
      "last_update": "2023-03-25T08:30:20"
    },
    {
      "name": "MSC Oscar",
      "registration_id": "MSC-789",
      "position": {
        "x": 51.507222,
        "y": -0.127758
      },
      "course": 90,
      "speed": 22,
      "start_port": "Port of Hong Kong",
      "end_port": "Port of Hamburg",
      "last_update": "2023-03-25T08:30:25"
    },
    {
      "name": "CMA CGM Marco",
      "registration_id": "CMA-321",
      "position": {
        "x": 35.689487,
        "y": 139.691711
      },
      "course": 270,
      "speed": 15,
      "start_port": "Port of Tokyo",
      "end_port": "Port of Le Havre",
      "last_update": "2023-03-25T08:30:30"
    },
    {
      "name": "Maersk Mc-Kinney",
      "registration_id": "MAE-654",
      "position": {
        "x": 37.77493,
        "y": -122.41942
      },
      "course": 120,
      "speed": 12,
      "start_port": "Port of LA",
      "end_port": "Port of Tokyo",
      "last_update": "2023-03-25T08:30:35"
    },
    {
      "name": "Cosco Shipping",
      "registration_id": "COS-987",
      "position": {
        "x": 31.224361,
        "y": 121.475104
      },
      "course": 300,
      "speed": 18,
      "start_port": "Port of Ningbo",
      "end_port": "Port of Felixstowe",
      "last_update": "2023-03-25T08:30:40"
    },
    {
      "name": "Maersk Mc-Kinney",
      "registration_id": "MAE-654",
      "position": {
        "x": 37.77493,
        "y": -122.41942
      },
      "course": 120,
      "speed": 12,
      "start_port": "Port of LA",
      "end_port": "Port of Tokyo",
      "last_update": "2023-03-25T08:30:35"
    },
    {
      "name": "Cosco Shipping",
      "registration_id": "COS-987",
      "position": {
        "x": 31.224361,
        "y": 121.475104
      },
      "course": 300,
      "speed": 18,
      "start_port": "Port of Ningbo",
      "end_port": "Port of Felixstowe",
      "last_update": "2023-03-25T08:30:40"
    },
    {
      "name": "MSC Zoe",
      "registration_id": "MSC-852",
      "position": {
        "x": 53.551086,
        "y": 9.993682
      },
      "course": 180,
      "speed": 10,
      "start_port": "Port of Algeciras",
      "end_port": "Port of Rotterdam",
      "last_update": "2023-03-25T08:30:45"
    },
  ]
}

res = requests.post('http://172.28.0.22:5000/sendJson', json=oldMockupData)
if res.ok:
    print(res.json())

res = requests.post('http://localhost:5000/sendJson', json=newMockupData)
if res.ok:
    print(res.json())
