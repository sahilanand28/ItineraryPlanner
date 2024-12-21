# Aegean Tour Itinerary Solver

This Python program prepares an island tour itinerary by determining the mode of transport (either airborne or by sea) between islands based on customer preferences. The goal is to satisfy as many customers as possible while minimizing airborne hops.

## Features
- Ensures each customer gets at least one hop with their preferred mode of transport.
- Minimizes airborne hops and defaults to sea transport when possible.
- Returns "NO ITINERARY" if it is impossible to satisfy all customer preferences.

## Prerequisites
- Python 3.x
- A virtual environment setup in the project directory.

## How to Run the Program

1. **Clone the repository** or download the project files.

2. **Set up the virtual environment**:
   
    - Activate the virtual environment:
      ```bash
      .\env\Scripts\activate
      ```

4. **Run the program**:

    - After activating the virtual environment, execute the Python script:
      ```bash
      python island_tour.py
      ```

5. **Input Format**:  
   The program expects input from `stdin` in the following format:
