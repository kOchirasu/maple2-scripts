""" trigger/52010027_qd/main_quest10003102.xml """
import trigger_api


"""
바람의 골짜기 : 52010027
중간 보스 사라짐
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003102], quest_states=[1]):
            return Del(self.ctx)


class Del(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010027, portal_id=6007)
        self.spawn_monster(spawn_ids=[803])
        self.set_npc_emotion_loop(spawn_id=803, sequence_name='Stun_A', duration=160000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 엔피씨와말을걸면(self.ctx)


class 엔피씨와말을걸면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스몬스터는소멸준비(self.ctx)


class 보스몬스터는소멸준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=완료조건, action='exit')
        self.add_cinematic_talk(npc_id=11003469, msg='$52010027_QD__MAIN_QUEST10003102__0$', duration=4000)
        self.add_cinematic_talk(npc_id=11003469, msg='$52010027_QD__MAIN_QUEST10003102__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 보스몬스터는소멸준비01(self.ctx)


class 보스몬스터는소멸준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003102__2$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003102__3$', duration=3000)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=10000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 보스몬스터는소멸준비02(self.ctx)


class 보스몬스터는소멸준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.add_cinematic_talk(npc_id=11003469, msg='$52010027_QD__MAIN_QUEST10003102__4$', duration=4000)
        self.add_cinematic_talk(npc_id=11003469, msg='$52010027_QD__MAIN_QUEST10003102__5$', duration=3000)
        self.add_cinematic_talk(npc_id=11003469, msg='$52010027_QD__MAIN_QUEST10003102__6$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 보스몬스터는소멸(self.ctx)


class 보스몬스터는소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 보스몬스터는소멸_01(self.ctx)


class 보스몬스터는소멸_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[803])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투종료(self.ctx)


class 전투종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003102__7$', duration=2000)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003102__8$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003102__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 전투종료01(self.ctx)


class 전투종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투종료02(self.ctx)


class 전투종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 완료조건(self.ctx)


class 완료조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, type='trigger', achieve='WindValleyBattle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000051, portal_id=3)


initial_state = idle
