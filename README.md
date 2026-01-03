# Progetto: Predizione del Valore di Mercato di un Calciatore

Questo progetto è un esercizio pratico di machine learning che implementa un modello di **Regressione Lineare** per predire il valore di mercato (in milioni di euro) di un calciatore sulla base di alcune sue statistiche stagionali.

L'intero processo è contenuto nello script `hands_on_calciatori.py`, che esegue le seguenti operazioni in sequenza:

1.  **Generazione Dati**: Crea un dataset fittizio di 100 calciatori con statistiche casuali (`Gol_Stagionali`, `Assist`, `Eta`).
2.  **Addestramento Modello**: Utilizza `scikit-learn` per addestrare un modello di `LinearRegression`.
3.  **Valutazione**: Calcola le metriche di performance del modello, come **Mean Squared Error (MSE)** e **R-squared (R2) Score**.
4.  **Predizione**: Esegue una predizione pratica su un nuovo giocatore fittizio.
5.  **Reporting**: Genera un report (`report_calciatori.md`) che riassume l'analisi, le performance e i risultati.

## Come Eseguire il Progetto

### Prerequisiti
- Python 3.x
- Le librerie specificate in `requirements.txt`

### Installazione
Clona il repository e installa le dipendenze:
```bash
git clone <URL_DEL_TUO_REPOSITORY>
cd <NOME_DELLA_CARTELLA>
pip install -r requirements.txt
```

### Esecuzione
Per eseguire l'analisi completa, lancia lo script:
```bash
python hands_on_calciatori.py
```
Al termine dell'esecuzione, nella cartella verrà creato il file `report_calciatori.md` con il riepilogo dei risultati.

## Esempio di Risultato
L'output a console mostrerà i passaggi dell'analisi, e il report generato conterrà un'analisi dettagliata come la seguente:

> ### 4. Predizione Pratica
> È stato simulato un nuovo giocatore con le seguenti caratteristiche:
> - Gol Stagionali: `20`
> - Assist: `10`
> - Età: `24`
>
> La stima del suo valore di mercato è:
> - **Valore di Mercato Stimato**: **`36.78` Milioni di Euro**

---
*Questo progetto è stato creato come esercizio per un corso di IA applicata allo Sport.*
