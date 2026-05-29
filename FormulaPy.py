import fastf1
from fastf1 import plotting
import pandas as pd
import os
import shutil
import circuito
from rich.console import Console
import logging
logging.disable(logging.INFO)

console = Console(force_terminal=True)

def pulisci():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

cache_path = 'cache'

if not os.path.exists(cache_path):
    os.makedirs(cache_path)

console.print("BENVENUTO IN FORMULAPY", style="bold red")
fastf1.Cache.enable_cache(cache_path)

console.print("Che anno ti interessa?", style="bold")
anno = int(input())

schedule = fastf1.get_event_schedule(anno, include_testing=False)
for i, (_, row) in enumerate(schedule.iterrows()):
    print(f"{i+1}. {row['EventName']} ({row['Location']})")

console.print("E la gara?", style="bold")
ngara = int(input())
print("Caricamento")
event_name = schedule.iloc[ngara - 1]['EventName']

session = fastf1.get_session(anno, event_name, 'R')
session.load(telemetry=True, laps=True)
pulisci()

console.print(f"\n[bold]Risultati - {event_name} {anno}[/bold]\n")
results = session.results[['Position', 'FullName', 'TeamName', 'GridPosition', 'Points']].copy()
results['Position'] = results['Position'].astype(int)
results = results.sort_values('Position')

for _, row in results.iterrows():
    try:
        colore = plotting.get_team_color(row['TeamName'], session=session)
    except Exception:
        colore = "#FFFFFF"
    console.print(
        f"{int(row['Position']):>2}. {row['FullName']:<25} {row['TeamName']:<25} "
        f"Grid: {int(row['GridPosition']):>2}   Punti: {row['Points']}",
        style=f"bold {colore}"
    )

if anno >= 2018 and anno <= 2025:
    circuito.stampaCircuito(anno, event_name, session)

ris = None
while ris not in ['y', 'Y', 'n', 'N']:
    console.print("\nVuoi cancellare tutta la cache? y/n", style="bold")
    ris = input()
    if ris in ['y', 'Y']:
        if os.path.exists(cache_path):
            shutil.rmtree(cache_path)
            console.print("Cache cancellata", style="bold red")
            exit()
    elif ris in ['n', 'N']:
        console.print("Cache non cancellata", style="bold green")
        exit()
    else:
        console.print("Scelta non valida", style="red")
