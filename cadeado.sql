CREATE DATABASE cadeado;

CREATE TABLE IF NOT EXISTS `cadeado` (
  `id` int(11) NOT NULL auto_increment,
  `nome` varchar(45) NOT NULL,
  `senha` varchar(6) NOT NULL,
  `desabilitado` tinyint(1) default '0',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

CREATE TABLE IF NOT EXISTS `ramal` (
  `id` int(11) NOT NULL auto_increment,
  `ramal` varchar(10) NOT NULL,
  `desabilitado` tinyint(1) default '0',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

