from tkinter import *
from PIL import ImageTk, Image      # PIL --> Pyhton Image Library
from tkinter import messagebox

def get_Url():
    Url = url.get()
    gmail = e_mail.get()
    passWd = pasxwd.get()
    tweets = tweet.get()
    if '@' or '#' in tweets:
        messagebox.showinfo('OKOK👾')
    else:
        breakpoint()
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service

    s = Service('C:/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}  ## Handle alert chrome selenium driver !!!
    chrome_options.add_experimental_option("prefs", prefs)
    driver.maximize_window()
    driver.get(Url)

    time.sleep(10)
    email = driver.find_element(By.CSS_SELECTOR, "input[name='text']")
    time.sleep(2)
    email.send_keys(gmail)

    next_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
    next_btn.click()

    time.sleep(4)
    passwd = driver.find_element(By.CSS_SELECTOR, "input[type='password']")

    time.sleep(2)
    passwd.send_keys('scraper123')

    passwd.send_keys(Keys.ENTER)

    try:
        ads_close = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/span/span')
        ads_close.click()
    except:
        pass

    time.sleep(5)
    search_tweet = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    search_tweet.send_keys(tweets)

    search_tweet.send_keys(Keys.ENTER)

    time.sleep(3)
    likes_tweets = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Likes")]')
    likes_tweets.click()

    replyclick = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Reply")]')
    replyclick.click()

    time.sleep(3)
    message = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Tweet text")]')
    message.send_keys('I love you')

    send_message = driver.find_element(By.XPATH, '//div[contains(@data-testid, "tweetButton")]')
    send_message.click()

    datas = driver.find_elements(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[.]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]')
    for j in datas:
        person = j.find_element(By.CLASS_NAME, 'css-bfa6kz')
        p_id = j.find_elements(By.CLASS_NAME, 'css-bfa6kz')[1]
        publish_time = j.find_elements(By.CLASS_NAME, 'css-4rbku5')[2]

        print(person.text, "   ----  ", p_id.text, "   ----  ", publish_time.text)

        body = driver.find_element(By.XPATH, '/html/body')
        body.send_keys(Keys.PAGE_DOWN)

    time.sleep(15)

root = Tk()

root.title('Twitter Bot🤖')
twitter_icon = PhotoImage(file='twitter_icon.png')
root.iconphoto(False, twitter_icon)     # to change the icon

# root.minsize(100, 100)      # To
# root.maxsize(300, 300)           # Miantain
root.geometry('730x650')                     # Width  &  Height
# root.configure(background='red')    # Backgroung color

background = PhotoImage(file='twitter_img')   # background image !!!
bg = Label(root, image=background)
bg.place(x=0, y=0, relheight=1, relwidth=1)


img = Image.open('twitter_img')   # location of img
img_resized = img.resize((50, 50))                     # Resize the image

img = ImageTk.PhotoImage(img_resized)
img_Label = Label(root, image=img)

img_Label.pack(pady=(7, 7), padx=(30, 180))          # image on GUI   -->> arranege ==>>{y-X}

text = Label(root, text="Twitter Bot")        # for write any text
text.configure(background="CornflowerBlue", fg="Blue", font=("Courier", 24, 'underline', 'bold'))   # font color-->size  ?
text.pack(padx=(30, 180))


text = Label(root, text="Enter Url")        # for write any text
text.configure(background="Grey", fg="black", font=('verdana', 20, 'italic'))   # font color-->size  ?
text.pack(pady=(20,20),  padx=(30, 180))

url = Entry(root, width=50)
url.configure(background="yellow", fg="red")
url.pack(pady=(20, 20), padx=(30, 180))
url.pack(ipady=3)           # height of box

g_mail = Label(root, text=" User ID ")        # for write any text
g_mail.configure(background="Pink", fg="black", font=('verdana', 20, 'italic'))   # font color-->size  ?
g_mail.pack(padx=(30, 180))

e_mail = Entry(root, width=50)
e_mail.configure(background="yellow", fg="red")
e_mail.pack(pady=(20, 20), padx=(30, 180))
e_mail.pack(ipady=3)           # height of box

password = Label(root, text="Password ")        # for write any text
password.configure(background="IndianRed", fg="black", font=('verdana', 20, 'italic'))   # font color-->size  ?
password.pack(padx=(30, 180))

pasxwd = Entry(root, width=50)
pasxwd.configure(background="yellow", fg="red")
pasxwd.pack(pady=(20, 20), padx=(30, 180))
pasxwd.pack(ipady=3)           # height of box

search_tweet = Label(root, text=" #Tweet ")        # for write any text
search_tweet.configure(background="CornflowerBlue", fg="black", font=('verdana', 20, 'italic'))   # font color-->size  ?
search_tweet.pack(padx=(30, 180))

tweet = Entry(root, width=50)
tweet.configure(background="yellow", fg="red")
tweet.pack(pady=(20, 20), padx=(30, 180))
tweet.pack(ipady=3)           # height of box

login = Button(root, text='search->here', background="orange", fg="white", command=get_Url)    # commmand for caling ftn
login.pack(pady=(20, 20), padx=(30, 180))
login.pack()

root.mainloop()
