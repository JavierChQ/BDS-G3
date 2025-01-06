-- Active: 1735250242590@@127.0.0.1@3306@db_proyecto_datag3
CREATE TABLE empresa(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ruc VARCHAR(20) NOT NULL,
    razon_social VARCHAR(255) NOT NULL
);

CREATE TABLE ciudad(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_ciudad VARCHAR(100) NOT NULL
);

CREATE TABLE direccion(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    direccion VARCHAR(100) NOT NULL,
    ciudad_id int NOT NULL,
    empresa_id int NOT NULL,
    FOREIGN KEY (ciudad_id) REFERENCES ciudad(id),
    FOREIGN KEY (empresa_id) REFERENCES empresa(id) 
);