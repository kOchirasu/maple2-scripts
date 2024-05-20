""" trigger/02000037_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000931], state=2)
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009]) # Stairs 10
        self.set_mesh(trigger_ids=[4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034]) # Bridge 15
        self.set_mesh(trigger_ids=[4040,4041,4042,4043,4044,4045,4046]) # Slab 7
        self.set_mesh(trigger_ids=[4050], visible=True) # invisible barrier
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[5000]) # StairsAppear
        self.set_effect(trigger_ids=[5001]) # Vibrate

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 난이도체크(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_level() == 2:
            return 레이드(self.ctx)
        if self.dungeon_level() == 3:
            return 카오스레이드(self.ctx)


class 레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000]):
            return 연출딜레이(self.ctx)


class 카오스레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 연출딜레이(self.ctx)


class 연출딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


"""
class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000144, script='$02000037_BF__BOSSSPAWN__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출종료(self.ctx)
"""

class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_cinematic_ui(type=0)
        # self.set_cinematic_ui(type=2)
        self.set_interact_object(trigger_ids=[10000931], state=1)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000931]):
            return 사념등장01(self.ctx)


class 사념등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4050]) # invisible barrier
        self.set_effect(trigger_ids=[5000], visible=True) # StairsAppear
        self.set_effect(trigger_ids=[5001], visible=True) # Vibrate
        self.set_random_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009], visible=True, start_delay=10, fade=50)
        self.set_random_mesh(trigger_ids=[4040,4041,4042,4043,4044,4045,4046], visible=True, start_delay=7, interval=400, fade=50)
        self.set_random_mesh(trigger_ids=[4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034], visible=True, start_delay=15, interval=800, fade=50)


initial_state = 시작대기중
