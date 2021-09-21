
# helper

def team_helper(team) -> dict:
    return {
        "_id": team["_id"],
        "name": team["name"],
        "overall_ga": team["overall_ga"],
        "overall_gs": team["overall_gs"],
        "points": team["points"],
        "round": team["round"],
        "season": team["position"],
        "squad": team["squad"],
    }


# retrieve all teams in database
async def retrieve_teams():
    teams = []
    async for team in team_collection.find():
        teams.append(team_helper(team))
    return teams

# Add a new student into to the database
async def add_team(team_data: dict) -> dict:
    team = await team_collection.insert_one(team_data)
    new_team = await team_collection.find_one({"_id": team.inserted_id})
    return team_helper(new_team)

# Retrieve a team with a matching ID
async def retrieve_team(name: str) -> dict:
    team = await team_collection.find_one({"name": ObjectId(name)})
    if team:
        return team_helper(team)

# Delete a team from the database
async def delete_team(name: str):
    team = await team_collection.find_one({"name": ObjectId(name)})
    if team:
        await team_collection.delete_one({"name": ObjectId(name)})
        return True