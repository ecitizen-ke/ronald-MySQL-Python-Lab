from flask import Blueprint, request, jsonify
from app.models import State

state_bp = Blueprint("state_bp", __name__)


@state_bp.route("/api/v1/states", methods=["GET"])
def getStates():
    # initialize the user object and then call the required method
    states= State().get_States()
    if states:
        return jsonify({"message": "states displayed successfully", "status": 201,"result":states})
    else:
        return jsonify({"message": "states not displayed", "status": 400})

@state_bp.route("/api/v1/states/create", methods=["POST"])
def register():
    # initialize the user object
    state = State()

    # Get data from the rsequest object
    data = request.get_json()
    # print("data:",request.get_data())
    
    name = data.get("name") 
    abbreviation = data.get("abbreviation")
    capital = data.get("capital")
    population = data.get("population")
    year_admitted = data.get("year_admitted")

    # invoke create user method
    result = state.create(name, abbreviation, capital, population, year_admitted)
    if result == False:
        return jsonify({"message": "State already exists in the database.", "status": 500})
    return jsonify({"message": "user registered successfully", "status": 201})

@state_bp.route("/api/v1states/filter", methods=["GET"])
def filterStates_name_A():
    """
    filter states by names starting with letter A
    """
    # initialize the user object
    state = State()
    states= state.list_states_starting_with_A()
    if states:
        return jsonify({"message": "states displayed successfully", "status": 201,"result":states})
    else:
        return jsonify({"message": "states not displayed", "status": 400})

@state_bp.route("/api/v1/states/filter/name_asc", methods=["GET"])
def filterStates_asc():
    """
    filter states by name in ascending order
    """
    # initialize the user object
    state = State()
    states= state.filter_states_by_name_asc()
    return jsonify(states)

@state_bp.route("/api/v1/states/update/population", methods=["PATCH"])
def update_population_by_id():
    state = State()
    data = request.get_json()
    id = data.get('id')
    population = data.get('population')
    states = state.update_states_population(id, population)
    return states

@state_bp.route("/api/v1/states/delete", methods=["DELETE"])
def deleteState():
    state = State()
    data = request.get_json()
    id = data.get('id')
    states = state.delete_state(id)
    if states:
        return jsonify({"message": "State deleted successfully", "status": 200})
    else:
        return jsonify({"message": "State not found", "status": 404})
@state_bp.route("/api/v1/states/populous", methods=["GET"])
def get_populous_state():
    state = State()
    popular_state = state.get_highest_populated_state()
    if popular_state:
         return jsonify({"message": "Popular state", "status": 200, "result": popular_state})
    else:
        return jsonify({"message": "No state found with the highest population", "status": 404})

@state_bp.route("/api/v1/states/search", methods=["GET"])
def search_state():
    """search state by name"""
    state =State()
    data = request.get_json()
    name = data.get('name')  # assuming 'name' is the key in the request JSON body that contains the state name.
    result= state.search_states(name)
    if result:
        return jsonify({"state": result, "code": 200})
    else:
        return jsonify({"message": "state not found", "code": 404})
        
@state_bp.route("/api/v1/states/capital", methods=["GET"])
def states_capital():
    state = State()
    capitals = state.list_state_capitals()
    if capitals:
        return jsonify({"message": "capitals displayed successfully", "status": 201,"result": capitals})
    else:
        return jsonify({"message": "capitals not displayed", "status": 400})

@state_bp.route("/api/v1/states/average_population", methods=["GET"])
def average_states_population():
    """
    this function calculate and return the average population of states
    """
    state = State()
    average_pop = state.average_population()
    if average_pop:
        return jsonify({"message": "average population displayed successfully", "status": 201,"result": average_pop})
    else:
        return jsonify({"message": "average population not displayed", "status": 400})

@state_bp.route("/api/v1/states/range_population", methods=["GET"])
def range_of_population():
    """
    that counts the number of states within 
a population between 1,000,000 and 5,000,000 people
    """
    state = State()
    range_count = state.count_population_range()
    if range_count:
        return jsonify({"message": "range of population displayed successfully", "status": 201,"result": range_count})
    else:
        return jsonify({"message": "range of population not displayed", "status": 400})

@state_bp.route("/api/v1/states/join_state_capital", methods=["GET"])
def joinStateCapital():
    join_record = State().join_states_capital()
    if join_record:
        return jsonify({"message": "joined records displayed successfully", "status": 201,"result": join_record})
    else:
        return jsonify({"message": "joined records not displayed", "status": 400})
   

@state_bp.route("/api/v1/states/searchByName",methods=["POST"])
def searchStateByName():
    """
    this functions searches for state details by name
    """
    state=State()

    data=request.get_json()

    name=data.get("name")

    result=state.search_State_By_Name(name)

    if result:
        return jsonify({"message": "search successful", "status": 201,"result":result})
    else:
        return jsonify({"message": "search unsuccessful", "status": 400,"result":result})
    
@state_bp.route("/api/v1/states/admitedBtw1750and1850",methods=["GET"])
def stateAdmittedBetween1750and1850():  
    """
    this functions searches for state details admitted between 1750 and 1850
    """
    state=State() 
    result = state.state_admitted_btw_1750_AND_1850()
    if result:
        return jsonify({"message": "search successful", "status": 201,"result":result})
    else:
        return jsonify({"message": "search unsuccessful", "status": 400,"result":result})
    