
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table gerrit_test.inline_comments
CREATE TABLE IF NOT EXISTS `inline_comments` (
  `comment_id` varchar(255) DEFAULT NULL,
  `request_id` int(11) NOT NULL,
  `in_reply_to` varchar(255) DEFAULT NULL,
  `patchset_id` int(11) NOT NULL,
  `file_name` varchar(1023) DEFAULT NULL,
  `line_number` int(11) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `written_on` datetime DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `side` varchar(50) DEFAULT NULL,
  `message` text,
  `start_line` smallint(6) DEFAULT NULL,
  `end_line` smallint(6) DEFAULT NULL,
  `start_character` smallint(6) DEFAULT NULL,
  `end_character` smallint(6) DEFAULT NULL,
  `sentiment_score` int(11) DEFAULT NULL,
  KEY `comment_id` (`comment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `patches` (
  `patch_id` int(10) NOT NULL AUTO_INCREMENT,
  `request_id` int(10) DEFAULT NULL,
  `revision` varchar(255) DEFAULT NULL,
  `patchset_number` int(10) DEFAULT NULL,
  `comment_count` int(10) DEFAULT NULL,
  `subject` varchar(2048) DEFAULT NULL,
  `message` text,
  `checkout` varchar(1024) DEFAULT NULL,
  `cherrypick` varchar(1024) DEFAULT NULL,
  `format` varchar(1024) DEFAULT NULL,
  `pull` varchar(1024) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `committer` varchar(255) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `committed` datetime DEFAULT NULL,
  PRIMARY KEY (`patch_id`)
) ENGINE=MyISAM AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `patch_details` (
  `request_id` int(11) NOT NULL,
  `patchset_id` int(11) NOT NULL,
  `file_name` varchar(1024) NOT NULL,
  `change_type` varchar(10) DEFAULT NULL,
  `insertions` int(11) DEFAULT NULL,
  `deletions` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `people` (
  `gerrit_id` int(11) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `preferred_email` varchar(200) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `avatar` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`gerrit_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `requests` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `gerrit_id` int(11) NOT NULL,
  `gerrit_key` varchar(255) NOT NULL,
  `owner` int(11) DEFAULT NULL,
  `subject` varchar(1023) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `project` varchar(255) DEFAULT NULL,
  `branch` varchar(1024) DEFAULT NULL,
  `topic` varchar(1024) DEFAULT NULL,
  `starred` tinyint(1) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `sort_key` varchar(64) DEFAULT NULL,
  `owner_name` varchar(255) DEFAULT NULL,
  `owner_email` varchar(255) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `insertions` int(11) DEFAULT NULL,
  `deletions` int(11) DEFAULT NULL,
  PRIMARY KEY (`request_id`),
  KEY `gerrit_id` (`gerrit_id`),
  KEY `project_id` (`project_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12366 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `request_detail` (
  `request_id` int(10) NOT NULL,
  `gerrit_id` varchar(255) DEFAULT NULL,
  `project` varchar(255) DEFAULT NULL,
  `branch` varchar(255) NOT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `change_id` varchar(127) DEFAULT NULL,
  `subject` varchar(512) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `insertions` int(11) DEFAULT NULL,
  `deletions` int(11) DEFAULT NULL,
  `sort_key` varchar(127) DEFAULT NULL,
  `mergeable` tinyint(4) DEFAULT NULL,
  `owner` int(11) DEFAULT NULL,
  `number_patches` tinyint(4) DEFAULT NULL,
  `curent_patch_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `reviews` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `request_id` int(10) DEFAULT NULL,
  `people_id` int(10) DEFAULT NULL,
  `verified` tinyint(4) DEFAULT NULL,
  `reviewed` tinyint(4) DEFAULT NULL,
  `build` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `review_comments` (
  `comments_id` int(10) NOT NULL AUTO_INCREMENT,
  `request_id` int(10) NOT NULL,
  `message_id` varchar(50) DEFAULT NULL,
  `patchset_id` tinyint(4) DEFAULT NULL,
  `author` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `message` text,
  `sentiment_score` int(11) DEFAULT NULL,
  PRIMARY KEY (`comments_id`)
) ENGINE=MyISAM AUTO_INCREMENT=349 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
