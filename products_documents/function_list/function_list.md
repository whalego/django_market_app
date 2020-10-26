## ログイン認証
| function_name | url_pattern | about |
| ---- | --- | ---- |
| ログイン | login_oauth | 各アカウントをDBのデータと都合する。 |
| ログアウト | logout | 各対象アカウントのログアウト |


## アカウント管理
| function_name | url_pattern | about |
| ---- | --- | ---- |
| 企業アカウントの作成 | make_company_account | 企業アカウントの作成 |
| 企業アカウントの削除 | delete_company_account | 企業アカウントの削除<br>(削除フラグを1にする) |
| 企業アカウントの更新 | update_company_account | 企業アカウントの情報を更新 |
| 利用者アカウントの作成 | make_user_account | 利用者アカウントの作成 |
| 利用者アカウントの削除 | delete_user_account | 利用者アカウントの削除<br>(削除フラグを１にする) |
| 利用者アカウントの更新 | update_user_account | 利用者アカウントの更新 |
| システム管理者アカウントの作成 | make_system_admin_account | システム管理者のアカウントの作成<br>(更新は行わないものとする) |
| システム管理者アカウントの削除 | delete_system_admin_account | システム管理者アカウントの削除<br>(削除フラグを１にする) |
| 各ユーザのパスワードリセット | reset_password | システム管理者がシステム管理者以外のユーザの<br>パスワードをリセットする |

## 商品管理
| function_name | url_pattern | about |
| ---- | --- | ---- |
| 商品の登録 | add_item | 企業アカウントから商品の登録を行う |
| 商品の削除 | delete_item | 企業アカウントとシステム管理者からの商品の削除を行う |
| 商品の情報更新 | update_item | 企業アカウントとシステム管理者からの商品の更新を行う |
| 商品の表示 | show_item | 全ユーザーが使う商品の一覧の取得 |
| 商品の購入 | buy_item | 利用者が商品の購入を行う |
| 買い物かごの更新 | update_item_bucket | 利用者の購入予定商品の更新 |
| 買い物かごの情報表示 | show_item_bucket | 利用者の購入予定商品の詳細表示 |
| 購入履歴の閲覧 | show_purchase_history | 利用者とシステム管理者からの購入履歴の閲覧 |

