### Slide 1 — Attention
**Title:** Lo que antes tomaba 45 minutos ahora toma 3 — con el mismo resultado.
**Format:** contrast
**Content:**
- Antes: buscar contexto → leer archivos → entender patrón → escribir → iterar. 45 min mínimo.
- Ahora: describir la tarea en lenguaje natural → Kiro lee el codebase, escribe y verifica. 3 min.
**Visual:** Contraste visual antes/después con línea de tiempo — 45 min en rojo, 3 min en verde
**Speaker note:** No empieces explicando qué es Kiro Crew. Empieza con el número: "45 minutos vs 3 minutos." Deja que eso aterrice. Luego: "Eso no es magia — tiene una razón específica. Y es lo que quiero mostrarles en los próximos 10 minutos."

### Slide 2 — Interest
**Title:** El problema no es que los devs sean lentos — es que el contexto se pierde entre herramientas y conversaciones.
**Format:** bullets
**Content:**
- Un dev pasa ~35% de su tiempo buscando contexto que ya existe en otro lugar
- Cada cambio de herramienta cuesta ~23 minutos de reconcentración
- Un manager espera una feature mientras el dev reconstruye contexto que el manager ya tiene
**Visual:** Diagrama de flujo: dev → IDE → Slack → doc → IDE → Slack (ciclo sin salida)
**Speaker note:** Aquí hablas con ambas audiencias al mismo tiempo. Al dev: "Saben de qué hablo — el rabbit hole de leer 8 archivos antes de tocar uno." Al manager: "Y ese tiempo invisible es exactamente por qué el sprint se extiende." Pausa un segundo entre los dos.

### Slide 3 — Desire — el sistema
**Title:** Kiro Crew es un agente de desarrollo que recuerda tu codebase, aprende tus patrones y puede hacer trabajo completo en tu nombre.
**Format:** bullets
**Content:**
- Memory — sabe qué hay en tu repo, qué decidiste antes, qué patrones usas
- Skills — protocolos especializados que le das para tareas específicas
- Agents — puede delegar partes del trabajo a sub-agentes que corren en paralelo
**Visual:** Diagrama de tres círculos conectados: Memory → Skills → Agents
**Speaker note:** La analogía que funciona para ambas audiencias: "Piensen en un desarrollador senior que siempre está disponible, ya leyó todo el codebase, y no se cansa de los tasks repetitivos." Para el dev: es el compañero que sabe todo el contexto. Para el manager: es velocidad sin más headcount.

### Slide 4 — Desire — en acción
**Title:** Este framework fue construido con Kiro Crew en una sesión — 7 skills, 6 PRs, y un .pptx generado automáticamente.
**Format:** bullets
**Content:**
- Prompt: "crea un framework de presentaciones para audiencias técnicas y no-técnicas"
- Resultado: 7 skills, workflow ejecutable, 3 ejemplos end-to-end, script Python de exportación
- Cada PR fue creado, revisado y mergeado dentro de la misma sesión
**Visual:** Screenshot del repo de GitHub con los 6 PRs mergeados
**Speaker note:** Este es el meta-momento: "Lo que están viendo ahora — este deck — fue generado por el pipeline que construimos con Kiro Crew." Si la audiencia es técnica, esto les va a gustar. Si no es técnica: "El mismo sistema que les explico fue el que hizo el trabajo."

### Slide 5 — Desire — mapa de conceptos
**Title:** Kiro Crew tiene cinco building blocks — empiezas con uno y agregas los demás cuando los necesitas.
**Format:** bullets
**Content:**
- Skills — protocolos para tareas específicas (primer paso, 5 min para configurar)
- Workflows — pipelines multi-fase reiniciables, visibles en el dashboard
- Crons — cualquier tarea recurrente automatizada con un script
**Visual:** Escalera de complejidad: Skills (base) → Workflows → Crons → Artifacts → Subagents
**Speaker note:** No intentes explicar cada uno en detalle. Di: "Estos son los 3 que vas a usar la primera semana. Hay dos más — Artifacts y Subagents — los vas a necesitar cuando tus tareas crezcan. No te preocupes por ellos hoy." Eso reduce la carga cognitiva sin quitar información.

### Slide 6 — Action
**Title:** Puedes empezar hoy — el primer resultado útil toma menos de 15 minutos.
**Format:** bullets
**Content:**
- Si eres dev: abre un proyecto, describe una tarea en lenguaje natural, mira qué hace Kiro
- Si lideras un equipo: pide a un dev que lo pruebe y mide el tiempo — compara con el promedio anterior
- El único requisito: tener un proyecto con código existente
**Visual:** No visual needed — la apuesta final hace el trabajo
**Speaker note:** No termines con preguntas. Termina con: "Tomen 15 minutos esta semana. Si en 15 minutos Kiro no entendió tu codebase y no hizo algo útil, tienen permiso de olvidar que esta presentación existió." Eso es una apuesta concreta. La audiencia técnica la entiende. La no-técnica también.
