# Coupon-Clipper-by-Python-and-Selenium

I like to shopping at Jewelosco(also known as Safeway in other area), but every time I have to applying the digital coupons manually. With this project, the coupons in my interested categories and weekly ad could be loaded automatically. Delay added in page loading, inputting and clipping intentionally to avoid bot detection.

Marianos is my another favourite local grocery store, but their system can recognize selenium as bot easily. Please refer to issues for details.

### Method to Acchieve:
Combine Selenium automation testing tool with Python 

### Function:
Complete the following functions:
```css
Login automatically

Clip all digital coupons by category search result

Clip all weekly ad coupons
```
Following is an the video to show how it looks like when running:

https://drive.google.com/file/d/1hCV2tGzt8akWg6NttqXp_sh963wuqxdv/view?usp=sharing
### How to run:
Install Selenium, Chromedriver.exe
( download link https://chromedriver.chromium.org/downloadsmust match the version of Chrome)
Install Yaml

In config.yml file , set up email, password and catagories.

Run file JW_CPCliper.py

#### Example of config.yml file as following:

userinfo:

   email: "sfw12345@gmail.com"
  
   passowrd: "12345abcde"
  
catagory: [coca, fish]


### To do:
```css
Run the function automatically with script , for example run the script every Wednesday  at night

Retrieve Rewards summary with expire date

Email or text reminder for interested coupons or expiring rewards

```
