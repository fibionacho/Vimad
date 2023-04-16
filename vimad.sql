CREATE TABLE Estudio (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  fec_fundacion DATE
);

INSERT INTO Estudio (nombre, fec_fundacion)
VALUES ('Estudio1', '2022-01-01'),
       ('Estudio2', '2005-07-15'),
       ('Estudio3', '1998-12-31');

CREATE TABLE Director (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  fec_nacimiento DATE,
  nacionalidad VARCHAR(50)
);

INSERT INTO Director (nombre, fec_nacimiento, nacionalidad)
VALUES ('Pedro', '1995-02-03', 'España'),
        ('Ana', '1998-01-12', 'Canadá');


CREATE TABLE Actor (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  fec_nacimiento DATE,
  nacionalidad VARCHAR(50)
);


INSERT INTO Actor (nombre, fec_nacimiento, nacionalidad)
VALUES ('Actor1', '1985-06-20', 'Estados Unidos'),
       ('Actor2', '1978-09-12', 'Reino Unido'),
       ('Actor3', '1990-03-08', 'España'),
       ('Actor4', '1982-12-05', 'Canadá'),
       ('Actor5', '1975-07-18', 'Australia');


CREATE TABLE Corto (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(50),
  puntuacion VARCHAR(10),
  genero VARCHAR(50),
  duracion VARCHAR(3),
  fec_estreno DATE,
  idioma VARCHAR(50),
  pais VARCHAR(50),
  sinopsis TEXT,
  ruta_imagen VARCHAR(255) NULL,
  ruta_video VARCHAR(255) NULL,
  estudio_id INT,
  FOREIGN KEY (estudio_id) REFERENCES Estudio (id) ON DELETE CASCADE
);


INSERT INTO Corto (titulo, puntuacion, genero, duracion, fec_estreno, idioma, pais, sinopsis, ruta_imagen, ruta_video)
VALUES ('Corto1', '8.5', 'Comedia', '15', '2022-01-01', 'Español', 'España', 'Sinopsis del Corto1', 'imagen1.jpg', 'video1.mp4'),
       ('Corto2', '7.9', 'Drama', '12', '2021-05-15', 'Inglés', 'Estados Unidos', 'Sinopsis del Corto2', 'imagen2.jpg', 'video2.mp4'),
       ('Corto3', '6.6', 'Acción', '20', '2020-10-10', 'Francés', 'Francia', 'Sinopsis del Corto3', 'imagen3.jpg', 'video3.mp4'),
       ('Corto4', '9.1', 'Fantasía', '8', '2023-03-20', 'Alemán', 'Alemania', 'Sinopsis del Corto4', 'imagen4.jpg', 'video4.mp4'),
       ('Corto5', '7.3', 'Romance', '18', '2022-07-05', 'Italiano', 'Italia', 'Sinopsis del Corto5', 'imagen5.jpg', 'video5.mp4');


CREATE TABLE Dirige (
  id VARCHAR(100) PRIMARY KEY,
  nombre_id INT,
  titulo_id INT,
  FOREIGN KEY (nombre_id) REFERENCES Director (id) ON DELETE CASCADE,
  FOREIGN KEY (titulo_id) REFERENCES Corto (id) ON DELETE CASCADE
);

INSERT INTO Dirige (id, nombre_id, titulo_id)
VALUES ('1', 1, 1),
       ('2', 1, 2),
       ('3', 2, 3),
       ('4', 2, 4),
       ('5', 1, 5);


CREATE TABLE Actua (
    id VARCHAR(100) PRIMARY KEY,
    nombre_id INT,
    titulo_id INT,
    FOREIGN KEY (nombre_id) REFERENCES Actor(id),
    FOREIGN KEY (titulo_id) REFERENCES Corto(id)
);

INSERT INTO Actua (id, nombre_id, titulo_id)
VALUES ('1',5,1),
('2', 5, 2),
('3', 1, 2),
('4', 1, 3),
('5', 2, 3);