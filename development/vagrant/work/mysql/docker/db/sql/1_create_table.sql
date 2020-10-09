-- Project Name  market_app
-- DateTime     20201007 174713
-- Author        Master_k
-- RDBMS Type    MySQL
-- Application   A5SQL Mk-2

/*
  BackupToTempTable, RestoreFromTempTable疑似命令が付加されています。
  これにより、drop table, create table 後もデータが残ります。
  この機能は一時的に $$TableName のような一時テーブルを作成します。
*/

-- 管理者
-- RestoreFromTempTable
create table system_admin_infomation (
  id CHAR(36) not null comment 'システム管理者ID'
  , password TEXT not null comment 'システム管理者パスワード'
  , created_at DATETIME not null comment '作成日時'
  , deleted_at DATETIME comment '削除日時'
  , constraint system_admin_infomation_PKC primary key (id)
) comment '管理者' ;

-- 買い物かご
-- RestoreFromTempTable
create table shopping_cart (
  user_id CHAR(36) not null comment '利用者ID'
  , item_id CHAR(36) not null comment '商品ID'
  , item_count INT not null comment '購入個数'
  , updated_at DATETIME not null comment '更新日時'
) comment '買い物かご' ;

-- 購入履歴
-- RestoreFromTempTable
create table purchase_history (
  user_id CHAR(36) not null comment '利用者ID'
  , item_id CHAR(36) not null comment '商品ID'
  , item_count INT not null comment '購入個数'
  , purchased_at DATETIME not null comment '購入日時'
) comment '購入履歴' ;

-- 利用者情報
-- RestoreFromTempTable
create table user_infomation (
  id CHAR(36) not null comment '利用者ID'
  , password TEXT not null comment '利用者パスワード'
  , name VARCHAR(256) not null comment '利用者名'
  , name_kana VARCHAR(512) not null comment '利用者ふりがな'
  , mail_address VARCHAR(255) not null comment '利用者メールアドレス'
  , address VARCHAR(256) not null comment '利用者住所'
  , address_kana VARCHAR(512) comment '利用者住所ふりがな'
  , zip_code CHAR(7) not null comment '利用者郵便番号'
  , created_at DATETIME not null comment '利用者作成日時'
  , updated_at DATETIME comment '利用者更新日時'
  , deleted_at DATETIME comment '利用者削除日時'
  , is_deleted TINYINT(1) default 0 not null comment '削除フラグ'
  , constraint user_infomation_PKC primary key (id)
) comment '利用者情報' ;

-- 商品評価
-- RestoreFromTempTable
create table item_review (
  id CHAR(36) not null comment '評価ID'
  , item_id CHAR(36) not null comment '商品ID'
  , review FLOAT(2,1) not null comment 'レビュー'
  , rate FLOAT(2,1) not null comment 'レート'
  , constraint item_review_PKC primary key (id)
) comment '商品評価' ;

-- 商品カテゴリー
-- RestoreFromTempTable
create table categories (
  id TINYINT not null comment 'カテゴリーID'
  , name VARCHAR(128) not null comment 'カテゴリー名'
  , constraint categories_PKC primary key (id)
) comment '商品カテゴリー' ;

-- 消費税
-- RestoreFromTempTable
create table tax (
  id TINYINT(2) not null comment '消費税管理番号0-10, 1-8, 2-予備'
  , tax SMALLINT(3) not null comment '値'
  , constraint tax_PKC primary key (id)
) comment '消費税' ;

-- 商品情報
-- RestoreFromTempTable
create table item_infomation (
  id CHAR(36) not null comment '商品IDUUID(v4)'
  , name VARCHAR(256) not null comment '商品名'
  , price BIGINT not null comment '商品価格'
  , tax_id TINYINT(2) default 0 not null comment '税金ID0-10, 1-8, 2-予備'
  , infomation TEXT comment '情報'
  , stock INT not null comment '在庫'
  , categories_one TINYINT comment 'カテゴリー1'
  , categories_two TINYINT comment 'カテゴリー2'
  , categories_three TINYINT comment 'カテゴリー3'
  , created_company_id CHAR(36) not null comment '登録会社'
  , created_at DATETIME not null comment '商品作成日時'
  , updated_at DATETIME comment '商品更新日時'
  , deleted_at DATETIME comment '商品削除日時'
  , is_deleted TINYINT(1) default 0 not null comment '削除フラグ'
  , constraint item_infomation_PKC primary key (id)
) comment '商品情報' ;

-- 企業情報
-- RestoreFromTempTable
create table company_infomation (
  id CHAR(36) not null comment '会社IDUUID(v4)'
  , password TEXT not null comment '会社パスワード'
  , name VARCHAR(256) not null comment '会社名'
  , name_kana VARCHAR(512) not null comment '会社名ふりがな'
  , phone_number VARCHAR(16) not null comment '会社の電話番号'
  , mail_address VARCHAR(255) not null comment '会社メールアドレス'
  , address VARCHAR(256) not null comment '会社住所'
  , address_kana VARCHAR(512) comment '会社住所ふりがな'
  , zip_code CHAR(7) comment '会社郵便番号'
  , infomation TEXT comment '会社説明'
  , logo_image MEDIUMTEXT comment '会社ロゴ約16MBまで許容'
  , created_at DATETIME not null comment '会社作成日時'
  , updated_at DATETIME comment '会社更新日時'
  , deleted_at DATETIME comment '会社削除日時'
  , is_deleted TINYINT(1) default 0 not null comment '会社削除フラグ'
  , constraint company_infomation_PKC primary key (id)
) comment '企業情報' ;
