""" trigger/99999925/main.xml """
import trigger_api


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206,207], auto_target=False)
        self.spawn_monster(spawn_ids=[211], auto_target=False)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[221,222,223,224,225,226,227,228], auto_target=False)
        self.spawn_monster(spawn_ids=[230,231,232,233], auto_target=False)
        self.set_mesh(trigger_ids=[301])
        self.move_npc(spawn_id=230, patrol_name='MS2PatrolData0')
        self.move_npc(spawn_id=231, patrol_name='MS2PatrolData1')
        self.move_npc(spawn_id=232, patrol_name='MS2PatrolData11')
        self.move_npc(spawn_id=233, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData22')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData3')
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData4')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData5')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=402) >= 1:
            return LoadingStart(self.ctx)


class LoadingStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=1, script='$99999925__MAIN__0$', time=3)
        self.set_ai_extra_data(key='BuffStart', value=1, is_modify=True)
        self.set_skip(state=Dialogue01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Dialogue01Skip(self.ctx)


class Dialogue01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SwitchRandom(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class SwitchRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return switch01(self.ctx)
        if self.random_condition(weight=33.0):
            return switch02(self.ctx)
        if self.random_condition(weight=33.0):
            return switch03(self.ctx)


class switch01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[403]):
            return BrokenCheck(self.ctx)


class switch02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[404]):
            return BrokenCheck(self.ctx)


class switch03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[405]):
            return BrokenCheck(self.ctx)


class BrokenCheck(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='BuffStart', value=2, is_modify=True)
        self.set_actor(trigger_id=601, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=602, visible=True, initial_sequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[401]):
            return BrokenWood(self.ctx)


class BrokenWood(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[411], enable=True)
        self.set_skill(trigger_ids=[412], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return None # Missing State: EndPlay


initial_state = DungeonStart
