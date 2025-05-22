from fastapi import FastAPI
from pydantic import BaseModel
from club_selector import choisir_club

app = FastAPI()

class ClubRequest(BaseModel):
    nom_club: str = "Paris Rue Froment"

@app.post("/choisir-club")
def choisir_club_api(request: ClubRequest):
    success = choisir_club(request.nom_club)
    if success:
        return {"status": "success", "club": request.nom_club}
    else:
        return {"status": "error", "message": "Club non trouvé"}
