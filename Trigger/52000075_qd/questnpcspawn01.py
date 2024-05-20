""" trigger/52000075_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017])
        self.spawn_monster(spawn_ids=[101,201], auto_target=False) # 레이먼, 경비병
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002668], quest_states=[3]):
            return RemoveNpc01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002668], quest_states=[2]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002668], quest_states=[1]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002667], quest_states=[3]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002667], quest_states=[2]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002667], quest_states=[1]):
            return NpcChange01(self.ctx)


# 40002668 퀘스트 완료 상태
class RemoveNpc01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])


# 40002667 퀘스트 진행중 상태
class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017], visible=True)
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[202,900,901,902], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900,901,902]):
            return MobChange01(self.ctx)


class MobChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobChange02(self.ctx)


class MobChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000075, portal_id=10)
        self.spawn_monster(spawn_ids=[301], auto_target=False) # 어둠의 졸개

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobChange03(self.ctx)


class MobChange03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobChange04(self.ctx)


class MobChange04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobTalk01(self.ctx)


class MobTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001960, script='$52000075_QD__QUESTNPCSPAWN01__0$', time=4) # 어둠의 졸개
        self.set_skip(state=MobTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MobTalk02(self.ctx)


class MobTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobTalk03(self.ctx)


class MobTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600, enable=False)
        self.destroy_monster(spawn_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='abductedRamon')


# 40002667 퀘스트 완료 가능 상태
class GuardDown01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[202], auto_target=False)


initial_state = Wait
