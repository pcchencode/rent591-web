# 實作說明
1. 資料源：[591 房屋交易租屋網](https://rent.591.com.tw/?kind=0&region=1)

2. 安裝所需套件
    ```
    $ pip install -r requirements.txt
    ```
    * 安裝 mongodb 環境
    ```
    $ docker run -p 127.0.0.1:27017:27017 --name some-mongo -d mongo
    ```
3. 爬蟲程式：
    * `taipei_crawler_591.py` &#8594; 爬取臺北市所有出租物件
        ```
        $ python3 taipei_crawler_591.py
        ```

    * `new_taipei_crawler_591.py` &#8594; 爬取新北市所有出租物件
        ```
        $ python3 new_taipei_crawler_591.py
        ```
4. api：
    * 執行 flask-api：
        ```
        $ cd api
        $ python3 app.py
        ```
5. api 規格:
    ### 條件一：`男生可承租`且`位於新北`的物件
    * 瀏覽器輸入：`http://127.0.0.1:5000/male-new-taipei`

    ### 條件二：以`聯絡固話`查詢物件
    * 瀏覽器輸入：`http://127.0.0.1:5000/phone/{your_phone_number}`

    ### 條件三：`非屋主自行刊登`的物件
    * 瀏覽器輸入：`http://127.0.0.1:5000/non-owner`

    ### 條件四：`臺北`、`屋主為女性`、的物件
    * 瀏覽器輸入：`http://127.0.0.1:5000/taipei-miss-wu`  

    ### 一般查詢
    * 瀏覽器輸入：`http://127.0.0.1:5000/query/?region={value}&renter={value}&......`
        * `region`： string 地區
        * `renter`： string 出租者
        * `renter_type`： string 出租者身份
        * `obj_type`： string 物件型態
        * `phone`： string 聯絡固話
        * `status`： string 物件狀況
        * `gender_req`： string 性別要求
