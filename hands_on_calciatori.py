
# Report: Predizione Valore di Mercato Calciatori

Questo report riassume i risultati dell'analisi e del modello di regressione lineare per la stima del valore di mercato dei calciatori.

## 1. Dati
- **Dataset Generato**: `dataset_giocatori.csv`
- **Numero di Giocatori**: 100
- **Features Utilizzate**: ['Gol_Stagionali', 'Assist', 'Eta']
- **Target**: `Valore_Mercato_Milioni`

## 2. Performance del Modello
Le performance sono state valutate su un test set composto dal 20% dei dati.

- **Mean Squared Error (MSE)**: `18.99`
- **R-squared (R2) Score**: `0.83`

L'R2 Score indica che il modello riesce a spiegare circa il **83%** della varianza nel valore di mercato dei giocatori, un risultato molto buono per il nostro dataset sintetico.

## 3. Dettagli del Modello
Il modello ha imparato la seguente relazione:

`Valore = (1.15 * Gol) + (0.61 * Assist) + (-0.48 * Età) + 25.00`

- **Coefficiente per Gol Stagionali**: `1.15`. Per ogni gol in più, il valore aumenta in media di questo importo (in milioni).
- **Coefficiente per Assist**: `0.61`.
- **Coefficiente per Età**: `-0.48`. Il valore negativo indica che, a parità di gol e assist, l'aumentare dell'età tende a diminuire il valore di mercato nel nostro modello.

## 4. Predizione Pratica
È stato simulato un nuovo giocatore con le seguenti caratteristiche:
- Gol Stagionali: `20`
- Assist: `10`
- Età: `24`

La stima del suo valore di mercato è:
- **Valore di Mercato Stimato**: **`33.01` Milioni di Euro**
