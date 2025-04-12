show databases;
create database ouvidoria;

use ouvidoria;

CREATE TABLE manifestacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('reclamacao', 'elogio', 'sugestao') NOT NULL,
    descricao TEXT
);

select * from manifestacao;
SELECT COUNT(*) FROM manifestacao;