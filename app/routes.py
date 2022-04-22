from flask import Blueprint, jsonify

class Planet:
    def __init__(self,id, name, description):
        self.id = id
        self.name = name
        self.description = description
    
planets = [
    Planet(1,"Mercury", {"mass":123, "distance_from_sun": 456, "num_moon": 1}),
    Planet(2,"Venus", {"mass":333, "distance_from_sun": 555, "num_moon": 3}),
    Planet(3,"Earth", {"mass":444, "distance_from_sun": 567, "num_moon": 0}),
]

planets_bp = Blueprint("planets",__name__, url_prefix="/planets")

@planets_bp.route("", methods =["GET"])

def get_all_planets():
    all_planet = []
    for planet in planets:
        all_planet.append({
            "id" : planet.id,
            "name": planet.name,
            "description": planet.description
        })
    return jsonify(all_planet) , 200
