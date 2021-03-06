CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

INSERT INTO site (id, name, url, accuracy, type) VALUES (uuid_generate_v4(), 'Coindesk', 'https://coindesk.com', 0.000, 'core');

INSERT INTO author(id, name, accuracy) VALUES (uuid_generate_v4(), 'Ian Koide', 0.000);