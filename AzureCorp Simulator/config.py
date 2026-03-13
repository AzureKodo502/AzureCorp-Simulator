class Config:
    """
    FILE DI CONFIGURAZIONE
    Contiene tutti i parametri globali della simulazione.
    Separare i dati dalla logica e permette di calibrare il modello senza toccare il codice.
    """

    # IMPOSTAZIONI SISTEMA
    SEED = None            # Imposta un numero (oppure lo stesso seed) per ripetere la stessa simulazione. None = Casuale.
    FILE_LOG = "report_dati_AzureCorp.csv" # Nome del file Excel/CSV di output
    SOGLIA_BANCAROTTA = 0.0 # Sotto questa cifra l'azienda fallisce

    # SCENARIO GENERALE
    Giorni = 365           # Durata temporale, modificabile a piacimento (Default 365 giorni)
    Budget = 20000.0       # Budget di partenza
    Meteo = 0.7            # Stabilità Meteo (0.0 stabile, 1.0 caotico)

    # PARAMETRI ECONOMICI
    Tasso_Interesse_Passivo = 0.20  # Percentuale per gli interessi (Default 20%)
    Probabilita_Evento = 0.04       # Percentuale di probabilità di Eventi (Default 4%)
    
    # COSTI FISSI
    Affitto_e_Tasse_Giornaliero = 150.0 

    # RISORSE AZIENDALI
    Ettari = 100
    Trattori = 3
    Operai = 6
    Stipendio_Giornaliero_Totale = Operai * 80.0  # Costo giornaliero degli operai
    Costo_Base_Carburante_Trattore = 100.0
    Manutenzione = 50.0

    # SETTORE DEL GRANO
    Ettari_Grano = 60
    Costo_Semina_Grano = 250.0
    Resa_Ettaro_Grano = 6000.0      # Kg/Ettaro ottimali
    Prezzo_Base_Grano = 0.28        # €/Kg
    Giorni_Necessari_Grano = 150    # Ciclo biologico

    # SETTORE DEL LATTE
    Mucche = 40
    Costo_Mangime = 15.0            # €/Giorno
    Litri_Prodotti = 28.0           # Litri al giorno
    Prezzo_Base_Latte = 0.70        # €/Litro
    Costo_Manutenzione_Stalla = 80.0

    # SETTORE DELL'UVA
    Ettari_Vino = 20
    Resa_Ettaro_Vino = 6000.0
    Conversione_Vino = 0.65         # Resa uva -> vino
    Costo_Imbottigliamento_Vino = 2.5
    Prezzo_Base_Vino = 6.0
    Giorno_Inizio_Vendemmia = 240   # Inizio Autunno
