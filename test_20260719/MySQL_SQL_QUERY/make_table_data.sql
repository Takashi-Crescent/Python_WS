-- テーブル作成
DROP TABLE IF EXISTS xxxx;
CREATE TABLE xxxx (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(30) NOT NULL,
  `age` INT NOT NULL,
  PRIMARY KEY (`id`));

-- テーブルへのデータ挿入
INSERT INTO xxxx (name,age) VALUES
('xxxx',30),('yyyy',38),('rrrr',27),('nnnn',27),('aaaa',36),('ssss',33);
