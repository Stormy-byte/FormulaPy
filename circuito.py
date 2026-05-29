import fastf1
import matplotlib.pyplot as plt

def stampaCircuito(anno, event_name, sessione):
    sessione.load(telemetry=True, laps=True, weather=False, messages=False)

    results = sessione.results.copy()
    results['Position'] = results['Position'].astype(int)

    # vincitore
    driver = results[results['Position'] == 1].iloc[0]
    abbr = driver['Abbreviation']

    lap = sessione.laps.pick_drivers(abbr).pick_fastest()

    try:
        pos_data = lap.get_pos_data()
        x = pos_data['X']
        y = pos_data['Y']
    except Exception as e:
        print(f"Impossibile caricare la telemetria: {e}")
        return

    circuit_info = sessione.get_circuit_info()
    corners = circuit_info.corners

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color='black')
    plt.plot(corners['X'], corners['Y'], 'ro')

    for _, row in corners.iterrows():
        plt.text(row['X'], row['Y'], str(row['Number']), fontsize=8)

    plt.title(f"Circuito di {sessione.event['EventName']} {anno}")
    plt.axis('equal')
    plt.axis('off')
    plt.show()