import sys
from threading import Thread
from time import sleep
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import data
import pkg_resources.py2_warn


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./icon/ZZicon.ico"))
hotel = data.Hotel()
# hotel.hours.setStyleSheet('QLabel[time="true"]{border-image: url(./icon/rili.png);}')
# hotel.minute.setStyleSheet('QLabel[time="true"]{border-image: url(./icon/rili.png);}')
# hotel.week.setStyleSheet('QLabel[time="true"]{border-image: url(./icon/rili.png);}')

# 循环显示图片的线程
thread_pics = Thread(target=hotel.open_image)
# 实时显示价格的线程
thread_price = Thread(target=hotel.print_price)
# 显示天气的线程
thread_weather = Thread(target=hotel.print_weather)
# 显示时间线程
thread_time = Thread(target=hotel.print_time)
# 显示message线程
thread_message = Thread(target=hotel.print_message)

hotel.show()
sleep(1)

thread_price.start()
thread_weather.start()
thread_time.start()
thread_message.start()
thread_pics.start()

sys.exit(app.exec())




