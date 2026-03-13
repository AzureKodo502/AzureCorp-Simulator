import random
from config import Config

class UnitaProduttiva:
    """
    Classe Madre
    Implementa le logiche comuni di bilancio e gestione del tempo
    """
    def __init__(self, nome):
        """ Inizializzazione degli attributi in comune di tutte le sottoclassi """
        self.nome = nome
        self.soldi_spesi = 0.0
        self.soldi_guadagnati = 0.0
        self.quantita_prodotta = 0.0
        self.tempo_impiegato = 0
        self.ricavo_oggi = 0.0
        self.spesa_oggi = 0.0

    def calcola_giornata(self, meteo, risorse, giorno_anno, molt_prezzi, molt_prod):
        """ Metodo per calcolare la giornata, dovrà essere sovrascritto dalle sottoclassi """
        pass

    def get_flusso_cassa_odierno(self):
        """Ricavo - Spese restituiscono il flusso di cassa giornaliero """
        return self.ricavo_oggi - self.spesa_oggi

    def genera_quantita_random(self, base_output, meteo):
        """
        Metodo per la generazione della quantità random
        Include un controllo per evitare produzioni negative dovuto al meteo instabile
        """
        fattore = random.uniform(meteo, 1.2)
        if fattore < 0.1: 
            fattore = 0.1
        
        quantita = base_output * fattore
        return max(0.0, quantita)

    def get_profitto(self):
        """ Soldi Guadagnati - Soldi spesi ricava il profitto giornaliero """
        return self.soldi_guadagnati - self.soldi_spesi


class CampoGrano(UnitaProduttiva):
    """
    Coltivazione del Grano
    La logica è Semina > Costi iniziali > Attesa fino al 150esimo giorno > Raccolta
    """
    def __init__(self):
        super().__init__("Campo di Grano")
        self.giorni_passati = 0
        self.soldi_spesi += Config.Costo_Semina_Grano * Config.Ettari_Grano

    def calcola_giornata(self, meteo, risorse, giorno_anno, molt_prezzi, molt_prod):
        self.ricavo_oggi = 0.0
        self.spesa_oggi = 0.0 

        self.giorni_passati += 1
        self.tempo_impiegato += 1

        if self.giorni_passati >= Config.Giorni_Necessari_Grano:
            if risorse.get('trattori_disponibili', 1) > 0:
                
                resa_teorica = Config.Ettari_Grano * Config.Resa_Ettaro_Grano
                quantita_base = self.genera_quantita_random(resa_teorica, meteo)
                kg_reali = quantita_base * molt_prod['grano']
                
                prezzo = Config.Prezzo_Base_Grano * molt_prezzi['grano']
                costo_carb = Config.Costo_Base_Carburante_Trattore * molt_prezzi['carburante']
                
                self.ricavo_oggi = kg_reali * prezzo
                self.spesa_oggi = costo_carb
                
                self.quantita_prodotta += kg_reali
                self.soldi_guadagnati += self.ricavo_oggi
                self.soldi_spesi += self.spesa_oggi
                
                perc_danno = (1 - molt_prod['grano']) * 100
                messaggio = f"Raccolto: {int(kg_reali)} kg (Efficienza: {int(100 - perc_danno)}%). Ricavo: {round(self.ricavo_oggi, 2)} euro"
                
                # Reset del contatore per iniziare un nuovo ciclo, in caso di simulazioni più lunghe di 1 anno
                self.giorni_passati = 0
                self.soldi_spesi += Config.Costo_Semina_Grano * Config.Ettari_Grano
                
                return messaggio
            else:
                return "Coltura pronta, ma risorse (trattori) insufficienti."
                
        return "Fase di maturazione vegetativa..."


class Stalla(UnitaProduttiva):
    """
    Settore Allevamento e Produzione Latte
    La logica è a ciclo continuo con costi e ricavo giornalieri
    """
    def __init__(self):
        super().__init__("Stalla (Latte)")
    
    def calcola_giornata(self, meteo, risorse, giorno_anno, molt_prezzi, molt_prod):
        self.tempo_impiegato += 1
        
        costo_cibo = Config.Mucche * Config.Costo_Mangime * molt_prezzi['costi_vari']
        manutenzione = Config.Costo_Manutenzione_Stalla * molt_prezzi['costi_vari']
        self.spesa_oggi = costo_cibo + manutenzione

        prod_base = self.genera_quantita_random(Config.Mucche * Config.Litri_Prodotti, meteo)
        litri_reali = prod_base * molt_prod['latte']

        prezzo = Config.Prezzo_Base_Latte * molt_prezzi['latte']
        self.ricavo_oggi = litri_reali * prezzo
        
        self.soldi_spesi += self.spesa_oggi
        self.soldi_guadagnati += self.ricavo_oggi
        self.quantita_prodotta += litri_reali
        
        return f"Produzione: {int(litri_reali)} L. Margine: {int(self.ricavo_oggi - self.spesa_oggi)} euro"


class Vigneto(UnitaProduttiva):
    """
    Coltivazione dell'uva
    La logica è ibrida, prima la fase di maturazione, poi la fase di trasformazione
    """
    def __init__(self):
        super().__init__("Vigneto & Cantina")
        self.uva_in_magazzino = 0.0
        self.vendemmia_completata = False
    
    def calcola_giornata(self, meteo, risorse, giorno_anno, molt_prezzi, molt_prod):
        self.tempo_impiegato += 1
        self.ricavo_oggi = 0.0
        self.spesa_oggi = 30.0 * molt_prezzi['costi_vari']
        
        messaggio = ""
        giorno_relativo = ((giorno_anno - 1) % 365) + 1
        
        # Fase di Maturazione
        fine_vendemmia = Config.Giorno_Inizio_Vendemmia + 30
        if Config.Giorno_Inizio_Vendemmia <= giorno_relativo < fine_vendemmia:
            if not self.vendemmia_completata:
                if risorse.get('operai_disponibili', 2) >= 2:
                    risorse['operai_disponibili'] -= 2
                    
                    base_uva = (Config.Ettari_Vino * Config.Resa_Ettaro_Vino) / 30.0
                    uva_reale = self.genera_quantita_random(base_uva, meteo) * molt_prod['vino']
                    
                    self.uva_in_magazzino += uva_reale
                    messaggio = f"Vendemmia in corso: {int(uva_reale)} kg. "
        else:
            self.vendemmia_completata = False

        # Fase di Trasformazione in vino
        if self.uva_in_magazzino > 50:
            capacita_max = (Config.Ettari_Vino * Config.Resa_Ettaro_Vino) / 45.0
            if capacita_max < 400: 
                capacita_max = 400.0 
            
            lavorazione = min(self.uva_in_magazzino, capacita_max)
            self.uva_in_magazzino -= lavorazione
            
            bottiglie = int((lavorazione * Config.Conversione_Vino) / 0.75)
            costo_prod = bottiglie * Config.Costo_Imbottigliamento_Vino * molt_prezzi['costi_vari']
            ricavo = bottiglie * Config.Prezzo_Base_Vino * molt_prezzi['vino']
            
            self.spesa_oggi += costo_prod
            self.ricavo_oggi += ricavo
            self.quantita_prodotta += bottiglie
            
            messaggio += f"Cantina: {bottiglie} bottiglie."
            
        self.soldi_spesi += self.spesa_oggi
        self.soldi_guadagnati += self.ricavo_oggi
        
        if messaggio == "": 
            return "Maturazione vegetativa."
        return messaggio
