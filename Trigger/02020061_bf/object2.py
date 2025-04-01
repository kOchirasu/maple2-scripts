""" trigger/02020061_bf/object2.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101])
        self.set_user_value(trigger_id=99990014, key='EliteSpawn', value=0)
        self.set_interact_object(trigger_ids=[12000085], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart') == 1:
            return 레버2_체크(self.ctx)


class 레버2_체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[722], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[712]):
            return 레버2_발동(self.ctx)
        if self.user_detected(box_ids=[9012]):
            return 레버2_안내멘트(self.ctx)


class 레버2_안내멘트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020061_BF__OBJECT2__0$', duration=5000, box_ids=['9012'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[712]):
            return 레버2_발동(self.ctx)


class 레버2_발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True)
        self.set_interact_object(trigger_ids=[12000085], state=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02020061_BF__OBJECT2__1$', duration=5000, box_ids=['9012'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000085], state=0):
            return 레버2_몬스터등장(self.ctx)


class 레버2_몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990014, key='EliteSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 레버2_재활성(self.ctx)


class 레버2_재활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000085], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000085], state=0):
            return 레버2_재활성_대기(self.ctx)


class 레버2_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 레버2_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101])
        self.set_user_value(trigger_id=99990014, key='EliteSpawn', value=2)
        self.destroy_monster(spawn_ids=[722], arg2=False)
        self.set_interact_object(trigger_ids=[12000085], state=2)


initial_state = 대기
