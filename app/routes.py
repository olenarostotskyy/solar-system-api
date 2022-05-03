from app import db
from app.models.planets import Planet
from flask import Blueprint, jsonify, make_response,abort, request

planets_bp = Blueprint("planets",__name__, url_prefix="/planets")

#Helper function to validate planet id and handling errors
def validate_planet(planet_id):
    # handling invalid planet_id input
    try:
        planet_id=int(planet_id)
    except:
        abort(make_response({"msg":f"Planet # {planet_id} is invalid id "},400))   
    #read planet id 
    planet=Planet.query.get(planet_id)
    if planet is None:
        abort(make_response({"msg":f"Planet # {planet_id} not found "},404)) 
    
    return planet

#Helper function to check if all attributes are entered in request body
def check_request_body():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or "num_moon" not in request_body or "color" not in request_body:
        abort(make_response(f"Invalid request ! name, description, color and num_moon are required", 400))
    return request_body

#Route functions:
@planets_bp.route("", methods = ["POST"])
def create_one_planet():
    request_body = check_request_body()
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

# decorator that transforms the function follows into endpoint
@planets_bp.route("/<planet_id>", methods=["GET"]) 
def get_one_planet(planet_id):
    planet=validate_planet(planet_id)
    return {
                "id" : planet.id,
                "name": planet.name,
                "description": planet.description,
                "num_moon": planet.num_moon,
                "color":planet.color
            }, 200

#update planet
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    planet=validate_planet(planet_id)
    request_body=check_request_body()

    planet.name=request_body["name"]
    planet.description=request_body["description"]
    planet.color=request_body["color"]
    planet.num_moon=request_body["num_moon"]

    db.session.commit()
    return (make_response(f"Planet # {planet_id}  successfully updated"), 200)


@planets_bp.route("/<planet_id>", methods=["DELETE"])    
def delete_one_planet(planet_id):
    planet=validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return (make_response(f"Planet # {planet_id}  successfully deleted"), 200)

