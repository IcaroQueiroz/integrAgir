from PyQt5.QtGui import QIcon, QPixmap

class Theme:
    def change_theme(self):
        if self.styleSheet() == self.current_theme:
            # Carregue o arquivo CSS para o novo tema desejado
            new_icon = QIcon(":/imagens/img/desligar.png")
            new_home = QPixmap(":/imagens/img/home_t.png")
            new_home68 = QPixmap(":/imagens/img/home68-t.png")
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

                #passoApassoEaj, #passoApassoLacon, #passoApassoCielo, 
                #passoApassoRede, #passoApassoStone{
                    border-radius:14px;
                    border: black;
                    border-style: dotted;
                    border-width: 1.5px;
                    padding: 3px 15px 9px 9px;
                }

                QLineEdit {
                    background-color: #ffffff; /* Cor de fundo */
                    color: #000000; /* Cor do texto */
                    border: 1px solid #cccccc; /* Borda */
                    border-radius: 2px; /* Cantos arredondados */
                    padding: 6px; /* Espaçamento interno */
                }

                QLineEdit:focus {
                    border-color: #0000ff; /* Cor da borda quando em foco */
                    outline: none; /* Remove a linha de contorno padrão */
                }

                QGroupBox {
                    background-color: rgba(128, 128, 128, 0.3);
                    border: 1px; /* Borda */
                    border-radius: 4px; /* Cantos arredondados */
                    margin-top: 6px; /* Espaçamento superior */
                }

                QGroupBox::title {
                    subcontrol-origin: margin;
                    subcontrol-position: top left;
                    padding: 0 5px; /* Espaçamento interno */
                    background-color: #16191d; /* Cor de fundo do título */
                    color: #ffffff; /* Cor do texto do título */
                    border-top-left-radius: 3px; /* Cantos arredondados do título */
                    border-top-right-radius: 3px;
                }

                #widgetRelatorioEmprestimo, #widgetRelatorioCielo, #widgetRelatorioRede, #widgetRelatorioStone {
                    border-radius:15px;
                    border: black;
                    border-style: dotted;
                    border-width: 1.5px;
                }

                /* Outros seletores de estilo para widgets */

            """

        else:
            # Caso contrário, restaure a folha de estilos do tema anterior
            new_theme = self.current_theme
            new_icon = QIcon(":/imagens/img/ligar.png")
            new_home = QPixmap(":/imagens/img/home.png")
            new_home68 = QPixmap(":/imagens/img/home68-.png")

        # Aplique o novo tema para o aplicativo
        self.setStyleSheet(new_theme)
        self.ui.temaBtn.setIcon(new_icon)
        self.ui.labelHome.setPixmap(new_home)
        self.ui.labelHome1.setPixmap(new_home68)
        self.ui.labelHome2.setPixmap(new_home68)

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
