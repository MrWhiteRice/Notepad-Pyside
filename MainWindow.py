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

from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.unsavedChanges = False
        self.fileName = "Untitled"

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
        newAction.triggered.connect(self.Function_File_New)
        menu_File.addAction(newAction)

        newWindowAction = QAction("New &Window", self)
        newWindowAction.setShortcut("Ctrl+Shift+N")
        newWindowAction.triggered.connect(self.Function_File_NewWindow)
        menu_File.addAction(newWindowAction)

        openAction = QAction("&Open...", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.Function_File_Open)
        menu_File.addAction(openAction)

        saveAction = QAction("&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.Function_File_Save)
        menu_File.addAction(saveAction)

        saveAsAction = QAction("Save &As...", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        saveAsAction.triggered.connect(self.Function_File_SaveAs)
        menu_File.addAction(saveAsAction)

        menu_File.addSeparator()

        pageSetupAction = QAction("Page Set&up...", self)
        pageSetupAction.triggered.connect(self.Function_File_PageSetup)
        menu_File.addAction(pageSetupAction)

        printAction = QAction("&Print...", self)
        printAction.setShortcut("Ctrl+P")
        printAction.triggered.connect(self.Function_File_Print)
        menu_File.addAction(printAction)

        menu_File.addSeparator()

        exitAction = QAction("E&xit", self)
        exitAction.triggered.connect(self.Function_File_Exit)
        menu_File.addAction(exitAction)

    def InitEditMenu(self):
        menu_Edit = self.menu.addMenu("&Edit")

        undoAction = QAction("&Undo", self)
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.Function_Edit_Undo)
        menu_Edit.addAction(undoAction)

        redoAction = QAction("R&edo", self)
        redoAction.setShortcut("Ctrl+Shift+Z")
        redoAction.triggered.connect(self.Function_Edit_Redo)
        menu_Edit.addAction(redoAction)

        menu_Edit.addSeparator()

        cutAction = QAction("Cu&t", self)
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.Function_Edit_Cut)
        menu_Edit.addAction(cutAction)

        copyAction = QAction("&Copy", self)
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.Function_Edit_Copy)
        menu_Edit.addAction(copyAction)

        pasteAction = QAction("&Paste", self)
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.Function_Edit_Paste)
        menu_Edit.addAction(pasteAction)

        deleteAction = QAction("De&lete", self)
        deleteAction.setShortcut("Del")
        deleteAction.triggered.connect(self.Function_Edit_Delete)
        menu_Edit.addAction(deleteAction)

        menu_Edit.addSeparator()

        findAction = QAction("&Find...", self)
        findAction.setShortcut("Ctrl+F")
        findAction.triggered.connect(self.Function_Edit_Find)
        menu_Edit.addAction(findAction)

        findNextAction = QAction("Find &Next", self)
        findNextAction.setShortcut("F3")
        findNextAction.triggered.connect(self.Function_Edit_FindNext)
        menu_Edit.addAction(findNextAction)

        findPreviousAction = QAction("Find Pre&vious", self)
        findPreviousAction.setShortcut("Shift+F3")
        findPreviousAction.triggered.connect(self.Function_Edit_FindPrevious)
        menu_Edit.addAction(findPreviousAction)

        replaceAction = QAction("&Replace...", self)
        replaceAction.setShortcut("Ctrl+H")
        replaceAction.triggered.connect(self.Function_Edit_Replace)
        menu_Edit.addAction(replaceAction)

        goToAction = QAction("&Go To...", self)
        goToAction.setShortcut("Ctrl+G")
        goToAction.triggered.connect(self.Function_Edit_GoTo)
        menu_Edit.addAction(goToAction)

        menu_Edit.addSeparator()

        selectAllAction = QAction("Select &All", self)
        selectAllAction.setShortcut("Ctrl+A")
        selectAllAction.triggered.connect(self.Function_Edit_SelectAll)
        menu_Edit.addAction(selectAllAction)

        timeDateAction = QAction("Time/&Date", self)
        timeDateAction.setShortcut("F5")
        timeDateAction.triggered.connect(self.Function_Edit_TimeDate)
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
        #TODO: Check if original state was matched

    def TextChanged(self):
        if self.unsavedChanges == False:
            self.unsavedChanges = True
            self.SetDocumentTitle()

    def Function_File_New(self):
        self.textBox.clear()
        
        self.unsavedChanges = False
        self.fileName = "Untitled"

        self.SetDocumentTitle()

    def Function_File_NewWindow(self):
        print("TODO: Implement new window function")

    def Function_File_Open(self):
        print("TODO: Implement open function")

    def Function_File_Save(self):
        print("TODO: Implement save function")

    def Function_File_SaveAs(self):
        print("TODO: Implement save as function")

    def Function_File_PageSetup(self):
        print("TODO: Implement page setup function")

    def Function_File_Print(self):
        print("TODO: Implement print function")

    def Function_File_Exit(self):
        self.close()
        #TODO: Check if unsaved changes then prompt save

    def Function_Edit_Undo(self):
        self.textBox.undo()
        
    def Function_Edit_Redo(self):
        self.textBox.redo()

    def Function_Edit_Cut(self):
        self.textBox.cut()

    def Function_Edit_Copy(self):
        self.textBox.copy()

    def Function_Edit_Paste(self):
        self.textBox.paste()

    def Function_Edit_Delete(self):
        self.textBox.insertPlainText("")

    def Function_Edit_Find(self):
        print("TODO: create menu to search for text")

    def Function_Edit_FindNext(self):
        print("TODO: create menu to search downward from cursor for text")

    def Function_Edit_FindPrevious(self):
        print("TODO: create menu to search upward from cursor for text")

    def Function_Edit_Replace(self):
        print("TODO: create menu to replace text")

    def Function_Edit_GoTo(self):
        print("TODO: create menu to jump to line")

    def Function_Edit_SelectAll(self):
        self.textBox.selectAll()

    def Function_Edit_TimeDate(self):
        self.textBox.insertPlainText(str(datetime.now().strftime('%H:%M %p %d/%m/%Y')))
