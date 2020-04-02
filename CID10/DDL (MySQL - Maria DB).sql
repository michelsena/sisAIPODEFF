CREATE TABLE `cid10`.`cid_capitulo` ( 
`id` INT NOT NULL , 
`cat_inicio` VARCHAR(3) NOT NULL , 
`cat_fim` VARCHAR(3) NOT NULL , 
`descricao` VARCHAR(150) NOT NULL ) 
ENGINE = InnoDB;

CREATE TABLE `cid10`.`cid_grupo` (
 `id` INT NOT NULL , `capitulo_id` INT NOT NULL , 
 `cat_inicio` VARCHAR(3) NOT NULL ,
 `cat_fim` VARCHAR(3) NOT NULL , 
 `descricao` VARCHAR(150) NOT NULL )
 ENGINE = InnoDB;
 
 CREATE TABLE `cid_categoria` (
  `id` varchar(3) NOT NULL,
  `descricao` varchar(150) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE `cid_sub_categoria` (
  `id` varchar(4) NOT NULL,
  `descricao` varchar(150) NOT NULL
) ENGINE=InnoDB;