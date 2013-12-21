
-- ---
-- Table 'rss-feed'
-- 
-- ---

DROP TABLE IF EXISTS `rss-feed`;
		
CREATE TABLE `rss-feed` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `feedurl` VARCHAR(255) NOT NULL
);

-- ---
-- Table 'rss-log'
-- 
-- ---

DROP TABLE IF EXISTS `rss-log`;
		
CREATE TABLE `rss-log` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `id-rss` INT NOT NULL,
  `hash` CHAR(64) NOT NULL,
  `date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(`id-rss`) REFERENCES `rss-feed`(`id`)
);

-- ---
-- Table 'evernote-rss'
-- 
-- ---

DROP TABLE IF EXISTS `evernote-rss`;
		
CREATE TABLE `evernote-rss` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `id-rss-feed` INT NOT NULL,
  `notebook` VARCHAR(100) NOT NULL,
  FOREIGN KEY (`id-rss-feed`) REFERENCES `rss-feed`(`id`)
);

-- ---
-- Table 'evernote-tag'
-- 
-- ---

DROP TABLE IF EXISTS `evernote-tag`;
		
CREATE TABLE `evernote-tag` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `id-evernote-rss` INT NOT NULL,
  `tag` VARCHAR(50) NOT NULL,
  FOREIGN KEY (`id-evernote-rss`) REFERENCES `evernote-rss` (`id`)
);
