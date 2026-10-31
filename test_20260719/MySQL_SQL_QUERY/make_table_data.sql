-- テーブル作成
DROP TABLE IF EXISTS avgal_list_001;
CREATE TABLE avgal_list_001 (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(30) NOT NULL,
  `age` INT NOT NULL,
  PRIMARY KEY (`id`));

-- テーブルへのデータ挿入
INSERT INTO avgal_list_001 (name,age) VALUES
('黒川すみれ',30),('ジュリア',38),('吉良りん',27),('新村あかり',27),('AIKA',36),('仲村みう',33);
