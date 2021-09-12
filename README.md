# NSE-Scanner-1

# NSE-Scanner-1
#Requirements 
1. Python
2. pandas package
3. requests package
4. BeautifulSoup pckage



# Run steps
1. open command prompt in widows 
2. on command prompt go to directory where 'nse1.py' is downloaded
3. run following commad 
   python nse1.py "NIFTY 100"
4. you should see some output as follows  (sample)
   
Number of arguments: 1
NIFTY 100
https://www.nseindia.com/api/equity-stockIndices?index=NIFTY 100
===========Date 12/09/2021
=========== NIFTY 100
=========== Open=High (Sell) ===========
======================================
         Symbol       Open       High
======================================
        SBICARD     1138.0     1138.0
     MUTHOOTFIN     1548.0     1548.0


=========== Open=Low (Buy) ===========
======================================
         Symbol       Open        Low
======================================
      TATASTEEL     1420.0     1420.0
       BOSCHLTD    14200.0    14200.0
     ASIANPAINT     3305.0     3305.0
     HINDUNILVR     2782.0     2782.0
     
     
5. Various command line options can be supplied based on which category stocks needs to be scanned .
   for example.
   python nse1.py "NIFTY 50"
   python nse1.py "NIFTY AUTO"
   python nse1.py "NIFTY 500"
