```mermaid
graph TD
    A[Inicio] --> B[Mostrar mensaje:Bienvenido al juego de Piedra, Papel o Tijeras]
    B --> C[Solicitar al jugador que elija: Piedra, Papel o Tijeras]
    C --> D[Leer la elección del jugador]
    D --> E[Generar elección de la computadora de manera aleatoria: Piedra, Papel o Tijeras]
    E --> F[Comparar elección del jugador y elección de la computadora]
    F --> |Elección igual| G[Mostrar mensaje:Empate]
    F --> |Elección del jugador es Piedra| H{Elección de la computadora}
    H --> |Tijeras| I[Mostrar mensaje:Ganas]
    H --> |Papel| J[Mostrar mensaje:Pierdes]
    F --> |Elección del jugador es Papel| K{Elección de la computadora}
    K --> |Piedra| L[Mostrar mensaje:Ganas]
    K --> |Tijeras| M[Mostrar mensaje:Pierdes]
    F --> |Elección del jugador es Tijeras| N{Elección de la computadora}
    N --> |Papel| O[Mostrar mensaje:Ganas]
    N --> |Piedra| P[Mostrar mensaje:Pierdes]
    G --> Q[Mostrar las elecciones de ambos]
    I --> Q[Mostrar las elecciones de ambos]
    J --> Q[Mostrar las elecciones de ambos]
    L --> Q[Mostrar las elecciones de ambos]
    M --> Q[Mostrar las elecciones de ambos]
    O --> Q[Mostrar las elecciones de ambos]
    P --> Q[Mostrar las elecciones de ambos]
    Q --> R[Preguntar al jugador si quiere jugar otra vez]
    R --> |Sí| C
    R --> |No| S[Mostrar mensaje:Gracias por jugar]
    S --> T[Fin]
