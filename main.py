# import necessary classes
import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.box import Box

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL

# set up evas hints
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        # create window
        StandardWindow.__init__(self, "elmcalc", "Calculator", size=(600, 400))
        self.callback_delete_request_add(lambda o: elm.exit())

        # create layout box
        self.box = Box(self)
        self.box.size_hint_weight = EXPAND_BOTH
        self.box.size_hint_align = FILL_BOTH
        self.box.show()

    def update(self):
        # update UI
        pass

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()