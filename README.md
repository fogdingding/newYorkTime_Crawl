* 系統環境: mac air 10.15(C)
* 程式語言: python3
* tor
    * brew install tor
        * Paht: /user/loacl/etc/tor/torcc.sample
    * cd /user/local/etc/tor
    * cp torcc.sample torcc
    * tor --hash-password my_password
        * hashed password below is obtained via `tor --hash-password my_password` (copy this)
    * vim torcc
        * ControlPort 9051
        * HashedControlPassword "my_password"
        * CookieAuthentication 1
    * run tor
        * can use Terminal
            * tor
            * brew services restart tor (background)
            * brew services stop tor    (background)
    * python3 test_tor.py
        * if ip can chang, it is working.
        * 1th, is your ip
        * 2th, tor ip
        * 3th, chang tor ip.
        * 4th, crawl newYorkTime
* newYorkCrawl.py