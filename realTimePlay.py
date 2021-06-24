"""

Prog: Real time video from IP camera
IP: 10.88.97.100
Port: 37777
Username: admin
Password: kku12345678
Author: Thinnaphat Sodanat, KKU.
Date: 5/20/2021 2:30 PM

Ref: Dahua NetSDK Python 64bit
URL: https://www.dahuasecurity.com/support/downloadCenter/softwares?child=3&fbclid=IwAR16h0YwfseLYXatNLfu3YuRRlQhve2ipAlJ-rnnQwiBkKCmGuZft5CIB8U

"""

# coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ctypes import *

from design2 import Ui_MainWindow

from NetSDK.NetSDK import NetClient
from NetSDK.SDK_Callback import fDisConnect, fHaveReConnect, fDecCBFun, fRealDataCallBackEx2
from NetSDK.SDK_Enum import SDK_RealPlayType, EM_LOGIN_SPAC_CAP_TYPE, EM_REALDATA_FLAG
from NetSDK.SDK_Struct import C_LLONG, sys_platform, NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY, NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY, PLAY_FRAME_INFO

class myMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(myMainWindow, self).__init__(parent)
        self.setupUi(self)

        # interface initialization
        self._init_ui()

        # related variables and callbacks used by NetSDK
        self.loginID = C_LLONG()
        self.playID = C_LLONG()
        self.freePort = c_int()
        self.m_DisconnectCallBack = fDisConnect(self.DisConnectCallBack)
        self.m_ReconnectCallBack = fHaveReConnect(self.ReConnectCallBack)

        # get NetSDK object and initialize
        self.sdk = NetClient()
        self.sdk.InitEx(self.m_DisconnectCallBack)
        self.sdk.SetAutoReconnect(self.m_ReconnectCallBack)

        # login section
        ip = '10.88.97.100'
        port = 37777
        username = 'admin'
        password = 'kku12345678'
        # channel of IP camera 0 = DOOR, 1 = STAIR, 2 = IOT-1, 3 = IOT-2, 4 = STORE, 5 = CAM1
        channel = 2
        # main-stream
        stream_type = SDK_RealPlayType.Realplay
        # sub-stream
        # stream_type = SDK_RealPlayType.Realplay_1

        stuInParam = NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
        stuInParam.dwSize = sizeof(NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY)
        stuInParam.szIP = ip.encode()
        stuInParam.nPort = port
        stuInParam.szUserName = username.encode()
        stuInParam.szPassword = password.encode()
        stuInParam.emSpecCap = EM_LOGIN_SPAC_CAP_TYPE.TCP
        stuInParam.pCapParam = None

        stuOutParam = NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
        stuOutParam.dwSize = sizeof(NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)

        # login and play video (real-time)
        self.loginID, device_info, error_msg = self.sdk.LoginWithHighLevelSecurity(stuInParam, stuOutParam)
        self.playID = self.sdk.RealPlayEx(self.loginID, channel, self.PlayWnd.winId(), stream_type)

        # # face detection (draw a rectangle on faces)
        # result = self.sdk.RenderPrivateData(self.playID, True)
        # if not result:
        #     QMessageBox.about(self, 'prompt', self.sdk.GetLastErrorMessage())

    # initialize the interface
    def _init_ui(self):
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())

    # Realize the function of disconnection callback function
    def DisConnectCallBack(self):
        self.setWindowTitle("OffLine")

    # Realize the function of disconnection and reconnection callback function
    def ReConnectCallBack(self):
        self.setWindowTitle('OnLine')

    # Clean up resources when closing the main window
    def closeEvent(self, event):
        event.accept()
        if  self.loginID:
            self.sdk.Logout(self.loginID)
        self.sdk.Cleanup()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_wnd = myMainWindow()
    my_wnd.show()
    sys.exit(app.exec_())