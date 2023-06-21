from PyQt5.QtGui import QIcon

class Theme:
    def change_theme(self):
        if self.styleSheet() == self.current_theme:
            # Carregue o arquivo CSS para o novo tema desejado
            new_icon = QIcon(":/imagens/img/desligar.png")
            new_theme = """
                *{
                    border:none;
                    background-color: transparent;
                    background: transparent;
                    padding:0;
                    margin:0;
                }
                #centralwidget{
                    background-color: #F5FFFA;

                }
                #leftMenuSubContainer{
                    background-color: #004d61;
                }
                #leftMenuSubContainer QPushButton{
                    background-color: #004d61;
                    text-align: left;
                    padding:3px 10px;
                    color: #ffffff;
                }
                #frame_3 QPushButton{
                    background-color: #004d61;
                    text-align: left;
                    padding:3px 10px;
                    border-top-left-radius:10px;
                    border-bottom-left-radius:10px;
                }
                #centerMenuSubContainer{
                    background-color: #348498;
                }
                #centerMenuSubContainer QLabel{
                    color: #ffffff;
                }
                #comboBoxApp, #comboBoxCartao {
                    background-color:#fff;
                    font-size: 16px;
                    color: #348498;
                    font-family: Arial;
                    border-radius:10px;
                    border: 2px solid #348498;
                    padding-left: 5px;
                }
                #pageLacon QTabWidget::pane {
                    background: transparent;
                    border:none;
                }
                #pageLacon QTabBar::tab {
                    color: #A6A6A6;
                }
                #pageLacon QTabBar::tab:selected {
                    color: #000000;
                }
                #widgetInfo, #widgetSettings, #popupNotificationContantContainer{
                    background-color: #004d61;
                    border-radius:10px;
                }
                #headerContainer, #footerContainer ,#footerContainer QLabel{
                    background-color: #348498;
                    color: #ffffff;
                }

                /* Outros seletores de estilo para widgets */

            """

        else:
            # Caso contrário, restaure a folha de estilos do tema anterior
            new_theme = self.current_theme
            new_icon = QIcon(":/imagens/img/ligar.png") 

        # Aplique o novo tema para o aplicativo
        self.setStyleSheet(new_theme)
        self.ui.temaBtn.setIcon(new_icon)

        # Atualizar o estilo dos botões ativados
        buttons_list = [self.ui.homeBtn, self.ui.appBtn, self.ui.cardBtn, self.ui.reportBtn]
        for btn in buttons_list:
            if self.button_states[btn]:
                if self.styleSheet() == self.current_theme:
                    btn.setStyleSheet("background-color: #2c313c; border-left: 2px solid rgb(255,255,255);")
                    self.ui.settingsBtn.setStyleSheet("background-color: #2c313c;")
                else:
                    btn.setStyleSheet("background-color: #348498; border-left: 2px solid rgb(255,255,255);")
                    self.ui.settingsBtn.setStyleSheet("background-color: #348498;")

        self.ui.infoBtn.setStyleSheet("background-color: transparent;")
