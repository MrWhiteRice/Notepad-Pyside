from PySide6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QLabel
)

from PySide6.QtGui import (
    QIcon,
    QAction,
    QTextOption
)

from PySide6.QtCore import (
    Qt
)

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.unsavedChanges = False
        self.fileName = "Untitled"

        self.app = app
        self.SetDocumentTitle()
        self.setWindowIcon(QIcon("Resources/Images/Icon.png"))

        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)

        self.textBox = QTextEdit(self)
        self.textBox.setWordWrapMode(QTextOption.NoWrap)
        self.textBox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBox.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBox.setStyleSheet("""
            QTextEdit {
                border: 0;
                border-bottom: 1px solid black;
                border-color: white;
            }
        """)
        self.textBox.textChanged.connect(self.TextChanged)
        mainLayout.addWidget(self.textBox)

        self.InitMenu()
        self.InitStatusBar()

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def InitMenu(self):
        self.menu = self.menuBar()

        self.InitFileMenu()
        self.InitEditMenu()
        self.InitFormatMenu()
        self.InitViewMenu()
        self.InitHelpMenu()

    def InitFileMenu(self):
        menu_File = self.menu.addMenu("&File")
        
        newAction = QAction("&New", self)
        newAction.setShortcut("Ctrl+N")
        menu_File.addAction(newAction)

        newWindowAction = QAction("New &Window", self)
        newWindowAction.setShortcut("Ctrl+Shift+N")
        menu_File.addAction(newWindowAction)

        openAction = QAction("&Open...", self)
        openAction.setShortcut("Ctrl+O")
        menu_File.addAction(openAction)

        saveAction = QAction("&Save", self)
        saveAction.setShortcut("Ctrl+S")
        menu_File.addAction(saveAction)

        saveAsAction = QAction("Save &As...", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        menu_File.addAction(saveAsAction)

        menu_File.addSeparator()

        pageSetupAction = QAction("Page Set&up...", self)
        menu_File.addAction(pageSetupAction)

        printAction = QAction("&Print...", self)
        printAction.setShortcut("Ctrl+P")
        menu_File.addAction(printAction)

        menu_File.addSeparator()

        exitAction = QAction("E&xit", self)
        menu_File.addAction(exitAction)

    def InitEditMenu(self):
        menu_Edit = self.menu.addMenu("&Edit")

        undoAction = QAction("&Undo", self)
        undoAction.setShortcut("Ctrl+Z")
        menu_Edit.addAction(undoAction)

        redoAction = QAction("R&edo", self)
        redoAction.setShortcut("Ctrl+Shift+Z")
        menu_Edit.addAction(redoAction)

        menu_Edit.addSeparator()

        cutAction = QAction("Cu&t", self)
        cutAction.setShortcut("Ctrl+X")
        menu_Edit.addAction(cutAction)

        copyAction = QAction("&Copy", self)
        copyAction.setShortcut("Ctrl+C")
        menu_Edit.addAction(copyAction)

        pasteAction = QAction("&Paste", self)
        pasteAction.setShortcut("Ctrl+V")
        menu_Edit.addAction(pasteAction)

        deleteAction = QAction("De&lete", self)
        deleteAction.setShortcut("Del")
        menu_Edit.addAction(deleteAction)

        menu_Edit.addSeparator()

        findAction = QAction("&Find...", self)
        findAction.setShortcut("Ctrl+F")
        menu_Edit.addAction(findAction)

        findNextAction = QAction("Find &Next", self)
        findNextAction.setShortcut("F3")
        menu_Edit.addAction(findNextAction)

        findPreviousAction = QAction("Find Pre&vious", self)
        findPreviousAction.setShortcut("Shift+F3")
        menu_Edit.addAction(findPreviousAction)

        replaceAction = QAction("&Replace...", self)
        replaceAction.setShortcut("Ctrl+H")
        menu_Edit.addAction(replaceAction)

        goToAction = QAction("&Go To...", self)
        goToAction.setShortcut("Ctrl+G")
        menu_Edit.addAction(goToAction)

        menu_Edit.addSeparator()

        selectAllAction = QAction("Select &All", self)
        selectAllAction.setShortcut("Ctrl+A")
        menu_Edit.addAction(selectAllAction)

        timeDateAction = QAction("Time/&Date", self)
        timeDateAction.setShortcut("F5")
        menu_Edit.addAction(timeDateAction)

    def InitFormatMenu(self):
        menu_Format = self.menu.addMenu("F&ormat")

        wordWrapAction = QAction("&Word Wrap", self)
        menu_Format.addAction(wordWrapAction)

        fontAction = QAction("&Font...", self)
        menu_Format.addAction(fontAction)

    def InitViewMenu(self):
        menu_View = self.menu.addMenu("&View")

        menu_Zoom = menu_View.addMenu("&Zoom")

        zoomInAction = QAction("Zoom &In", self)
        zoomInAction.setShortcut("Ctrl++")
        menu_Zoom.addAction(zoomInAction)

        zoomOutAction = QAction("Zoom &Out", self)
        zoomOutAction.setShortcut("Ctrl+-")
        menu_Zoom.addAction(zoomOutAction)

        restoreDefualtZoomAction = QAction("&Restore Default Zoom", self)
        restoreDefualtZoomAction.setShortcut("Ctrl+0")
        menu_Zoom.addAction(restoreDefualtZoomAction)

        statusBarAction = QAction("&Status Bar", self)
        menu_View.addAction(statusBarAction)

    def InitHelpMenu(self):
        menu_Help = self.menu.addMenu("&Help")

        viewHelpAction = QAction("View &Help", self)
        menu_Help.addAction(viewHelpAction)

        sendFeedbackAction = QAction("Send &Feedback", self)
        menu_Help.addAction(sendFeedbackAction)

        menu_Help.addSeparator()

        aboutNotepadAction = QAction("&About Notepad", self)
        menu_Help.addAction(aboutNotepadAction)

    def InitStatusBar(self):
        statusBar = self.statusBar()

        initSpacer = QLabel("")
        statusBar.addPermanentWidget(initSpacer, 50)

        cursorPosition = QLabel("Ln 1, Col 1")
        statusBar.addPermanentWidget(cursorPosition, 20)

        textZoom = QLabel("100%")
        statusBar.addPermanentWidget(textZoom, 5)

        lineEndings = QLabel("Windows (CRLF)")
        statusBar.addPermanentWidget(lineEndings, 15)

        characterEncoding = QLabel("UTF-8")
        statusBar.addPermanentWidget(characterEncoding, 10)

    def SetDocumentTitle(self):            
        docEdited = "" if self.unsavedChanges == False else "*"
        self.setWindowTitle(docEdited + self.fileName + " - Notepad")
    
    def TextChanged(self):
            print('changed!', self.unsavedChanges)
            if self.unsavedChanges == False:
                print("asdasd")
                self.unsavedChanges = True
                self.SetDocumentTitle()

    
