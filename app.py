from fastapi import FastAPI
from db import (
    dodaj_zadanie,
    pokaz_zadania,
    zmien_status_zadania,
    usun_zadanie,
    znajdz_zadanie,
)

app = FastAPI()


@app.get("/zadania")
def pobierz_zadania():
    zadania = pokaz_zadania()
    return {"zadania": zadania}


@app.post("/zadania")
def nowe_zadanie(nazwa: str, status: str):
    dodaj_zadanie(nazwa, status)
    return {"message": f"Dodano zadnie: {nazwa}"}


@app.delete("/zadania/{id}")
def usun(id: int):
    if not znajdz_zadanie(id):
        return {"error": "Nie ma zadania o takim id"}
    usun_zadanie(id)
    return {"message": f"Zadanie {id} usunięte"}


@app.put("/zadania/{id}")
def zmien_status(id: int, status: str):
    if not znajdz_zadanie(id):
        return {"error": "Nie ma zadania o takim id"}
    zmien_status_zadania(status, id)
    return {"message": f"Status zadania {id} zmieniony na {status}"}
