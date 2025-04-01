""" trigger/02000471_bf/warpcheck.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040318, key='InteractClear', value=0)
        self.set_user_value(trigger_id=2040323, key='Warp', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Boss') == 1:
            return warp_condition(self.ctx)


"""
class warp(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='10002019clear') != 1 or self.user_value(key='10002020clear') != 1 or self.user_value(key='10002021clear') != 1 or self.user_value(key='10002022clear') != 1 or self.user_value(key='10002023clear') != 1 or self.user_value(key='10002024clear') != 1:
            return warp_condition(self.ctx)
"""

class warp_condition(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return end(self.ctx)
        if self.npc_hp(spawn_id=1999, is_relative=True) <= 70:
            return warp_1st(self.ctx)


class warp_1st(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002106], state=1)
        self.set_interact_object(trigger_ids=[10002107], state=1)
        self.set_mesh(trigger_ids=[1207,1208], visible=True)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARPCHECK__0$', duration=5000, box_ids=['0'])
        self.add_buff(box_ids=[720], skill_id=70002061, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return end(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return warp_go(self.ctx)
        if self.object_interacted(interact_ids=[10002106], state=0):
            return warp_cancel(self.ctx)
        if self.object_interacted(interact_ids=[10002107], state=0):
            return warp_cancel(self.ctx)


class warp_cancel(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002106], state=0)
        self.set_interact_object(trigger_ids=[10002107], state=0)
        self.set_mesh(trigger_ids=[1207,1208])
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARPCHECK__1$', duration=5000, box_ids=['0'])
        self.add_buff(box_ids=[720], skill_id=70002062, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return end(self.ctx)
        if self.npc_hp(spawn_id=1999, is_relative=True) <= 30:
            return warp_2nd(self.ctx)


class warp_go(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002106], state=0)
        self.set_interact_object(trigger_ids=[10002107], state=0)
        self.set_mesh(trigger_ids=[1207,1208])
        self.set_user_value(trigger_id=2040323, key='Warp', value=1)
        self.add_buff(box_ids=[720], skill_id=70002062, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return end(self.ctx)
        if self.npc_hp(spawn_id=1999, is_relative=True) <= 30:
            return warp_2nd(self.ctx)


class warp_2nd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002106], state=1)
        self.set_interact_object(trigger_ids=[10002107], state=1)
        self.set_mesh(trigger_ids=[1207,1208], visible=True, fade=10.0)
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARPCHECK__0$', duration=5000, box_ids=['0'])
        self.add_buff(box_ids=[720], skill_id=70002061, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return end(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return warp_go2(self.ctx)
        if self.object_interacted(interact_ids=[10002106], state=0):
            return warp2_cancel(self.ctx)
        if self.object_interacted(interact_ids=[10002107], state=0):
            return warp2_cancel(self.ctx)


class warp2_cancel(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002106], state=0)
        self.set_interact_object(trigger_ids=[10002107], state=0)
        self.set_mesh(trigger_ids=[1207,1208])
        self.set_event_ui_script(type=BannerType.Text, script='$02000471_BF__WARPCHECK__1$', duration=5000, box_ids=['0'])
        self.add_buff(box_ids=[720], skill_id=70002062, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return end(self.ctx)
        return end(self.ctx)


class warp_go2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002106], state=0)
        self.set_interact_object(trigger_ids=[10002107], state=0)
        self.set_mesh(trigger_ids=[1207,1208])
        self.set_user_value(trigger_id=2040323, key='Warp', value=2)
        self.add_buff(box_ids=[720], skill_id=70002062, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return end(self.ctx)
        return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
