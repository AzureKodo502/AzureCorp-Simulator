import random
import csv
import matplotlib.pyplot as plt
import numpy as np 
from config import Config
from classi import CampoGrano, Stalla, Vigneto

def inizializza_seed():
    """
    Gestisce la riproducibilità della simulazione
    Se Config.SEED è None, ne genera uno casuale
    """
    seed_da_usare = Config.SEED
    
    if seed_da_usare is None:
        seed_da_usare = random.randint(1, 1000000)
        tipo = "(Generato Casualmente)"
    else:
        tipo = "(Impostato da Config)"
        
    random.seed(seed_da_usare)
    np.random.seed(seed_da_usare)
    
    return seed_da_usare, tipo

def aggiorna_trend_economico(trend_attuale):
    # Qui uso uniform
    # la funzione uniform fa in modo che le probabilità di uscita in quel range siano le stesse per tutte
    delta = random.uniform(-0.02, 0.02)
    if random.random() < 0.05: 
        delta *= 5 
    nuovo_trend = trend_attuale + delta
    return max(0.5, min(1.8, nuovo_trend))

def genera_scenario_giornaliero(giorno, trend_mercato):
    molt_prezzi = {
        'grano': trend_mercato, 'latte': trend_mercato, 'vino': trend_mercato, 
        'carburante': 1.0, 'costi_vari': 1.0
    }
    
    if trend_mercato < 0.9:
        molt_prezzi['carburante'] = random.uniform(1.1, 1.4)
        molt_prezzi['costi_vari'] = random.uniform(1.0, 1.3)
    
    molt_prod = {'grano': 1.0, 'latte': 1.0, 'vino': 1.0}
    evento_msg = ""
    
    if random.random() < Config.Probabilita_Evento:
        tipo = random.choice(["SICCITÀ", "GUERRA", "PANDEMIA", "BOOM_EXPORT"])
        
        if tipo == "SICCITÀ":
            molt_prod['grano'] = 0.1
            molt_prod['latte'] = 0.7
            evento_msg = "🔥 Siccità grave: Produzione agricola crollata"
        elif tipo == "GUERRA":
            molt_prezzi['carburante'] = 3.0
            molt_prezzi['costi_vari'] = 2.0
            evento_msg = "💣 Guerra: Costi energetici aumentati"
        elif tipo == "PANDEMIA":
            molt_prod['latte'] = 0.0
            molt_prod['vino'] = 0.2
            evento_msg = "😷 Pandemia: Mercati chiusi, vendite bloccate"
        elif tipo == "BOOM_EXPORT":
            molt_prezzi['vino'] *= 2.0
            molt_prezzi['grano'] *= 1.5
            evento_msg = "🚀 Boom Export: Domanda di Export Aumentata"

    for chiave in molt_prezzi:
        if chiave not in ['carburante', 'costi_vari']:
             molt_prezzi[chiave] *= random.uniform(0.95, 1.05)
        
    return molt_prezzi, molt_prod, evento_msg

