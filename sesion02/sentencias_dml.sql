-- Active: 1735250242590@@127.0.0.1@3306@datag3
-- Sentencias DML
-- Insertar datos (INSERT)
INSERT INTO alumno(nro_documento,nombre) VALUES('100','cesar');
-- Insertar varios valores (solo en mysql)
INSERT INTO alumno(nro_documento,nombre,nota) VALUES
('200','javier',17),
('300','pedro',20),
('400','pablo',17),
('500','mirian',13),
('600','ana',17),
('700','rosa',15),
('800','manuel',15),
('900','miguel',17),
('1000','carlos',12);

-- Actualizar datos (UPDATE)
UPDATE alumno SET emial = 'correo@gmail.com';
-- Actualizar con WHERE
UPDATE alumno SET emial = 'cesar@gmail.com' WHERE id = 1;
-- Actualizar con funcion CONCAT
UPDATE alumno SET emial = CONCAT(nombre,'@gmail.com') WHERE id != 1;

-- Eliminar datos (DELETE)
DELETE FROM alumno WHERE id = 5;
DELETE FROM alumno WHERE id > 5;

-- Seleccionar datos (SELECT)
SELECT * FROM alumno;
SELECT nombre,nota FROM alumno;
SELECT nombre,nota FROM alumno WHERE nota > 15;