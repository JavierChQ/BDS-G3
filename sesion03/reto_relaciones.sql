CREATE TABLE empresa(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ruc VARCHAR(10) NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

INSERT INTO empresa(ruc,razon_social) VALUES
('123456100','Ansur Peru SAC'),
('123456200','TELCEL SAC'),
('123456300','BRONCO EIRL'),
('123456400','RAPI SAC');

CREATE TABLE ciudad(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_ciudad VARCHAR(100) NOT NULL
);

INSERT INTO ciudad(nombre_ciudad) VALUES
('Arequipa'),
('Cusco'),
('Lima'),
('Trujillo'),
('Puno');

CREATE TABLE direccion(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    direccion VARCHAR(100) NOT NULL,
    empresa_id int NOT NULL,
    ciudad_id int NOT NULL,
    FOREIGN KEY (empresa_id) REFERENCES empresa(id),
    FOREIGN KEY (ciudad_id) REFERENCES ciudad(id)
);

INSERT INTO direccion(direccion,empresa_id,ciudad_id) VALUES
('Calle cartagena 432',1,1),
('Av. Ejercito 345',1,2),
('Calle Agentina 532',2,3),
('Av. Miguel grau 444',2,4),
('Calle Primaver 3456',3,5),
('Av. Melgar 1234',4,5);