# This is a template file you can use to add Python code to a mode.

# To use it, and it to <your_machine>/modes/<your_mode>/code/<your_mode>.py

# Also, add a blank file called __init__.py to your machine folder root, and
# to your "modes" folder, and to your mode's "code" folder. (3 total)

# Also add a "code: your_mode.YourMode" (or whatever you call it) to the
# "mode:" section of your mode's <mode_name>.yaml configuration file.

from mpf.core.mode import Mode


class BaseMode(Mode):
    def mode_init(self):
        """This code that will run once mode when MPF boots."""
        pass

    def mode_start(self, **kwargs):
        """This code will run every time this mode starts."""
        print('base mode started')
        del kwargs

        # call seek(self.player.bgm_position) to resume OR start music

    def mode_stop(self, **kwargs):
        """This code will run every time this mode stops."""
        # call get_pos() on sound and save
        # to self.player.bgm_position
        print('base mode ended')
        pass
