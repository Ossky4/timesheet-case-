# Comparativa final — mi-primer-repo vs csvtools-case vs timesheet-case

## Propósito
Comparar los tres casos realizados para identificar qué tipo de señal aporta cada uno, en qué condiciones Codex rinde mejor y qué hipótesis conviene probar a continuación.

## Caso 1 — mi-primer-repo
Este repositorio funcionó como sandbox inicial para validar el método de trabajo con Codex en condiciones controladas.

### Qué se probó
- PRs pequeñas y de una sola intención.
- Tests puntuales.
- Bugfixes pequeños.
- Mejoras de UX acotadas.
- Refactors pequeños, incluyendo un caso multiarchivo.
- Cambios mixtos de código, tests y documentación.

### Qué señal aportó
`mi-primer-repo` confirmó que el método base funciona bien cuando:
- el contexto es simple,
- el riesgo es bajo,
- la validación es barata,
- y el alcance está claramente delimitado.

También sirvió para fijar un patrón operativo:
- contrato de trabajo claro,
- PR pequeña,
- checks explícitos,
- microevaluación humana al cierre.

## Caso 2 — csvtools-case
Este repositorio funcionó como Case Project de cleanup arquitectónico pequeño en un entorno más real que el sandbox inicial.

### Qué se probó
- PR1 documental para delimitar alcance y hotspots.
- Cleanup local mínimo.
- Cleanup multiarchivo real.
- Blindaje con tests de la frontera tratada.
- Estabilización del entorno mínimo de tests.
- Un segundo hotspot distinto, aunque de menor entidad estructural.
- Cierre documental y playbook reusable.

### Qué señal aportó
`csvtools-case` confirmó que Codex puede trabajar con control en un repo más real cuando:
- el hotspot está bien delimitado,
- el cambio sigue siendo pequeño y reversible,
- la validación mínima del repo es suficiente,
- y la revisión humana mantiene disciplina de alcance.

También mostró algo importante:
mejorar primero la infraestructura mínima de validación eleva la calidad de todas las PRs posteriores.

## Caso 3 — timesheet-case
Este repositorio funcionó como caso para medir una hipótesis distinta: elección entre varias alternativas plausibles de cleanup.

### Qué se probó
- PR1 de selección explícita entre alternativas.
- PR2 técnica sobre la opción más conservadora para la frontera CLI ↔ dominio.
- Rechazo implícito de una primera dirección menos conservadora.
- PR3 de blindaje con tests unitarios.
- PR4 mínima de entorno para hacer ejecutable ese blindaje.
- PR5 de retrospectiva breve de cierre.

### Qué señal aportó
`timesheet-case` añadió una señal nueva respecto a los casos anteriores:
no solo que Codex puede ejecutar cambios pequeños, sino que puede participar en una decisión local entre varias opciones plausibles, siempre que existan:
- alcance explícito,
- criterio conservador,
- revisión humana disciplinada,
- y validación mínima suficiente.

También mostró que la revisión humana no solo valida ejecución, sino calidad de decisión.

## Diferencias clave entre los tres casos

### mi-primer-repo
- mayor control,
- menor complejidad,
- señal rápida,
- mejor para fijar el método base.

### csvtools-case
- más real que el sandbox,
- útil para medir cleanup multiarchivo pequeño,
- mejor para probar disciplina de frontera y entorno de tests,
- buena base para extraer método reusable.

### timesheet-case
- más útil para medir juicio entre alternativas,
- mejor señal sobre selección conservadora,
- más dependiente de revisión humana para distinguir una solución válida de la mejor opción razonable.

## Aprendizajes operativos comunes
En los tres casos, Codex rindió mejor cuando se mantuvieron estas condiciones:
- una sola intención por PR,
- cambios pequeños y revisables,
- restricciones explícitas,
- checks claros,
- separación entre fallo del entorno y efecto del cambio,
- microevaluación humana breve tras cada revisión.

## Qué parece funcionar mejor
Codex aporta más valor cuando trabaja como:
- operador técnico de ejecución,
- en repos con validación barata,
- sobre hotspots acotados,
- con decisiones reversibles,
- y con revisión humana que discipline alcance y criterio.

## Límites observados
- El valor cae cuando la PR aporta más higiene local que señal estructural.
- No se ha probado todavía un caso con dependencias internas claramente más ricas.
- Tampoco se ha probado una decisión con varias alternativas plausibles y mayor profundidad estructural.
- El entorno de validación sigue siendo un factor clave para la calidad de la señal.

## Conclusión
Los tres casos, en conjunto, sugieren que Codex funciona bien en cambios pequeños, acotados, reversibles y bien revisados.

La evidencia es especialmente sólida en tres planos:
1. ejecución disciplinada de PRs pequeñas,
2. cleanup multiarchivo pequeño con validación suficiente,
3. elección conservadora entre alternativas locales plausibles.

## Recomendación del siguiente experimento
No seguir por inercia en ninguno de estos tres repositorios.

El siguiente Case Project debería probar una hipótesis nueva y explícita, idealmente una de estas:
1. dependencias entre módulos algo más ricas,
2. alternativa de cleanup con mayor profundidad estructural,
3. hotspot ambiguo donde la selección correcta exija más juicio técnico sin salir todavía de PRs pequeñas.

La recomendación actual es pasar a un caso donde el reto principal ya no sea solo ejecutar bien, sino decidir bien en un contexto un poco más denso.
