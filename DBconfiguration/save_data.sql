INSERT INTO usuarios (nombre, correo, telefono, fecha_nacimiento) VALUES
('Juan Pérez', 'juan.perez@example.com', '777-111-2233', '1990-03-15'),
('María López', 'maria.lopez@example.com', '777-444-5566', '1992-08-21'),
('Carlos Ruiz', 'carlos.ruiz@example.com', '777-777-8899', '1988-12-05');

INSERT INTO credenciales (id_usuario, username, password_hash) VALUES
(1, 'juan.perez', 'hash_juan_perez'),
(2, 'maria.lopez', 'hash_maria_lopez'),
(3, 'carlos.ruiz', 'hash_carlos_ruiz');
