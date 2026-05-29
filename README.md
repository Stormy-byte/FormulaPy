# FormulaPy 🏎️

Programma da terminale per visualizzare i risultati e il circuito delle gare di Formula 1, usando i dati reali di FastF1.

## Requisiti

- Python 3.8+
- Windows / Linux / macOS

## Installazione

### 1. Clona il repository
```bash
git clone https://github.com/tuousername/formulapy.git
cd formulapy
```

### 2. Crea un ambiente virtuale
```bash
python -m venv venv
```

Attivalo:
- **Windows:** `venv\Scripts\activate`
- **Linux/macOS:** `source venv/bin/activate`

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Avvia il programma
```bash
python formula1.py
```

## Oppure scarica l'exe

Se sei su Windows puoi scaricare direttamente l'eseguibile dalla sezione [Releases](https://github.com/Stormy-byte/FormulaPy/releases) senza installare nulla.

## Funzionalità

- Visualizza il calendario di qualsiasi stagione di F1
- Mostra i risultati della gara con i colori delle scuderie
- Disegna il tracciato del circuito con i numeri delle curve
- Cache automatica per non riscaricare i dati già scaricati

## Dipendenze principali

- [FastF1](https://github.com/theOehrly/Fast-F1) — dati telemetrici F1
- [matplotlib](https://matplotlib.org/) — grafico del circuito
- [rich](https://github.com/Textualize/rich) — output colorato nel terminale
