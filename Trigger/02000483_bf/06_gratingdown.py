""" trigger/02000483_bf/06_gratingdown.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002051], state=0) # Lever_BlockStart
        self.set_interact_object(trigger_ids=[10002052], state=0) # Lever_BlockOff
        self.set_mesh(trigger_ids=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211]) # GratingDown
        self.set_mesh(trigger_ids=[6300,6301,6302,6303,6304,6305], visible=True) # GratingUp
        # InvisibleBarrier_TOKfalse
        self.set_mesh(trigger_ids=[3901])
        self.set_breakable(trigger_ids=[6000]) # Grating_Start
        self.set_breakable(trigger_ids=[6001]) # Grating_Start
        self.set_breakable(trigger_ids=[6002]) # Grating_Start
        self.set_breakable(trigger_ids=[6003]) # Grating_Start
        self.set_breakable(trigger_ids=[6004]) # Grating_Start
        self.set_breakable(trigger_ids=[6005]) # Grating_Start
        self.set_breakable(trigger_ids=[6006]) # Grating_Start
        self.set_breakable(trigger_ids=[6007]) # Grating_Start
        self.set_breakable(trigger_ids=[6008]) # Grating_Start
        self.set_breakable(trigger_ids=[6009]) # Grating_Start
        self.set_breakable(trigger_ids=[6010]) # Grating_Start
        self.set_breakable(trigger_ids=[6011]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6000]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6001]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6002]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6003]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6004]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6005]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6006]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6007]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6008]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6009]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6010]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6011]) # Grating_Start
        self.set_breakable(trigger_ids=[6100]) # Grating_Off
        self.set_breakable(trigger_ids=[6101]) # Grating_Off
        self.set_breakable(trigger_ids=[6102]) # Grating_Off
        self.set_breakable(trigger_ids=[6103]) # Grating_Off
        self.set_breakable(trigger_ids=[6104]) # Grating_Off
        self.set_breakable(trigger_ids=[6105]) # Grating_Off
        self.set_breakable(trigger_ids=[6106]) # Grating_Off
        self.set_breakable(trigger_ids=[6107]) # Grating_Off
        self.set_breakable(trigger_ids=[6108]) # Grating_Off
        self.set_breakable(trigger_ids=[6109]) # Grating_Off
        self.set_breakable(trigger_ids=[6110]) # Grating_Off
        self.set_breakable(trigger_ids=[6111]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6100]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6101]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6102]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6103]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6104]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6105]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6106]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6107]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6108]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6109]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6110]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6111]) # Grating_Off
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_user_value(key='BlockEnable', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlockEnable') == 1:
            return BlockEnable(self.ctx)


class BlockEnable(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002051], state=1) # Lever_BlockStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002051], state=0):
            return BlockStart(self.ctx)


class BlockStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6300,6301,6302,6303,6304,6305], start_delay=100, fade=2.0) # GratingUp
        self.set_breakable(trigger_ids=[6000], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6001], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6002], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6003], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6004], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6005], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6006], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6007], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6008], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6009], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6010], enable=True) # Grating_Start
        self.set_breakable(trigger_ids=[6011], enable=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6000], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6001], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6002], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6003], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6004], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6005], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6006], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6007], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6008], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6009], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6010], visible=True) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6011], visible=True) # Grating_Start

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BlockIng(self.ctx)


class BlockIng(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # InvisibleBarrier_TOKfalse
        self.set_mesh(trigger_ids=[3901], visible=True)
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BlockEnd(self.ctx)


class BlockEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], visible=True) # GratingDown
        self.set_breakable(trigger_ids=[6000]) # Grating_Start
        self.set_breakable(trigger_ids=[6001]) # Grating_Start
        self.set_breakable(trigger_ids=[6002]) # Grating_Start
        self.set_breakable(trigger_ids=[6003]) # Grating_Start
        self.set_breakable(trigger_ids=[6004]) # Grating_Start
        self.set_breakable(trigger_ids=[6005]) # Grating_Start
        self.set_breakable(trigger_ids=[6006]) # Grating_Start
        self.set_breakable(trigger_ids=[6007]) # Grating_Start
        self.set_breakable(trigger_ids=[6008]) # Grating_Start
        self.set_breakable(trigger_ids=[6009]) # Grating_Start
        self.set_breakable(trigger_ids=[6010]) # Grating_Start
        self.set_breakable(trigger_ids=[6011]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6000]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6001]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6002]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6003]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6004]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6005]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6006]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6007]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6008]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6009]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6010]) # Grating_Start
        self.set_visible_breakable_object(trigger_ids=[6011]) # Grating_Start

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BlockDisable(self.ctx)


class BlockDisable(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002052], state=1) # Lever_BlockOff

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002052], state=0):
            return BlockOffStart(self.ctx)


class BlockOffStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6200,6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211], start_delay=100, fade=2.0) # GratingDown
        self.set_breakable(trigger_ids=[6100], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6101], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6102], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6103], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6104], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6105], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6106], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6107], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6108], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6109], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6110], enable=True) # Grating_Off
        self.set_breakable(trigger_ids=[6111], enable=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6100], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6101], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6102], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6103], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6104], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6105], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6106], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6107], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6108], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6109], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6110], visible=True) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6111], visible=True) # Grating_Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BlockOffIng(self.ctx)


class BlockOffIng(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # InvisibleBarrier_TOKfalse
        self.set_mesh(trigger_ids=[3901])
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BlockOffEnd(self.ctx)


class BlockOffEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6300,6301,6302,6303,6304,6305], visible=True) # GratingUp
        self.set_breakable(trigger_ids=[6100]) # Grating_Off
        self.set_breakable(trigger_ids=[6101]) # Grating_Off
        self.set_breakable(trigger_ids=[6102]) # Grating_Off
        self.set_breakable(trigger_ids=[6103]) # Grating_Off
        self.set_breakable(trigger_ids=[6104]) # Grating_Off
        self.set_breakable(trigger_ids=[6105]) # Grating_Off
        self.set_breakable(trigger_ids=[6106]) # Grating_Off
        self.set_breakable(trigger_ids=[6107]) # Grating_Off
        self.set_breakable(trigger_ids=[6108]) # Grating_Off
        self.set_breakable(trigger_ids=[6109]) # Grating_Off
        self.set_breakable(trigger_ids=[6110]) # Grating_Off
        self.set_breakable(trigger_ids=[6111]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6100]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6101]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6102]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6103]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6104]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6105]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6106]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6107]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6108]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6109]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6110]) # Grating_Off
        self.set_visible_breakable_object(trigger_ids=[6111]) # Grating_Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BlockEnable(self.ctx)


initial_state = Setting
