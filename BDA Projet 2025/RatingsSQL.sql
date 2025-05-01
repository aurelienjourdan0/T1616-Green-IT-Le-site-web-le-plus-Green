CREATE DATABASE IF NOT EXISTS details;

USE details;


CREATE TABLE ratings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    `rank` INT,
    average FLOAT NOT NULL,
    bayes_average FLOAT NOT NULL,
    users_rated INT NOT NULL,
    url VARCHAR(200),
    thumbnail VARCHAR(255)
);


INSERT INTO ratings (name, year, `rank`, average, bayes_average, users_rated, url, thumbnail) VALUES
('Catan', 1995, 250, 7.2, 6.9, 50000, 'https://boardgamegeek.com/boardgame/13/catan', 'https://cf.geekdo-images.com/W3Bsga_uLP9kO91gZ7H8yw__micro/img/LA4OvGfQ_TXQ-2mhaIFZp2ITWpc=/fit-in/64x64/filters:strip_icc()/pic2419375.jpg'),
('Terraforming Mars', 2016, 5, 8.4, 8.2, 80000, 'https://boardgamegeek.com/boardgame/167791/terraforming-mars', 'https://cf.geekdo-images.com/wg9oOLcsKvDesSUdZQ4rxw__micro/img/LUkXZhd1TO80eCiXMD3-KfnzA6k=/fit-in/64x64/filters:strip_icc()/pic3536616.jpg'),
('Carcassonne', 2000, 150, 7.4, 7.1, 62000, 'https://boardgamegeek.com/boardgame/822/carcassonne', 'https://cf.geekdo-images.com/NSD4L9c-rY5OOlJYFlQ2Wg__micro/img/24OH1Dg8dljTUr02UMMtjD3fONg=/fit-in/64x64/filters:strip_icc()/pic5647234.png'),
('Gloomhaven', 2017, 1, 8.8, 8.6, 90000, 'https://boardgamegeek.com/boardgame/174430/gloomhaven', 'https://cf.geekdo-images.com/sZYp_3BTDGjh2unaZfZmuA__micro/img/sQyh47ClBO3d5sxPm73hMvM-JV4=/fit-in/64x64/filters:strip_icc()/pic2437871.jpg'),
('7 Wonders', 2010, 60, 7.8, 7.5, 45000, 'https://boardgamegeek.com/boardgame/68448/7-wonders', 'https://cf.geekdo-images.com/WzNs1mA_o22ZWTR8fkLP2g__micro/img/xh3isprMbt_FCg9vs3w_ifv-JXY=/fit-in/64x64/filters:strip_icc()/pic3376065.jpg'),
('Dominion', 2008, 90, 7.6, 7.3, 40000, 'https://boardgamegeek.com/boardgame/36218/dominion', 'https://cf.geekdo-images.com/OGOmpi0GgwOwH2y28QgkuA__micro/img/VlsgqS2v915vSCwTPVWFVms0-TY=/fit-in/64x64/filters:strip_icc()/pic460011.jpg'),
('Azul', 2017, 45, 7.9, 7.6, 37000, 'https://boardgamegeek.com/boardgame/230802/azul', 'https://cf.geekdo-images.com/843kZ6WR0HfyXWEybA6L7A__micro/img/856O6uUDr2GpOo4vyEUiWDLyzko=/fit-in/64x64/filters:strip_icc()/pic4930887.jpg'),
('Scythe', 2016, 12, 8.2, 8.0, 56000, 'https://boardgamegeek.com/boardgame/169786/scythe', 'https://cf.geekdo-images.com/07MRsX6Tv5elGdefTOQxsQ__micro/img/S95YtDhkxghGsLCk9xstxnXeoYQ=/fit-in/64x64/filters:strip_icc()/pic5235769.png'),
('Wingspan', 2019, 20, 8.1, 7.8, 72000, 'https://boardgamegeek.com/boardgame/266192/wingspan', 'https://cf.geekdo-images.com/yLZJCVLlIx4c7eJEWUNJ7w__micro/img/5ZaRePVhfelfofF7T_OC1e0gUCw=/fit-in/64x64/filters:strip_icc()/pic4458123.jpg'),
('Ticket to Ride', 2004, 110, 7.3, 6.9, 60000, 'https://boardgamegeek.com/boardgame/9209/ticket-ride', 'https://cf.geekdo-images.com/0K1AOciqlMVUWFPLTJSiww__micro/img/fNo9_FY6sdu7szEouS2v9IVjHfI=/fit-in/64x64/filters:strip_icc()/pic66668.jpg'),
('Pandemic', 2008, 70, 7.6, 7.2, 67000, 'https://boardgamegeek.com/boardgame/30549/pandemic', 'https://cf.geekdo-images.com/B1VZL2s3EFifndAsI3k5KA__micro/img/yGo7cXfjmOzakqlm3kdIbVm7SZc=/fit-in/64x64/filters:strip_icc()/pic4328856.jpg'),
('Brass: Birmingham', 2018, 2, 8.7, 8.5, 48000, 'https://boardgamegeek.com/boardgame/224517/brass-birmingham', 'https://cf.geekdo-images.com/moCQ39CcMSmHjnvxhkLgLg__micro/img/idSdnH7lA8BapLKnwCMFiPYVQFo=/fit-in/64x64/filters:strip_icc()/pic2729316.png'),
('Root', 2018, 18, 8.1, 7.9, 42000, 'https://boardgamegeek.com/boardgame/237182/root', 'https://cf.geekdo-images.com/x3zxjr-Vw5iU4yDPg70Jgw__micro/img/4Od3GYCiqptga0VbmyumPbJlBsU=/fit-in/64x64/filters:strip_icc()/pic3490053.jpg'),
('The Crew', 2019, 55, 8.0, 7.6, 39000, 'https://boardgamegeek.com/boardgame/284083/crew-quest-planet-nine', 'https://cf.geekdo-images.com/98LnQShydr11OBKS46xY-Q__micro/img/bIVTqYzQ5wDuCSmcQvpNokXZOUo=/fit-in/64x64/filters:strip_icc()/pic5687013.jpg'),
('Splendor', 2014, 130, 7.5, 7.1, 51000, 'https://boardgamegeek.com/boardgame/148228/splendor', 'https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__micro/img/VaWkmRffgWdhbynm-GUM4anrlic=/fit-in/64x64/filters:strip_icc()/pic1904079.jpg'),
('Codenames', 2015, 85, 7.6, 7.2, 73000, 'https://boardgamegeek.com/boardgame/178900/codenames', 'https://cf.geekdo-images.com/Q2u-Nk68Wb1iLjxh_dfsIg__micro/img/XOAPhcYFTV6_GWueoFFEYE2qSAM=/fit-in/64x64/filters:strip_icc()/pic3476592.jpg'),
('Betrayal at House on the Hill', 2004, 190, 6.8, 6.5, 31000, 'https://boardgamegeek.com/boardgame/10547/betrayal-house-hill', 'https://cf.geekdo-images.com/F4-UGFUM3FfVLWsgBgpFLQ__micro/img/FCaKmzjG7Ftl5igbteIzW4VwaVo=/fit-in/64x64/filters:strip_icc()/pic4314964.jpg'),
('Love Letter', 2012, 160, 7.2, 6.8, 28000, 'https://boardgamegeek.com/boardgame/129622/love-letter', 'https://cf.geekdo-images.com/T1ltXwapFUtghS9A7_tf4g__micro/img/Qiu0VH-5VxmCUkISsvN5-dRlrKw=/fit-in/64x64/filters:strip_icc()/pic1401448.jpg'),
('King of Tokyo', 2011, 140, 7.2, 6.9, 33000, 'https://boardgamegeek.com/boardgame/70323/king-tokyo', 'https://cf.geekdo-images.com/m_RzXpHURC0_xLkvRSR_sw__micro/img/os4ChJCgP0VGLN9WU1Ea6c4z6CE=/fit-in/64x64/filters:strip_icc()/pic3043734.jpg'),
('Everdell', 2018, 30, 8.0, 7.7, 47000, 'https://boardgamegeek.com/boardgame/199792/everdell', 'https://cf.geekdo-images.com/fjE7V5LNq31yVEW_yuqI-Q__micro/img/TAgkPCJdNAIHZfn1BE1DXadBL9g=/fit-in/64x64/filters:strip_icc()/pic3918905.png');



-- Affiche toutes les tables
SHOW TABLES;

-- Affiche le contenu de la table 'jeu'
-- Affiche toutes les tables
SHOW TABLES;

-- Affiche le contenu de la table 'jeu'
SELECT * FROM jeu;
SELECT * FROM ratings;
SELECT * FROM utilisateurs;