# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceRecogUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 511, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Play_wnd = QtWidgets.QLabel(self.groupBox_2)
        self.Play_wnd.setGeometry(QtCore.QRect(10, 30, 491, 351))
        self.Play_wnd.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.Play_wnd.setText("")
        self.Play_wnd.setAlignment(QtCore.Qt.AlignCenter)
        self.Play_wnd.setObjectName("Play_wnd")
        self.GlobalImg_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.GlobalImg_groupBox.setGeometry(QtCore.QRect(520, 0, 511, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.GlobalImg_groupBox.setFont(font)
        self.GlobalImg_groupBox.setObjectName("GlobalImg_groupBox")
        self.GlobalImg_wnd = QtWidgets.QLabel(self.GlobalImg_groupBox)
        self.GlobalImg_wnd.setGeometry(QtCore.QRect(10, 30, 491, 351))
        self.GlobalImg_wnd.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.GlobalImg_wnd.setText("")
        self.GlobalImg_wnd.setObjectName("GlobalImg_wnd")
        self.FaceImg_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.FaceImg_groupBox.setGeometry(QtCore.QRect(0, 390, 511, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.FaceImg_groupBox.setFont(font)
        self.FaceImg_groupBox.setObjectName("FaceImg_groupBox")
        self.FaceImg_wnd = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.FaceImg_wnd.setGeometry(QtCore.QRect(10, 30, 261, 261))
        self.FaceImg_wnd.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.FaceImg_wnd.setLineWidth(0)
        self.FaceImg_wnd.setText("")
        self.FaceImg_wnd.setObjectName("FaceImg_wnd")
        self.label_14 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_14.setGeometry(QtCore.QRect(280, 30, 71, 20))
        self.label_14.setObjectName("label_14")
        self.face_time_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_time_label.setGeometry(QtCore.QRect(340, 30, 151, 20))
        self.face_time_label.setObjectName("face_time_label")
        self.label_10 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_10.setGeometry(QtCore.QRect(280, 50, 71, 20))
        self.label_10.setObjectName("label_10")
        self.face_sex_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_sex_label.setGeometry(QtCore.QRect(340, 50, 151, 20))
        self.face_sex_label.setObjectName("face_sex_label")
        self.label_11 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_11.setGeometry(QtCore.QRect(280, 70, 71, 20))
        self.label_11.setObjectName("label_11")
        self.face_age_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_age_label.setGeometry(QtCore.QRect(340, 70, 151, 20))
        self.face_age_label.setObjectName("face_age_label")
        self.label_15 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_15.setGeometry(QtCore.QRect(280, 90, 71, 20))
        self.label_15.setObjectName("label_15")
        self.face_race_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_race_label.setGeometry(QtCore.QRect(340, 90, 151, 20))
        self.face_race_label.setObjectName("face_race_label")
        self.label_17 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_17.setGeometry(QtCore.QRect(280, 110, 71, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_18.setGeometry(QtCore.QRect(280, 130, 71, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_19.setGeometry(QtCore.QRect(280, 150, 71, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.label_20.setGeometry(QtCore.QRect(280, 170, 71, 20))
        self.label_20.setObjectName("label_20")
        self.face_eye_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_eye_label.setGeometry(QtCore.QRect(340, 110, 151, 20))
        self.face_eye_label.setObjectName("face_eye_label")
        self.face_mouth_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_mouth_label.setGeometry(QtCore.QRect(340, 130, 151, 20))
        self.face_mouth_label.setObjectName("face_mouth_label")
        self.face_mask_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_mask_label.setGeometry(QtCore.QRect(340, 150, 151, 20))
        self.face_mask_label.setObjectName("face_mask_label")
        self.face_beard_label = QtWidgets.QLabel(self.FaceImg_groupBox)
        self.face_beard_label.setGeometry(QtCore.QRect(340, 170, 151, 20))
        self.face_beard_label.setObjectName("face_beard_label")
        self.CandidateImg_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.CandidateImg_groupBox.setGeometry(QtCore.QRect(520, 390, 511, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CandidateImg_groupBox.setFont(font)
        self.CandidateImg_groupBox.setObjectName("CandidateImg_groupBox")
        self.CandidateImg_wnd = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.CandidateImg_wnd.setGeometry(QtCore.QRect(10, 30, 261, 261))
        self.CandidateImg_wnd.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.CandidateImg_wnd.setText("")
        self.CandidateImg_wnd.setObjectName("CandidateImg_wnd")
        self.label_25 = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.label_25.setGeometry(QtCore.QRect(280, 30, 111, 20))
        self.label_25.setObjectName("label_25")
        self.candidate_name_label = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.candidate_name_label.setGeometry(QtCore.QRect(390, 30, 111, 20))
        self.candidate_name_label.setObjectName("candidate_name_label")
        self.label_27 = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.label_27.setGeometry(QtCore.QRect(280, 50, 111, 20))
        self.label_27.setObjectName("label_27")
        self.candidate_sex_label = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.candidate_sex_label.setGeometry(QtCore.QRect(390, 50, 111, 20))
        self.candidate_sex_label.setObjectName("candidate_sex_label")
        self.label_29 = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.label_29.setGeometry(QtCore.QRect(280, 70, 111, 20))
        self.label_29.setObjectName("label_29")
        self.candidate_birth_label = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.candidate_birth_label.setGeometry(QtCore.QRect(390, 70, 111, 20))
        self.candidate_birth_label.setObjectName("candidate_birth_label")
        self.label_30 = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.label_30.setGeometry(QtCore.QRect(280, 90, 111, 20))
        self.label_30.setObjectName("label_30")
        self.candidate_id_label = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.candidate_id_label.setGeometry(QtCore.QRect(390, 90, 111, 20))
        self.candidate_id_label.setObjectName("candidate_id_label")
        self.label_32 = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.label_32.setGeometry(QtCore.QRect(280, 110, 111, 20))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.label_33.setGeometry(QtCore.QRect(280, 130, 131, 20))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.label_34.setGeometry(QtCore.QRect(280, 150, 111, 20))
        self.label_34.setObjectName("label_34")
        self.candidate_library_no_label = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.candidate_library_no_label.setGeometry(QtCore.QRect(390, 110, 111, 20))
        self.candidate_library_no_label.setObjectName("candidate_library_no_label")
        self.candidate_library_name_label = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.candidate_library_name_label.setGeometry(QtCore.QRect(390, 130, 111, 20))
        self.candidate_library_name_label.setObjectName("candidate_library_name_label")
        self.candidate_similarity_label = QtWidgets.QLabel(self.CandidateImg_groupBox)
        self.candidate_similarity_label.setGeometry(QtCore.QRect(390, 150, 111, 20))
        self.candidate_similarity_label.setObjectName("candidate_similarity_label")
        self.FaceImg_groupBox.raise_()
        self.groupBox_2.raise_()
        self.GlobalImg_groupBox.raise_()
        self.CandidateImg_groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FaceRecognition"))
        self.groupBox_2.setTitle(_translate("MainWindow", "RealPlay"))
        self.GlobalImg_groupBox.setTitle(_translate("MainWindow", "Global Picture"))
        self.FaceImg_groupBox.setTitle(_translate("MainWindow", "Face Picture"))
        self.label_14.setText(_translate("MainWindow", "time:"))
        self.face_time_label.setText(_translate("MainWindow", "123123"))
        self.label_10.setText(_translate("MainWindow", "sex:"))
        self.face_sex_label.setText(_translate("MainWindow", "123123"))
        self.label_11.setText(_translate("MainWindow", "age:"))
        self.face_age_label.setText(_translate("MainWindow", "123123"))
        self.label_15.setText(_translate("MainWindow", "race:"))
        self.face_race_label.setText(_translate("MainWindow", "123123"))
        self.label_17.setText(_translate("MainWindow", "eye:"))
        self.label_18.setText(_translate("MainWindow", "mouth:"))
        self.label_19.setText(_translate("MainWindow", "mask:"))
        self.label_20.setText(_translate("MainWindow", "beard:"))
        self.face_eye_label.setText(_translate("MainWindow", "123123"))
        self.face_mouth_label.setText(_translate("MainWindow", "123123"))
        self.face_mask_label.setText(_translate("MainWindow", "123123"))
        self.face_beard_label.setText(_translate("MainWindow", "123123"))
        self.CandidateImg_groupBox.setTitle(_translate("MainWindow", "Candidate Picture"))
        self.label_25.setText(_translate("MainWindow", "name:"))
        self.candidate_name_label.setText(_translate("MainWindow", "123123"))
        self.label_27.setText(_translate("MainWindow", "sex:"))
        self.candidate_sex_label.setText(_translate("MainWindow", "123123"))
        self.label_29.setText(_translate("MainWindow", "birth:"))
        self.candidate_birth_label.setText(_translate("MainWindow", "123123"))
        self.label_30.setText(_translate("MainWindow", "id:"))
        self.candidate_id_label.setText(_translate("MainWindow", "123123"))
        self.label_32.setText(_translate("MainWindow", "group id:"))
        self.label_33.setText(_translate("MainWindow", "group name:"))
        self.label_34.setText(_translate("MainWindow", "similarity(%):"))
        self.candidate_library_no_label.setText(_translate("MainWindow", "123123"))
        self.candidate_library_name_label.setText(_translate("MainWindow", "123123"))
        self.candidate_similarity_label.setText(_translate("MainWindow", "123123"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())