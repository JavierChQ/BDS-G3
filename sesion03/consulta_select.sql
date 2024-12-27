-- select
SELECT * FROM empleado;
SELECT nombre,pais FROM empleado;
SELECT * FROM empleado LIMIT 10;
SELECT * FROM empleado ORDER BY nombre;
SELECT * FROM empleado ORDER BY salario DESC;
SELECT * FROM empleado WHERE pais = 'Peru';
SELECT * FROM empleado WHERE salario > 5000;
SELECT * FROM empleado WHERE salario > 5000 AND pais = 'Peru';