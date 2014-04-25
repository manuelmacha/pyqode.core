from PyQt4 import QtDesigner


class WidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):
    """
    Base class for writing a designer plugins.

    To write a plugin, inherit from this class and define implement at least:

        - klass()
        - module()

    See :class:`pyqode.core.designer_plugins.code_edit_plugin.CodeEditPlugin`
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initialized = False
        print(self.name(), self.includeFile(), self.objectName())

    def klass(self):
        raise NotImplementedError()

    def initialize(self, form_editor):
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def isContainer(self):
        return False

    def icon(self):
        return None

    def domXml(self):
        return ('<widget class="%s" name="%s">\n</widget>\n' %
                (self.name(), self.objectName()))

    def group(self):
        return 'pyQode'

    def objectName(self):
        return self.name()

    def includeFile(self):
        return self.klass().__module__

    def name(self):
        return self.klass().__name__

    def toolTip(self):
        return ''

    def whatsThis(self):
        return ''

    def createWidget(self, parent):
        return self.klass()(parent)
