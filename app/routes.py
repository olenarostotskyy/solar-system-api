from app import db
from app.models.planets import Planet
from flask import Blueprint, jsonify, make_response,abort, request
    
# planets = [
#     Planet(1,"Mercury", {"mass":123, "distance_from_sun": 456, "num_moon": 1},"gray"),
#     Planet(2,"Venus", {"mass":333, "distance_from_sun": 555, "num_moon": 3},"white"),
#     Planet(3,"Earth", {"mass":444, "distance_from_sun": 567, "num_moon": 0},"blue"),
# ]

planets_bp = Blueprint("planets",__name__, url_prefix="/planets")
@planets_bp.route("", methods = ["POST"])
def create_one_planet():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or "num_moon" not in request_body or "color" not in request_body:
        return make_response(f"Invalid request", 400)
    
    new_planet = Planet(
                name = request_body["name"],
                description = request_body["description"],
                num_moon = request_body["num_moon"],
                color = request_body["color"],
                )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.id} is created",201)


@planets_bp.route("",methods=["GET"])
def get_all_planets():
    # building planet response
    planets=Planet.query.all()
    planet_response=[]
    for planet in planets:
        planet_response.append(
            {
            "id": planet.id,
            "name": planet.name,
            "description" : planet.description,
            "num_moon": planet.num_moon,
            "color":planet.color
            }
        )
    return jsonify(planet_response)

# @planets_bp.route("", methods =["GET"])

# #helper function to validate planet id and handling errors
# @planets_bp.route("/<planet_id>", methods=["GET"]) # decorator that transform the function follows into andpoint

# def validate_planet(planet_id):
#     # handling invalid planet_id input
#     try:
#         planet_id=int(planet_id)
#     except:
#         abort(make_response({"msg":f"{planet_id} is invalid id "},400 ))   
#     #read planet id 
#     for planet in planets:
#         if planet.id==planet_id:
#             return {
#                 "id" : planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "color":planet.color
#             }, 200

#     # returning 400 for non-existing planet     
#     abort(make_response({"msg":f"planet {planet_id} is not found"}, 404))   

# #read all the planets
# def get_all_planets():
#     all_planet = []
#     for planet in planets:
#         all_planet.append({
#             "id" : planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "color":planet.color
#         })
#     return jsonify(all_planet) , 200


# #read one planet
# def read_one_planet(planet_id):
#     planet=validate_planet(planet_id)
#     return planet    



