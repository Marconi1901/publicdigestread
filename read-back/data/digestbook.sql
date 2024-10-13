/*
Navicat MySQL Data Transfer

Source Server         : aliyun
Source Server Version : 50744
Source Host           : 60.205.203.199:3306
Source Database       : digestdemo

Target Server Type    : MYSQL
Target Server Version : 50744
File Encoding         : 65001

Date: 2024-10-13 09:57:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for digestbook
-- ----------------------------
DROP TABLE IF EXISTS `digestbook`;
CREATE TABLE `digestbook` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `content` varchar(3000) DEFAULT '' COMMENT '内容',
  `bookname` varchar(255) DEFAULT '' COMMENT '书名',
  `author` varchar(255) DEFAULT '' COMMENT '作者',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=571 DEFAULT CHARSET=utf8mb4;
