```mermaid
graph TD
    A[Inicio] --> B[Jugador 1 elige: Piedra, Papel o Tijeras]
    B --> C[Jugador 2 elige: Piedra, Papel o Tijeras]
    C --> D{Comparar Elecciones}
    D --> |Piedra == Piedra| E[Resultado: Empate]
    D --> |Papel == Papel| E[Resultado: Empate]
    D --> |Tijeras == Tijeras| E[Resultado: Empate]
    D --> |Piedra vs Tijeras| F[Resultado: Gana Piedra]
    D --> |Papel vs Piedra| G[Resultado: Gana Papel]
    D --> |Tijeras vs Papel| H[Resultado: Ganan Tijeras]
    E --> I[Fin]
    F --> I[Fin]
    G --> I[Fin]
    H --> I[Fin]