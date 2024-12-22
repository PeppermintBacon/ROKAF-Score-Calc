from PyQt5 import QtCore, QtGui, QtWidgets
import random
from cerberus import Validator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 371, 91))
        font = QtGui.QFont()
        font.setFamily("새굴림")
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">대한민국 공군 합격 예측</span></p><p>ROKAF Admission Probability Calculator</p></body></html>")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        # 공군 로고 
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(80, 420, 220, 120))  
        
        pixmap = QtGui.QPixmap(r"C:\Users\USER\Downloads\Republic_of_Korea_Air_Force_emblem.png")
        scaled_pixmap = pixmap.scaled(self.label_image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_image.setPixmap(scaled_pixmap)

        self.label_image.setScaledContents(False) 
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)

        self.labels = []
        self.lineEdits = []
        placeholders = [
            "자격 점수 (60-70):", 
            "출석 점수 (16-20):", 
            "추가 점수 (0-15):", 
            "면접 점수 (34-35):", 
            "모집인원:", 
            "지원자수:"
        ]

        for i, placeholder in enumerate(placeholders):
            label = QtWidgets.QLabel(self.centralwidget)
            label.setGeometry(QtCore.QRect(30, 130 + i * 40, 150, 30))  
            label.setText(placeholder)
            self.labels.append(label)

            lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            lineEdit.setGeometry(QtCore.QRect(200, 130 + i * 40, 150, 30))  
            lineEdit.setPlaceholderText("값을 입력하세요")
            self.lineEdits.append(lineEdit)


        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate.setGeometry(QtCore.QRect(130, 370, 120, 40))  
        self.pushButton_calculate.setStyleSheet("background-color: rgba(51, 153, 255, 0.8); color: white;") 
        self.pushButton_calculate.setText("계산하기")
        self.pushButton_calculate.clicked.connect(self.calculate_scores)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.second_window = None

    def calculate_scores(self):
        inputs = {
            'qualification': float(self.lineEdits[0].text() or 0),
            'attendance': float(self.lineEdits[1].text() or 0),
            'bonus': float(self.lineEdits[2].text() or 0),
            'interview': float(self.lineEdits[3].text() or 35),
            'num_recruits': int(self.lineEdits[4].text() or 1),
            'num_applicants': int(self.lineEdits[5].text() or 1),
        }

        if not self.validate_inputs(inputs):
            QtWidgets.QMessageBox.warning(None, "Input Error", "모든 입력은 유효해야 합니다.")
            return

        total_score = self.calculate_total_score(inputs)
        simulated_scores = self.generate_sample_scores(inputs['num_applicants'])
        cutoff_score = self.determine_cutoff_score(simulated_scores, inputs['num_recruits'])

        result_text = f"1차 최종 점수: {int(total_score)}\n점수 컷: {int(cutoff_score)}\n"
        if total_score >= cutoff_score:
            final_score = total_score + inputs['interview']
            result_text += f"최종 점수: {int(final_score)}\n"
            result_text += "축하드립니다! 합격입니다! 안전한 군생활을 응원합니다!" if final_score >= cutoff_score + 34 else "불합격"
        else:
            result_text += "불합격입니다. 다음 달에 지원해보세요!\n"

        self.show_result_window(result_text)

    def validate_inputs(self, inputs):
        schema = {
            'qualification': {'type': 'float', 'min': 60, 'max': 70},
            'attendance': {'type': 'float', 'min': 16, 'max': 20},
            'bonus': {'type': 'float', 'min': 0, 'max': 15},
            'interview': {'type': 'float', 'min': 34, 'max': 35, 'default': 35},
            'num_recruits': {'type': 'integer', 'min': 1},
            'num_applicants': {'type': 'integer', 'min': 1},
        }
        v = Validator(schema)
        return v.validate(inputs)

    def calculate_total_score(self, inputs):
        qualification = min(max(inputs['qualification'], 60), 70)
        attendance = min(max(inputs['attendance'], 16), 20)
        bonus = min(max(inputs['bonus'], 0), 15)
        return qualification + attendance + bonus

    def generate_sample_scores(self, num_samples):
        scores = []
        for _ in range(num_samples):
            rand = random.random()
            if rand < 0.3:
                scores.append(98)
            elif rand < 0.6:
                scores.append(99)
            elif rand < 0.7:
                scores.append(97)
            elif rand < 0.8:
                scores.append(96)
            else:
                scores.append(random.choice(list(range(76, 96)) + list(range(100, 106))))
        return scores

    def determine_cutoff_score(self, all_scores, num_recruits):
        sorted_scores = sorted(all_scores, reverse=True)
        cutoff_index = min(num_recruits, len(sorted_scores)) - 1
        return sorted_scores[cutoff_index] if cutoff_index >= 0 else 0

    def show_result_window(self, result_text):
        if self.second_window is None:
            self.second_window = QtWidgets.QWidget()
            self.second_window.setWindowTitle("결과")
            self.second_window.setGeometry(400, 100, 300, 200)
            self.second_window.setStyleSheet("background-color: #f0f0f0;")

            self.label_result = QtWidgets.QLabel(self.second_window)
            self.label_result.setGeometry(QtCore.QRect(10, 10, 280, 100))
            self.label_result.setWordWrap(True)  
            self.label_result.setAlignment(QtCore.Qt.AlignCenter)  
            self.label_result.setText(result_text)

                    
            self.button_reset_result = QtWidgets.QPushButton(self.second_window)
            self.button_reset_result.setGeometry(QtCore.QRect(40, 150, 100, 30))
            self.button_reset_result.setStyleSheet("background-color: rgba(169, 169, 169, 0.8); color: white;")
            self.button_reset_result.setText("다시하기")
            self.button_reset_result.clicked.connect(self.reset)

            
            self.button_exit_result = QtWidgets.QPushButton(self.second_window)
            self.button_exit_result.setGeometry(QtCore.QRect(160, 150, 100, 30))
            self.button_exit_result.setStyleSheet("background-color: rgba(219, 68, 85, 0.8); color: white;")
            self.button_exit_result.setText("종료하기")
            self.button_exit_result.clicked.connect(self.exit)

        self.label_result.setText(result_text)
        self.second_window.show()

    def reset(self):
        for lineEdit in self.lineEdits:
            lineEdit.clear()
        self.second_window.close()

    def exit(self):
        QtWidgets.qApp.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
