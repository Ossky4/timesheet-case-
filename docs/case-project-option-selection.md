# Case Project (PR1): selección de opción de cleanup

## Propósito del caso
Delimitar un primer hotspot de cleanup en este repositorio, de forma explícita y conservadora, antes de realizar cambios de código.

## Hipótesis del experimento
Si se define primero un alcance pequeño y criterios de decisión claros sobre la frontera entre **CLI**, **lógica principal** y **funciones de datos**, entonces la primera PR técnica podrá ser más acotada, revisable y con menor riesgo de efectos colaterales.

> Nota de prudencia: esta hipótesis **no** asume defectos internos concretos ni duplicaciones no verificadas; solo propone evaluar opciones plausibles a partir de la estructura actual del proyecto.

## Módulos bajo observación
- `timesheet/__main__.py`
- `timesheet/command_line_interface_functions.py`
- `timesheet/timesheet.py`
- `timesheet/data_functions.py`

## Alternativas plausibles de cleanup (sin cambios aún)

### Opción A — Clarificar frontera CLI ↔ lógica de negocio
Priorizar una separación más explícita entre parsing/orquestación de comandos (CLI) y operaciones de dominio de timesheet.

### Opción B — Clarificar frontera lógica de negocio ↔ acceso/transformación de datos
Priorizar una separación más explícita entre reglas de negocio y utilidades de persistencia/manipulación de datos.

### Opción C — Normalizar flujo end-to-end (entrada CLI → procesamiento → salida)
Priorizar consistencia de responsabilidades a lo largo del flujo completo, sin profundizar todavía en una sola frontera interna.

## Criterio para elegir entre alternativas
Se elegirá la alternativa que maximice simultáneamente:
1. **Bajo riesgo** de regresión funcional en la primera PR técnica.
2. **Cambio mínimo revisable** (small diff, propósito único).
3. **Mejora explícita de claridad** de responsabilidades entre módulos.
4. **Trazabilidad en tests existentes** (impacto comprobable sin rediseños amplios).

## Fuera de alcance en PR1
- Cambios de código en `timesheet/`.
- Cambios de tests, `setup.py`, `README.md`, workflows o tooling.
- Refactors amplios o multipropósito.
- Optimización de performance o cambios de comportamiento funcional.

## Secuencia prevista de PRs
- **PR1 (esta):** documento de selección de opción (solo alcance/criterios).
- **PR2:** primera intervención técnica mínima sobre la opción elegida.
- **PR3 (si aplica):** ajustes de consolidación y/o extensión acotada del cleanup inicial.