def esegui_simulazione():
    seed_corrente, tipo_seed = inizializza_seed()
    
    print("Inizio Simulazione")
    print(f"Seed: {seed_corrente} {tipo_seed}")
    print(f"Budget Iniziale: {int(Config.Budget)} euro\n")
    
    trend_mercato = random.uniform(0.8, 1.2) 
    azienda = [CampoGrano(), Stalla(), Vigneto()]
    
    cassa_attuale = Config.Budget
    debito_totale = 0.0
    
    dati_export = [] 
    storico_giorni = []
    storico_cassa = []
    storico_trend = []
    storico_settori = {'Grano': [], 'Latte': [], 'Vino': []}

    for giorno in range(1, Config.Giorni + 1):
        # Qui uso la funziona gauss per favorire di più giornate normali (meteo 1.0) e meno quelle più caotiche 
        meteo = random.gauss(1.0, Config.Meteo)
        
        trend_mercato = aggiorna_trend_economico(trend_mercato)
        molt_prezzi, molt_prod, news = genera_scenario_giornaliero(giorno, trend_mercato)
        
        if news: 
            print(f"\n >>> Giorno {giorno}: {news} <<<\n")

        costi_fissi = Config.Stipendio_Giornaliero_Totale + Config.Affitto_e_Tasse_Giornaliero
        cassa_attuale -= costi_fissi

        # Gestione banca e interessi
        if cassa_attuale < Config.SOGLIA_BANCAROTTA:
            interessi = abs(cassa_attuale) * (Config.Tasso_Interesse_Passivo / 365)
            cassa_attuale -= interessi
            debito_totale += interessi

        risorse = {'trattori_disponibili': Config.Trattori, 'operai_disponibili': Config.Operai}
        log_giornata = f"Giorno {giorno} [Mercato {round(trend_mercato, 2)}]: "
        
        profitti_del_giorno = {}

        for unita in azienda:
            messaggio = unita.calcola_giornata(meteo, risorse, giorno, molt_prezzi, molt_prod)
            flusso = unita.get_flusso_cassa_odierno()
            cassa_attuale += flusso
            profitti_del_giorno[unita.nome] = unita.get_profitto()
            
            if "Maturazione" not in messaggio and "Riposo" not in messaggio:
                log_giornata += f"[{unita.nome}: {messaggio}] "

        storico_giorni.append(giorno)
        storico_cassa.append(cassa_attuale)
        storico_trend.append(trend_mercato)
        storico_settori['Grano'].append(profitti_del_giorno["Campo di Grano"])
        storico_settori['Latte'].append(profitti_del_giorno["Stalla (Latte)"])
        storico_settori['Vino'].append(profitti_del_giorno["Vigneto & Cantina"])

        dati_export.append({
            'Giorno': giorno,
            'Trend_Mercato': round(trend_mercato, 2),
            'Cassa': round(cassa_attuale, 2),
            'Evento': news if news else "",
            'Profitto_Grano': round(profitti_del_giorno["Campo di Grano"], 2),
            'Profitto_Latte': round(profitti_del_giorno["Stalla (Latte)"], 2),
            'Profitto_Vino': round(profitti_del_giorno["Vigneto & Cantina"], 2)
        })

        if news: 
            print(log_giornata)
        
        # Condizione per la bancarotta irreversibile
        if cassa_attuale < -100000:
            print(f"\n  BANCAROTTA IRREVERSIBILE AL GIORNO {giorno}.")
            break

    # Esportazione dati in CSV
    with open(Config.FILE_LOG, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=dati_export[0].keys())
        writer.writeheader()
        writer.writerows(dati_export)
    print(f"\nDati esportati con successo in: {Config.FILE_LOG}")

    stampa_report_finale(cassa_attuale, debito_totale, seed_corrente, azienda)
    crea_grafici_avanzati(storico_giorni, storico_cassa, storico_trend, storico_settori)

def stampa_report_finale(cassa, debito, seed, azienda):
    print("\nREPORT FINALE DI PRODUZIONE")
    print(f"Seed Utilizzato: {seed}")
    print("PRODUZIONE FISICA TOTALE:")
    print(f"1. Grano: {int(azienda[0].quantita_prodotta)} Kg")
    print(f"2. Latte: {int(azienda[1].quantita_prodotta)} Litri")
    print(f"3. Vino:  {int(azienda[2].quantita_prodotta)} Bottiglie")
    print(f"Saldo Finale: {round(cassa, 2)} euro")
    print(f"Interessi Passivi Generati: {round(debito, 2)} euro")
    
    if cassa < 0:
        print("ESITO: FALLIMENTO ❌")
    else:
        print("ESITO: SUCCESSO ✅")
    print("\n")

def crea_grafici_avanzati(giorni, cassa, trend, settori):
    plt.figure(figsize=(14, 10))
    
    plt.subplot(3, 1, 1)
    plt.plot(giorni, cassa, label='Cassa Aziendale', color='green', linewidth=2)
    plt.axhline(y=0, color='red', linestyle='--', label='Soglia Bancarotta')
    plt.fill_between(giorni, cassa, 0, where=(np.array(cassa) < 0), color='red', alpha=0.3)
    plt.title('Salute Finanziaria')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(giorni, trend, label='Indice Economico (1.0 = Neutro)', color='orange')
    plt.axhline(y=1.0, color='gray', linestyle='--')
    plt.title('Scenario di Mercato')
    plt.ylabel('Moltiplicatore')
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(giorni, settori['Grano'], label='Grano', color='gold')
    plt.plot(giorni, settori['Latte'], label='Latte', color='blue')
    plt.plot(giorni, settori['Vino'], label='Vino', color='purple')
    plt.title('Andamento Profitti per Settore')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    esegui_simulazione()
