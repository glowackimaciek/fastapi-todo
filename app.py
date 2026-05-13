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
