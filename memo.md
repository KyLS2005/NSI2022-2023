CREATE TABLE Article ( id INTEGER PRIMARY KEY , Secteur TEXT , Nom TEXT , prix REAL , Quantité INTEGER );


INSERT INTO Article VALUES 

(1, "Jouet Enfants", "Peluche Mimiqui XXL", 59.99 , 1),
(2, "Vêtements", "Robe de soirée noire M", 39.99 , 1),
(3, "Nourriture évasion", "Bubble Tea", 1.5 , 2),
(4, "Fruit frais", "Melon d'eau", 5 , 1),
(5, "Beauté", "Palette Hiver 2023", 15 , 1),
(6, "Beauté", "Eye Liner True Damage", 2 , 1),
(7, "Beauté", "Hair dye Red 100 mL", 5 , 1),
(8, "Accessoires", "Collier Lune de Mars", 50.99 , 1),
(9, "Accessoires", "Collier Sable des temps", 55.99 , 1),
(10, "Jeux vidéos", "Joy-cons édition spécial", 89.90 , 1),
(11, "Jeux vidéos", "Final Fantasy Crisis Core Reunion", 59.90 , 1),
(12, "Patisserie", "Gateaux fondant au chocolat", 15.00 , 1),
(13, "Patisserie", "Pains au chocolat", 0.90 ,10),
(14, "Livres", "Tome 3 The Kane Chronicles", 16.90 ,1),
(15, "Livres", "Tome 2 The Kane Chronicles", 16.90 ,1);

SELECT * FROM Article;
SELECT Nom , prix, Quantité FROM Article ORDER BY  prix;
SELECT SUM(Quantité) FROM Article
