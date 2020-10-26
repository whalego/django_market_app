## ログイン認証
| function_name | url_pattern | about |
| ---- | --- | ---- |
| システム管理者アカウントのログイン | Admin_Login | 管理者アカウントを突合しトークンの発行を行う |
| システム管理者アカウントのトークンの検証 | Admin_Auth | ヘッダーに含まれたトークンの検証を行う |
| 企業アカウントのログイン | Company_Login | 企業アカウントを突合しトークンの発行を行う |
| 企業アカウントのトークンの検証 | Company_Auth | ヘッダーに含まれたトークンの検証を行う |
| 利用者アカウントのログイン | User_Login | 利用者アカウントを突合しトークンの発行を行う |
| 利用者アカウントのトークンの検証 | User_Auth | ヘッダーに含まれたトークンの検証を行う |

## アカウント管理
| function_name | url_pattern | about |
| ---- | --- | ---- |
| 企業アカウントの作成 | Make_Company_Account | 企業アカウントの作成 |
| 企業アカウントの削除 | Delete_Company_Account | 企業アカウントの削除<br>(削除フラグを1にする) |
| 企業アカウントの更新 | Update_Company_Account | 企業アカウントの情報を更新 |
| 利用者アカウントの作成 | Make_User_Account | 利用者アカウントの作成 |
| 利用者アカウントの削除 | Delete_User_Account | 利用者アカウントの削除<br>(削除フラグを１にする) |
| 利用者アカウントの更新 | Update_User_Account | 利用者アカウントの更新 |
| システム管理者アカウントの作成 | Make_System_Admin_Account | システム管理者のアカウントの作成<br>(更新は行わないものとする) |
| システム管理者アカウントの削除 | Delete_System_Admin_Account | システム管理者アカウントの削除<br>(削除フラグを１にする) |
| 各ユーザのパスワードリセット | Reset_Password | システム管理者がシステム管理者以外のユーザの<br>パスワードをリセットする |

## 商品管理
| function_name | url_pattern | about |
| ---- | --- | ---- |
| 商品の登録 | Add_Item | 企業アカウントから商品の登録を行う |
| 商品の削除 | Delete_Item | 企業アカウントとシステム管理者からの商品の削除を行う |
| 商品の情報更新 | Update_Item | 企業アカウントとシステム管理者からの商品の更新を行う |
| 全ての商品を表示 | Show_Item | 全ユーザーが使う商品の一覧の取得 |
| 商品の詳細表示| Show_Item_Detail | 全ユーザが使う商品の詳細表示 |
| 商品の購入 | Buy_Item | 利用者が商品の購入を行う |
| 買い物かごの更新 | Update_Item_Bucket | 利用者の購入予定商品の更新 |
| 買い物かごの情報表示 | Show_Item_Bucket | 利用者の購入予定商品の詳細表示 |
| 購入履歴の閲覧 | Show_Purchase_History | 利用者とシステム管理者からの購入履歴の閲覧 |

