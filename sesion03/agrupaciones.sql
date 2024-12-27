-- funciones de agrupación
-- 1. contar
SELECT COUNT(*) FROM empleado;
SELECT COUNT(*) FROM empleado WHERE salario > 5000;

-- maximo y minimo
SELECT MAX(salario),MIN(salario),AVG(salario) FROM empleado;

SELECT DISTINCT pais FROM empleado;

SELECT pais,COUNT(*) FROM empleado
GROUP BY pais
ORDER BY COUNT(*) DESC;

-- Salario maximo, minimo y promedio por pais
SELECT pais,area,MAX(salario),MIN(salario),AVG(salario) FROM empleado
GROUP BY pais,area;

SELECT pais,area,MAX(salario),MIN(salario),AVG(salario) FROM empleado
WHERE salario > 5000 -- WHERE: Antes de la agurpación
GROUP BY pais,area;

SELECT pais,AVG(salario) FROM empleado
GROUP BY pais
HAVING AVG(salario) > 4000; -- HAVING: Despues de la agrupación

-- subconsultas
SELECT AVG(salario) FROM empleado;
SELECT * FROM empleado
WHERE salario > (SELECT AVG(salario) FROM empleado);

SELECT pais,COUNT(*),(SELECT AVG(salario) FROM empleado) as salario_promedio FROM empleado
WHERE salario > (SELECT AVG(salario) FROM empleado)
GROUP BY pais ORDER BY COUNT(*) DESC;