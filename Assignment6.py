from PIL import Image
import pytesseract,re

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

file1 = Image.open("C:/Users/Inderjeet/PycharmProjects/data_science/amazon1-1.png")
# df = pytesseract.image_to_data(file1, lang='eng',output_type='data.frame')
# df1=df['text'].dropna()
#
# file2 = Image.open("C:/Users/Inderjeet/PycharmProjects/data_science/amazon2-1.png")
# df = pytesseract.image_to_data(file2, lang='eng',output_type='data.frame')
# df2=df['text'].dropna()
#
# file4 = Image.open("C:/Users/Inderjeet/PycharmProjects/data_science/amazon4-1.png")
# df = pytesseract.image_to_data(file4, lang='eng',output_type='data.frame')
# df4=df['text'].dropna()
#
file5 = Image.open("C:/Users/Inderjeet/PycharmProjects/data_science/amazon5-1.png")
# df = pytesseract.image_to_data(file5, lang='eng',output_type='data.frame')
# df5=df['text'].dropna()

# print(df1.to_string())

df= pytesseract.image_to_string(file5)
print(df)


gst = re.findall(r"GST Registration No: [\w]+", df)
date = re.findall(r"Invoice Date : [\S]+", df)
number = re.findall(r"Order Number: [\d—-]+[\s]+[\d-]+", df)
number1="".join(number)
number2=number1.replace(" ","")
pan=re.findall(r"PAN No: [\w]+", df)
details = re.findall(r"Invoice Details : [\w—-]+", df)
address = re.findall("Shipping Address : *\n.*\n.*\n.*\n.*\n.*", df)
address1="".join(address)
# address2=address1.replace("\n"," ")
amount = re.findall("Amount in Words: *\n.*\n.*", df)
amount1="".join(amount)
print(gst)
print(date)
print(number2)
print(pan)
print(details)
print(address1)
print(amount1)






