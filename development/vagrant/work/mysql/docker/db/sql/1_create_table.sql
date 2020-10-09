-- Project Name  market_app
-- DateTime     20201007 174713
-- Author        Master_k
-- RDBMS Type    MySQL
-- Application   A5SQL Mk-2

/*
  BackupToTempTable, RestoreFromTempTable�^�����߂��t������Ă��܂��B
  ����ɂ��Adrop table, create table ����f�[�^���c��܂��B
  ���̋@�\�͈ꎞ�I�� $$TableName �̂悤�Ȉꎞ�e�[�u�����쐬���܂��B
*/

-- �Ǘ���
-- RestoreFromTempTable
create table system_admin_infomation (
  id CHAR(36) not null comment '�V�X�e���Ǘ���ID'
  , password TEXT not null comment '�V�X�e���Ǘ��҃p�X���[�h'
  , created_at DATETIME not null comment '�쐬����'
  , deleted_at DATETIME comment '�폜����'
  , constraint system_admin_infomation_PKC primary key (id)
) comment '�Ǘ���' ;

-- ����������
-- RestoreFromTempTable
create table shopping_cart (
  user_id CHAR(36) not null comment '���p��ID'
  , item_id CHAR(36) not null comment '���iID'
  , item_count INT not null comment '�w����'
  , updated_at DATETIME not null comment '�X�V����'
) comment '����������' ;

-- �w������
-- RestoreFromTempTable
create table purchase_history (
  user_id CHAR(36) not null comment '���p��ID'
  , item_id CHAR(36) not null comment '���iID'
  , item_count INT not null comment '�w����'
  , purchased_at DATETIME not null comment '�w������'
) comment '�w������' ;

-- ���p�ҏ��
-- RestoreFromTempTable
create table user_infomation (
  id CHAR(36) not null comment '���p��ID'
  , password TEXT not null comment '���p�҃p�X���[�h'
  , name VARCHAR(256) not null comment '���p�Җ�'
  , name_kana VARCHAR(512) not null comment '���p�҂ӂ肪��'
  , mail_address VARCHAR(255) not null comment '���p�҃��[���A�h���X'
  , address VARCHAR(256) not null comment '���p�ҏZ��'
  , address_kana VARCHAR(512) comment '���p�ҏZ���ӂ肪��'
  , zip_code CHAR(7) not null comment '���p�җX�֔ԍ�'
  , created_at DATETIME not null comment '���p�ҍ쐬����'
  , updated_at DATETIME comment '���p�ҍX�V����'
  , deleted_at DATETIME comment '���p�ҍ폜����'
  , is_deleted TINYINT(1) default 0 not null comment '�폜�t���O'
  , constraint user_infomation_PKC primary key (id)
) comment '���p�ҏ��' ;

-- ���i�]��
-- RestoreFromTempTable
create table item_review (
  id CHAR(36) not null comment '�]��ID'
  , item_id CHAR(36) not null comment '���iID'
  , review FLOAT(2,1) not null comment '���r���['
  , rate FLOAT(2,1) not null comment '���[�g'
  , constraint item_review_PKC primary key (id)
) comment '���i�]��' ;

-- ���i�J�e�S���[
-- RestoreFromTempTable
create table categories (
  id TINYINT not null comment '�J�e�S���[ID'
  , name VARCHAR(128) not null comment '�J�e�S���[��'
  , constraint categories_PKC primary key (id)
) comment '���i�J�e�S���[' ;

-- �����
-- RestoreFromTempTable
create table tax (
  id TINYINT(2) not null comment '����ŊǗ��ԍ�0-10, 1-8, 2-�\��'
  , tax SMALLINT(3) not null comment '�l'
  , constraint tax_PKC primary key (id)
) comment '�����' ;

-- ���i���
-- RestoreFromTempTable
create table item_infomation (
  id CHAR(36) not null comment '���iIDUUID(v4)'
  , name VARCHAR(256) not null comment '���i��'
  , price BIGINT not null comment '���i���i'
  , tax_id TINYINT(2) default 0 not null comment '�ŋ�ID0-10, 1-8, 2-�\��'
  , infomation TEXT comment '���'
  , stock INT not null comment '�݌�'
  , categories_one TINYINT comment '�J�e�S���[1'
  , categories_two TINYINT comment '�J�e�S���[2'
  , categories_three TINYINT comment '�J�e�S���[3'
  , created_company_id CHAR(36) not null comment '�o�^���'
  , created_at DATETIME not null comment '���i�쐬����'
  , updated_at DATETIME comment '���i�X�V����'
  , deleted_at DATETIME comment '���i�폜����'
  , is_deleted TINYINT(1) default 0 not null comment '�폜�t���O'
  , constraint item_infomation_PKC primary key (id)
) comment '���i���' ;

-- ��Ə��
-- RestoreFromTempTable
create table company_infomation (
  id CHAR(36) not null comment '���IDUUID(v4)'
  , password TEXT not null comment '��Ѓp�X���[�h'
  , name VARCHAR(256) not null comment '��Ж�'
  , name_kana VARCHAR(512) not null comment '��Ж��ӂ肪��'
  , phone_number VARCHAR(16) not null comment '��Ђ̓d�b�ԍ�'
  , mail_address VARCHAR(255) not null comment '��Ѓ��[���A�h���X'
  , address VARCHAR(256) not null comment '��ЏZ��'
  , address_kana VARCHAR(512) comment '��ЏZ���ӂ肪��'
  , zip_code CHAR(7) comment '��ЗX�֔ԍ�'
  , infomation TEXT comment '��А���'
  , logo_image MEDIUMTEXT comment '��Ѓ��S��16MB�܂ŋ��e'
  , created_at DATETIME not null comment '��Ѝ쐬����'
  , updated_at DATETIME comment '��ЍX�V����'
  , deleted_at DATETIME comment '��Ѝ폜����'
  , is_deleted TINYINT(1) default 0 not null comment '��Ѝ폜�t���O'
  , constraint company_infomation_PKC primary key (id)
) comment '��Ə��' ;
