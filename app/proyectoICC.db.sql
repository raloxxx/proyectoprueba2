BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "estudiante" (
	"id"	INTEGER NOT NULL,
	"codigo"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
	"usuario"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "curso" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "matricula" (
	"id"	INTEGER NOT NULL,
	"profesor_id"	INTEGER NOT NULL,
	"estudiante_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("profesor_id") REFERENCES "profesor"("id"),
	FOREIGN KEY("estudiante_id") REFERENCES "estudiante"("id")
);
CREATE TABLE IF NOT EXISTS "profesor" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
	"usuario"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"codigo"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "foro" (
	"id"	INTEGER NOT NULL,
	"descripcion"	TEXT NOT NULL,
	"fecha_entrega"	DATE NOT NULL,
	"fecha_entregado"	DATE NOT NULL,
	"fecha_final"	DATE NOT NULL,
	"periodo_id"	INTEGER NOT NULL,
	"curso_id"	INTEGER NOT NULL,
	"estudiante_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("curso_id") REFERENCES "curso"("id"),
	FOREIGN KEY("periodo_id") REFERENCES "periodo"("id"),
	FOREIGN KEY("estudiante_id") REFERENCES "estudiante"("id")
);
CREATE TABLE IF NOT EXISTS "periodo" (
	"id"	INTEGER NOT NULL,
	"descripcion"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "periodo_curso" (
	"id"	INTEGER NOT NULL,
	"curso_id"	INTEGER NOT NULL,
	"periodo_id"	INTEGER NOT NULL,
	"matricula_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("periodo_id") REFERENCES "periodo"("id"),
	FOREIGN KEY("matricula_id") REFERENCES "matricula"("id"),
	FOREIGN KEY("curso_id") REFERENCES "curso"("id")
);
CREATE TABLE IF NOT EXISTS "tarea" (
	"id"	INTEGER NOT NULL,
	"ruta"	TEXT NOT NULL,
	"descripcion"	TEXT NOT NULL,
	"fecha_entrega"	DATE NOT NULL,
	"fecha_entregado"	DATE NOT NULL,
	"fecha_final"	DATE NOT NULL,
	"periodo_id"	INTEGER NOT NULL,
	"curso_id"	INTEGER NOT NULL,
	"estudiante_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("curso_id") REFERENCES "curso"("id"),
	FOREIGN KEY("estudiante_id") REFERENCES "estudiante"("id"),
	FOREIGN KEY("periodo_id") REFERENCES "periodo"("id")
);
CREATE TABLE IF NOT EXISTS "nota" (
	"id"	INTEGER NOT NULL,
	"unidad"	INTEGER NOT NULL,
	"nota"	DOUBLE NOT NULL,
	"id_actividad"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
COMMIT;
